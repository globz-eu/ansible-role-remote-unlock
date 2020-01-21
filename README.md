# Remote Unlock

Configure remote unlock LUKS encrypted Ubuntu Bionic using dropbear-initramfs.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
remote_unlock_dropbear_port: 10022
remote_unlock_dropbear_options: "-R -E -s -j -k -K 20 -I 120 -p {{ remote_unlock_dropbear_port }} -c /usr/bin/cryptroot-unlock"
remote_unlock_grub_cmdline_linux: "net.ifnames=0 biosdevname=0 ip=1.2.3.4::1.2.3.1:255.255.255.0::eth0:off"
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
