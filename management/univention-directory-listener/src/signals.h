/*
 * Univention Directory Listener
 *  signal handling
 *
 * Like what you see? Join us!
 * https://www.univention.com/about-us/careers/vacancies/
 *
 * SPDX-FileCopyrightText: 2004-2025 Univention GmbH
 * SPDX-License-Identifier: AGPL-3.0-only
 */

#ifndef _SIGNALS_H_
#define _SIGNALS_H_

void signals_block(void);
void signals_unblock(void);
void signals_init(void);

extern void exit_handler(int sig) __attribute__((noreturn));

#endif /* _SIGNALS_H_ */
