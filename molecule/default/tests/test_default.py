import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dropbear_initramfs_package(host):
    dropbear = host.package('dropbear-initramfs')

    assert dropbear.is_installed


def test_dropbear_config(host):
    config = host.file('/etc/dropbear-initramfs/config')

    assert config.exists
    assert config.user == 'root'
    assert config.group == 'root'
    assert oct(config.mode) == '0o644'
    assert config.contains(
        r'^DROPBEAR_OPTIONS="'
        r'-R -E -s -j -k -K 20 -I 120 -p 10022 -c /usr/bin/cryptroot-unlock"$'
    )
    assert config.contains(r'^IFDOWN=\*$')


def test_dropbear_authorized_keys(host):
    authorized_keys = host.file('/etc/dropbear-initramfs/authorized_keys')

    assert authorized_keys.exists
    assert authorized_keys.user == 'root'
    assert authorized_keys.group == 'root'
    assert oct(authorized_keys.mode) == '0o600'
    assert authorized_keys.contains(r'ssh-rsa AAAABLABLA== user@host')


def test_default_grub(host):
    default_grub = host.file('/etc/default/grub')

    assert default_grub.exists
    assert default_grub.user == 'root'
    assert default_grub.group == 'root'
    assert oct(default_grub.mode) == '0o644'
    assert default_grub.contains(
        r'^GRUB_CMDLINE_LINUX="'
        r'net\.ifnames=0 '
        r'biosdevname=0 '
        r'ip=1\.2\.3\.4::1\.2\.3\.1:255\.255\.255\.0::eth0:off"$'
    )
