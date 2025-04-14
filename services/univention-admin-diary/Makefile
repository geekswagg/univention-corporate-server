#!/usr/bin/make -f
#
# Like what you see? Join us!
# https://www.univention.com/about-us/careers/vacancies/
#
# SPDX-FileCopyrightText: 2019-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

build: umc/js/admindiary.css

%.css: %.styl
	stylus "$<"

clean:
	rm -f umc/js/admindiary.css

