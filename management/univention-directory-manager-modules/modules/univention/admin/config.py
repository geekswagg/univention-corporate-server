#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2004-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

"""
|UDM| configuration basics

.. deprecated:: UCS 4.4
"""


from types import ModuleType  # noqa: F401

import univention.admin.modules
import univention.admin.uldap


class config:
    """
    |UDM| configuration object.

    .. deprecated:: UCS 4.4
            use `None` instead
    """

    def __init__(self, host=''):
        # type: (str) -> None
        base = univention.admin.uldap.getBaseDN(host)
        self.data = {
            'ldap/base': base,
            'ldap/base/dns': 'cn=dns,' + base,
            'ldap/base/dhcp': 'cn=dhcp,' + base,
        }

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __contains__(self, key):
        return key in self.data

    def items(self):
        return self.data.items()


def getDefaultContainer(lo, module):
    # type: (univention.admin.uldap.access, ModuleType | str) -> str | None
    """
    Return any random default container for a UDM module.

    .. deprecated:: UCS 4.4

    :param lo: A LDAP connection object.
    :param module: The name of a UDM module.
    :returns: A distinguished name.
    """
    if module == 'dns/':
        module = 'dns/dns'
    try:
        return univention.admin.modules._get(module).object.get_default_containers(lo)[0]
    except IndexError:
        return None


def getDefaultValue(lo, name, position=None):
    # type: (univention.admin.uldap.access, str, univention.admin.uldap.position | None) -> str | None
    """
    Return the default value for a UDM module.

    :param univention.admin.uldap.access lo: A LDAP connection object.
    :param str name: The name of a property.
    :param univention.admin.uldap.position position: A UDM position specifying the LDAP base container.
    :returns: The default value.
    """
    if name == 'group':
        att = 'univentionDefaultGroup'
    elif name == 'computerGroup':
        att = 'univentionDefaultComputerGroup'
    else:
        att = name

    if position:
        _dn, attrs = lo.search(filter='objectClass=univentionDefault', attr=[att], base=position.getDomain(), scope='domain', unique=True, required=True)[0]
    else:
        _dn, attrs = lo.search(filter='objectClass=univentionDefault', attr=[att], scope='domain', unique=True, required=True)[0]
    result = attrs.get(att, [None])[0]
    if result is not None:
        return result.decode('UTF-8')
