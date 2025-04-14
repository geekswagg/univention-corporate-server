#!/bin/sh -e
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2020-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

cachedir=/var/lib/univention-directory-listener
for dir in "$cachedir" /var/lib/univention-ldap/listener; do
	find "$dir" ! -user listener -exec chown listener {} \;
done
