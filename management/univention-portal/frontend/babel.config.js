// SPDX-FileCopyrightText: 2025 Univention GmbH
// SPDX-License-Identifier: AGPL-3.0-only

module.exports = {
  presets: ['@vue/cli-plugin-babel/preset'],
  plugins: [
    ['@babel/proposal-decorators', { legacy: true }],
    ['@babel/proposal-class-properties', { loose: true }],
  ],
};
