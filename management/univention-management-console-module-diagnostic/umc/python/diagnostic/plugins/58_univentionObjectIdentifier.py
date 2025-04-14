#!/usr/bin/python3
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2019-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

import subprocess

from univention.admin.uldap import access, getAdminConnection
from univention.config_registry import ucr_live as ucr
from univention.lib.i18n import Translation
from univention.management.console.modules.diagnostic import Instance, ProblemFixed, Warning  # noqa: A004


_ = Translation('univention-management-console-module-diagnostic').translate

title = 'Unviention Object Identifier'
description = '\n'.join([
    _('All objects of class "univentionObject" should have the attribute "univentionObjectIdentifier" in OpenLDAP.'),
])


def univentionObject_without_univentionObjectIdentifier(lo: access) -> list[str]:
    return lo.searchDn('(&(objectClass=univentionObject)(!(objectClass=univentionLicense))(!(univentionObjectIdentifier=*)))')


def run(_umc_instance: Instance) -> None:
    if ucr.get('server/role') != 'domaincontroller_master':
        return

    lo, _pos = getAdminConnection()
    objs = univentionObject_without_univentionObjectIdentifier(lo)
    num_objs = len(objs)
    if num_objs:
        details = '\n\n' + _('Number of objects that should be fixed: %d') % num_objs
        raise Warning(description + details, buttons=[{
            'action': 'update_objects',
            'label': _('Update %d LDAP objects') % num_objs,
        }])


def update_objects(_umc_instance: Instance) -> None:
    cmd = "/usr/share/univention-ldap/univention-update-univention-object-identifier"
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        raise Warning(output, links=[])
    raise ProblemFixed(buttons=[])


actions = {
    'update_objects': update_objects,
}


if __name__ == '__main__':
    from univention.management.console.modules.diagnostic import main
    main()
