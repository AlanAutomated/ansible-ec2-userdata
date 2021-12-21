# Ansible EC2 UserData module
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An idempotent AWS EC2 UserData module to supplement the official amazon.aws.ec2_instance module. 

## Example Usage
Create a `library` folder within your ansible project and copy the module to the folder.

````
- name: Update EC2 UserData attribute value to foo
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1
    user_data: foo

- name: Update EC2 UserData attribute value to null
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1

- name: Compare the current and new UserData attribute values without updating the EC2 instance
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1
    user_data: 'foo'
  check_mode: on
````