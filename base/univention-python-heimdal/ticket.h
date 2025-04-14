/*
 * Python Heimdal
 *	Bindings for the ticket object of heimdal
 *
 * Like what you see? Join us!
 * https://www.univention.com/about-us/careers/vacancies/
 *
 * SPDX-FileCopyrightText: 2003-2025 Univention GmbH
 * SPDX-License-Identifier: AGPL-3.0-only
 */
#ifndef __TICKET_H__
#define __TICKET_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <krb5.h>
#include "context.h"

typedef struct {
	PyObject_HEAD
	krb5ContextObject *context;
	krb5_ticket ticket;
} krb5TicketObject;

extern PyTypeObject krb5TicketType;

krb5TicketObject *ticket_new(PyObject *unused, PyObject *args);

#endif /* __TICKET_H__ */
