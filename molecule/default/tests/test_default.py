import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dropbear_initramfs_package(host):
    packages = ['dropbear', 'initramfs-tools', 'busybox']

    for package in packages:
        pkg = host.package(package)

        assert pkg.is_installed


def test_dropbear_config(host):
    config = host.file('/etc/default/dropbear')

    assert config.exists
    assert config.user == 'root'
    assert config.group == 'root'
    assert oct(config.mode) == '0o644'
    assert config.contains(r'^NO_START=1$')


def test_dropbear_authorized_keys(host):
    authorized_keys = host.file('/etc/dropbear-initramfs/authorized_keys')

    assert authorized_keys.exists
    assert authorized_keys.user == 'root'
    assert authorized_keys.group == 'root'
    assert oct(authorized_keys.mode) == '0o600'
    assert authorized_keys.contains(r'ssh-rsa AAAABLABLA== user@host')


def test_unlock_script(host):
    crypt_unlock = host.file('/etc/initramfs-tools/hooks/crypt_unlock.sh')

    assert crypt_unlock.exists
    assert crypt_unlock.user == 'root'
    assert crypt_unlock.group == 'root'
    assert oct(crypt_unlock.mode) == '0o750'
    assert (
        crypt_unlock.sha256sum ==
        'f831eaa22cdce1acc742efcc4c5571b86ae967194d24b23f15609762162ca2e4'
    )


def test_cleanup_script(host):
    cleanup = host.file('/etc/initramfs-tools/scripts/init-bottom/cleanup.sh')

    assert cleanup.exists
    assert cleanup.user == 'root'
    assert cleanup.group == 'root'
    assert oct(cleanup.mode) == '0o750'
    assert (
        cleanup.sha256sum ==
        'e778d8aefb988e5645488e20759fbb7326783ff89840706aa0e8fc00447ee328'
    )


def test_initramfs_conf(host):
    initramfs_conf = host.file('/etc/initramfs-tools/initramfs.conf')

    assert initramfs_conf.exists
    assert initramfs_conf.user == 'root'
    assert initramfs_conf.group == 'root'
    assert oct(initramfs_conf.mode) == '0o644'
    assert initramfs_conf.contains(r'^IP=:::::eth0:dhcp')
