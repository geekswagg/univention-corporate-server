#!/bin/bash
#
# Univention Mail Postfix
#  call postmap on transport map and reload postfix
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2004-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

postmap /etc/postfix/transport
