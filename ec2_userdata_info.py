#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ec2_userdata

short_description: Update an EC2 UserData attribute

version_added: "1.0.0"

description: Updates the UserData attribute value of a stopped EC2 instance.

options:
    aws_access_key:
        description: If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.
        required: false
        type: str
    aws_secret_key:
        description: If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.
        required: false
        type: str
    instance_id:
        description: The ID of the EC2 instance.
        required: true
        type: str
    region:
        description: The region of the EC2 instance.
        required: true
        type: str
    user_data:
        description: The new UserData attribute value.
        required: true
        type: str

author:
    - Alan Haynes (@alanautomated)
"""

EXAMPLES = r"""
- name: Update EC2 UserData attribute value
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1
    user_data: 'foo'
"""

RETURN = r"""
None
"""

import os

import boto3
import botocore
from ansible.module_utils.basic import AnsibleModule
from botocore.exceptions import ClientError


def run_module():
    module_args = dict(
        aws_access_key=dict(type="str", required=False, no_log=True),
        aws_secret_key=dict(type="str", required=False, no_log=True),
        instance_id=dict(type="str", required=True),
        region=dict(type="str", required=True),
        user_data=dict(type="str", required=True),
    )

    result = dict(changed=False)

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    access_key = module.params.get("aws_access_key")
    secret_key = module.params.get("aws_secret_key")
    instance_id = module.params.get("instance_id")
    region = module.params.get("region")
    user_data = module.params.get("user_data")

    # Use environment variables if module arguments not passed
    if not access_key:
        if os.environ.get("AWS_ACCESS_KEY_ID"):
            access_key = os.environ["AWS_ACCESS_KEY_ID"]
        elif os.environ.get("AWS_ACCESS_KEY"):
            access_key = os.environ["AWS_ACCESS_KEY"]
        elif os.environ.get("EC2_ACCESS_KEY"):
            access_key = os.environ["EC2_ACCESS_KEY"]
        else:
            module.fail_json(
                msg="Parameter aws_access_key or equivalent environment variable required."
            )

    if not secret_key:
        if os.environ.get("AWS_SECRET_ACCESS_KEY"):
            secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
        elif os.environ.get("AWS_SECRET_KEY"):
            secret_key = os.environ["AWS_SECRET_KEY"]
        elif os.environ.get("EC2_SECRET_KEY"):
            secret_key = os.environ["EC2_SECRET_KEY"]
        else:
            module.fail_json(
                msg="Parameter aws_secret_key or equivalent environment variable required."
            )

    try:
        client = boto3.client(
            "ec2",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )

        response = client.modify_instance_attribute(
            InstanceId=instance_id, UserData={"Value": user_data}
        )
    except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
        module.fail_json(msg=str(e))

    try:
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            result["changed"] = True
    except KeyError:
        pass

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
Verifying
