# Ansible EC2 UserData modules
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Local AWS EC2 UserData modules to supplement the official amazon.aws.ec2_instance module. 

## Example Usage
Create a `library` folder within your ansible project and copy the modules to the folder.

````
- name: Update EC2 UserData attribute value of a stopped instance
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1
    user_data: 'foo'

- name: Update EC2 UserData attribute value
  ec2_userdata_info:
    instance_id: i-076XXXX
    region: us-east-1
  register: result

- name: Validate the result
  debug:
    var: result
````