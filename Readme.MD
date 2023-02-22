# Light Off
## This script could turn off/on light on raspberry pi

The script could turn off and on the light of Raspberry pi. You could deploy it using ansbile.

## Features
[x] Systemd service file to run the script on system start.

[x] Ansible deployment playbook.

## Usage

Modify `hosts` in `delopy.yml` to your hosts name. 

An Example hosts file:
    [local]
    server_ip ansible_ssh_private_key_file=[path to file] ansible_user=[server username]

Then in shell:
```
pipenv install
pipenv shell
ansible-playbook deploy.yml -i ~/.ansible/hosts
```

To skip ask sudo password, in `/etc/sudoers.d`, make a new file named by your username:
```
[YOUR USERNAME] ALL=(ALL) NOPASSWD:ALL
```