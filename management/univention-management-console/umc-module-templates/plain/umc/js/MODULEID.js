/*
 * SPDX-FileCopyrightText: YEAR Univention GmbH
 * SPDX-License-Identifier: AGPL-3.0-only
 */
/*global define*/

define([
	"dojo/_base/declare",
	"dojo/_base/lang",
	"dojo/on",
	"dojo/topic",
	"umc/dialog",
	"umc/tools",
	"umc/widgets/Page",
	"umc/widgets/Form",
	"umc/widgets/Module",
	"umc/widgets/TextBox",
	"umc/widgets/TextArea",
	"umc/i18n!umc/modules/MODULEID"
], function(declare, lang, on, topic, dialog, tools, Page, Form, Module, TextBox, TextArea, _) {
	return declare("umc.modules.MODULEID", [Module], {
		postMixInProperties: function() {
			this.inherited(arguments);
		},

		buildRendering: function() {
			this.inherited(arguments);
		}
	});
});
