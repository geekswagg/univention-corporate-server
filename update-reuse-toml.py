#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only
"""Create REUSE.toml from all Copyright information in DEB-5 compatible copyright information in Debian packages in subdirectories."""

import sys
from pathlib import Path

import toml
from debian.copyright import Copyright, NotMachineReadableError  # 0.1.49


REPO_ROOT = Path(".").resolve()
REUSE_TOML_PATH = REPO_ROOT / "REUSE.toml"

DEFAULT_UCS_ANNOTATIONS = [{
    'path': sorted([
        # "**.1",
        # "**.5",
        # "**.8",
        # "**.acl",
        # "**.ai",
        # "base/univention-dvd/data/*/**",
        # "base/univention-dvd/tasks/*/**",
        # "base/univention-dvd/tools/boot/**/parse_isolinux",
        # "base/univention-dvd/ucs**.conf",
        "test/**.cfg",
        "test/utils/id-broker/keycloak_ProxyPass.conf.example",
        "test/utils/id-broker/univention-test-app.conf",
        "test/utils/id-broker/univention-vhosts.conf.example",
        # "**/conffiles/*/**",
        # "**.css",
        # "**.csv",
        # "**.cvd",
        # "**/debian/**",
        "doc/errata/**.yaml",
        "doc/errata/erratum.schema.json",
        "doc/extended-docs/ucr-deprecated.schema.json",
        "**.gitignore",
        ".git-blame-ignore-revs",
        ".gitlab/issue_templates/default.md",
        ".gitlab/merge_request_templates/Default.md",
        "pyproject.toml",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "PULL_REQUEST_TEMPLATE.md",
        # "**.gpg",
        # "**.gz",
        # "**.html",
        # "**.ico",
        # "**.in",
        # "**.ini",
        # "**.jpg",
        # "**.json",
        # "**.ldif",
        # "**.md",
        # "**.mo",
        # "packaging/ucslint/testframework/**",
        # "**.patch",
        # "**.png",
        # "**.po",
        # "**.pot",
        # "**.rml",
        # "**.schema",
        # "**.short",
        # "**.styl",
        # "**.svg",
        # "**.svgz",
        # "**/tests/**",
        # "**/test/**",
        # "**.tmpl",
        # "**.toml",
        # "**.txt",
        # "**/unittest/**",
        # "**.zip",
    ]),
    'SPDX-FileCopyrightText': "2025 Univention GmbH",
    'SPDX-License-Identifier': "AGPL-3.0-only",
}, {
    'path': sorted([
        'doc/**.ai',
        'doc/**.drawio',
        'doc/**.graphml',
        'doc/**.svg',
        'doc/**.txt',
        'doc/**.png',
        "test/product-tests/ucsschool/largeenv-installation.csv",
        "test/scenarios/veyon/veyon.json",
        "test/ucs-gui-tests/installation/vminstall/expected_welcome_screen_with_kde.png",
    ]),
    'SPDX-FileCopyrightText': "2025 Univention GmbH",
    'SPDX-License-Identifier': "LicenseRef-Univention-Proprietary",
}]


def main():
    all_annotations = DEFAULT_UCS_ANNOTATIONS
    for path, dep5 in find_dep5_files():
        annotations = build_annotations(dep5, path)
        all_annotations.extend(annotations)

    reuse_toml = {
        "version": 1,
        "SPDX-PackageName": "Univention Corporate Server",
        "SPDX-PackageSupplier": "Univention GmbH <info@univention.de>",
        "SPDX-PackageDownloadLocation": "https://www.univention.com/",
        "annotations": all_annotations,
    }

    with open(REUSE_TOML_PATH, "w", encoding="utf-8") as f:
        toml.dump(reuse_toml, f)

    print(f"Created: {REUSE_TOML_PATH} with {len(all_annotations)} annotations.")


def find_dep5_files():
    for path in REPO_ROOT.glob("**/debian/copyright"):
        try:
            with open(path, encoding="utf-8") as fd:
                dep5 = Copyright(fd.read())
        except NotMachineReadableError:
            print('Not machine readable', path, file=sys.stderr)
            continue
        yield path, dep5


def normalize_pattern(pattern: str, base_path: Path):
    pattern = pattern.strip()
    # FIXME: multiple conditions may be true
    if pattern.endswith("/*"):
        pattern = pattern[:-1] + "**"
    elif pattern.endswith("/"):
        pattern += "**"
    elif '*' in pattern:
        pattern = pattern.replace('*', '**')
    elif '?' in pattern:
        pattern = pattern.replace('?', '*')

    full_path = base_path.parent.parent / pattern
    try:
        rel_path = full_path.relative_to(REPO_ROOT)
    except ValueError:
        rel_path = full_path
    return str(rel_path)


def build_annotations(dep5, base_path: Path):
    annotations = []
    for para in dep5.all_paragraphs():
        try:
            license_id = para.license.synopsis
            if not para.files or not license_id:
                continue
        except AttributeError:
            continue

        # if license_id.startswith('AGPL-3.0-only'):
        #     continue

        paths = [normalize_pattern(p, base_path) for p in para.files]
        annotation = {
            "path": paths if len(paths) > 1 else paths[0],
            "precedence": "override",
            "SPDX-License-Identifier": license_id.replace('WITH', 'AND'),
        }
        if hasattr(para, 'copyright'):
            annotation["SPDX-FileCopyrightText"] = para.copyright.strip()
        annotations.append(annotation)
    return annotations


if __name__ == "__main__":
    main()
