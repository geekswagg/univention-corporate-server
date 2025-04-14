#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2004-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

"""|UDM| module for all setting objects"""


import univention.admin
import univention.admin.filter
import univention.admin.handlers
import univention.admin.handlers.settings.default
import univention.admin.handlers.settings.directory
import univention.admin.handlers.settings.license
import univention.admin.handlers.settings.usertemplate
import univention.admin.localization
import univention.admin.uldap


translation = univention.admin.localization.translation('univention.admin.handlers.settings')
_ = translation.translate

module = 'settings/settings'
superordinate = 'settings/cn'
childs = False
short_description = _('Preferences')
object_name = _('Preference')
object_name_plural = _('Preferences')
long_description = ''
operations = ['search']
virtual = True
options = {}  # type: dict[str, univention.admin.option]
property_descriptions = {}  # type: dict[str, univention.admin.property]

mapping = univention.admin.mapping.mapping()


class object(univention.admin.handlers.simpleLdap):
    module = module


def lookup(co, lo, filter_s, base='', superordinate=None, scope='sub', unique=False, required=False, timeout=-1, sizelimit=0):
    # type: (None, univention.admin.uldap.access, str, str, univention.admin.handlers.simpleLdap | None, str, bool, bool, int, int) -> list[univention.admin.handlers.simpleLdap]
    return [
        obj
        for mod in (univention.admin.handlers.settings.directory, univention.admin.handlers.settings.default, univention.admin.handlers.settings.usertemplate, univention.admin.handlers.settings.license)
        for obj in mod.lookup(co, lo, filter_s, base, superordinate, scope, unique, required, timeout, sizelimit)
    ]


def identify(dn, attr, canonical=False):
    # type: (str, univention.admin.handlers._Attributes, bool) -> None
    pass
