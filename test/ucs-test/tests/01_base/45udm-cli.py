#!/usr/share/ucs-test/runner pytest-3 -s -l -vvv
## desc: Create a user via udm cli and authenticate via LDAP and Samba
## roles:
##  - domaincontroller_master
##  - domaincontroller_backup
##  - domaincontroller_slave
##  - memberserver
## tags:
##  - basic
##  - apptest
##  - skip_admember
## packages:
##  - univention-directory-manager-tools
## exposure: dangerous
## versions:
##  3.0-0: found

import subprocess
import time
from dataclasses import dataclass

import pytest

from univention import uldap
from univention.testing import utils


@dataclass
class User:
    user_dn: str
    username: str
    password: str


@pytest.fixture
def user(udm):
    return User(*udm.create_user(wait_for=True), 'univention')


def test_ldap_connection(ucr, user):
    print("Testing ldap connection")
    if ucr.get('server/role').startswith('domaincontroller_'):
        access = uldap.access(binddn=user.user_dn, bindpw=user.password, base=ucr['ldap/base'])
    else:
        access = uldap.access(ucr['ldap/master'], base=ucr['ldap/base'], binddn=user.user_dn, bindpw=user.password)
    data = access.get(user.user_dn, required=True)
    for (key, value) in data.items():
        print(f"{key} = {value}")
    assert data, data


def test_samba_connection(ucr, user):
    # In case of a memberserver in a S4 environment, we have to
    # wait until the user has been synchronized to Samba 4. Otherwise
    # we can't get a kerberos ticket
    print("Try to get a kerberos ticket for the new user", user.username)
    for _ in range(4 if ucr.get("server/role") == "memberserver" else 1):
        if not subprocess.run(["kinit", "--password-file=STDIN", user.username], input=user.password, text=True, check=False).returncode:
            break
        print("kinit failed. Retry in 4 seconds ...")
        time.sleep(4)
    else:
        pytest.fail("kinit failed after 16 seconds")

    s4_installed = utils.package_installed("univention-samba4")
    if s4_installed or utils.package_installed("univention-samba"):
        host = 'localhost' if s4_installed else ucr.get('ldap/master')
        print(f"Samba Logon with this new user against {host}")

        for _ in range(6):
            if not subprocess.run(("smbclient", "-L", host, "-U", f"{user.username}%{user.password}"), check=False).returncode:
                break
            print("First Samba login failed. Retry in 5 seconds ...")
            time.sleep(5)
        else:
            pytest.fail("Samba login failed after 30 seconds")
