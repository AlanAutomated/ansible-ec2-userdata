# Ansible EC2 UserData modules
Local AWS EC2 UserData modules to supplement the official amazon.aws.ec2_instance module. 

## Example Usage
Create a `library` folder within your ansible project and copy the modules to the folder.

````
- name: Update EC2 UserData attribute value
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