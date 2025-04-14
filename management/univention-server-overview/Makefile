#!/usr/bin/make -f
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2017-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

build: www/style.css

%.css: %.styl
	stylus "$<"

clean:
	rm -f www/style.css
