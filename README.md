# Remote Unlock

Configure remote unlock LUKS encrypted Ubuntu Bionic using dropbear-initramfs.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
remote_unlock_network_interface: eth0
remote_unlock_initramfs_conf_ip: ":::::{{ remote_unlock_network_interface }}:dhcp"
remote_unlock_authorized_keys: {}
```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
    remote_unlock_authorized_keys:
      user: ssh-rsa AAAABLABLA== user@host
  roles:
    - role: remote-unlock
```

## License

MIT
