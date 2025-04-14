#!/usr/bin/python3
#
# Univention Management Console
#  MODULEDESC
#
# SPDX-FileCopyrightText: YEAR Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

from univention.lib.i18n import Translation
from univention.management.console.base import Base
from univention.management.console.config import ucr  # noqa: F401
from univention.management.console.log import MODULE  # noqa: F401


_ = Translation('PACKAGENAME').translate


class Instance(Base):
    pass
