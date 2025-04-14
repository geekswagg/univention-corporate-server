#!/usr/bin/python3
#
# Univention App Center
#  Setup file for packaging
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2019-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only
#

from packaging import setup


setup(
    name='univention-appcenter-dev',
    packages=[
        'univention.appcenter.actions',
    ],
    package_dir={
        'univention.appcenter.actions': 'python/appcenter-dev/actions',
    },
)
