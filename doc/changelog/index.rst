.. SPDX-FileCopyrightText: 2021-2025 Univention GmbH
..
.. SPDX-License-Identifier: AGPL-3.0-only

.. _relnotes-changelog:

#########################################################
Changelog for Univention Corporate Server (UCS) |release|
#########################################################

.. _changelog-general:

*******
General
*******

.. _security:

* All security updates issued for UCS 5.2-0 are included:

  * :program:`avahi` (:uv:cve:`2023-38469`, :uv:cve:`2023-38470`,
    :uv:cve:`2023-38471`, :uv:cve:`2023-38472`, :uv:cve:`2023-38473`)
    (:uv:bug:`57914`)

  * :program:`bind9` (:uv:cve:`2024-11187`, :uv:cve:`2024-12705`)
    (:uv:bug:`57926`)

  * :program:`firefox-esr` (:uv:cve:`2024-11704`, :uv:cve:`2025-0237`,
    :uv:cve:`2025-0238`, :uv:cve:`2025-0239`, :uv:cve:`2025-0240`,
    :uv:cve:`2025-0241`, :uv:cve:`2025-0242`, :uv:cve:`2025-0243`,
    :uv:cve:`2025-1009`, :uv:cve:`2025-1010`, :uv:cve:`2025-1011`,
    :uv:cve:`2025-1012`, :uv:cve:`2025-1013`, :uv:cve:`2025-1014`,
    :uv:cve:`2025-1016`, :uv:cve:`2025-1017`) (:uv:bug:`57919`,
    :uv:bug:`57950`)

  * :program:`git` (:uv:cve:`2024-50349`, :uv:cve:`2024-52006`)
    (:uv:bug:`57911`)

  * :program:`glib2.0` (:uv:cve:`2024-52533`) (:uv:bug:`57920`)

  * :program:`gnutls28` (:uv:cve:`2024-12133`, :uv:cve:`2024-12243`)
    (:uv:bug:`57969`)

  * :program:`gsl` (:uv:cve:`2020-35357`) (:uv:bug:`57923`)

  * :program:`intel-microcode` (:uv:cve:`2024-21820`,
    :uv:cve:`2024-21853`, :uv:cve:`2024-23918`) (:uv:bug:`57916`)

  * :program:`jinja2` (:uv:cve:`2024-22195`, :uv:cve:`2024-34064`)
    (:uv:bug:`57927`)

  * :program:`libsoup2.4` (:uv:cve:`2024-52530`, :uv:cve:`2024-52531`,
    :uv:cve:`2024-52532`) (:uv:bug:`57924`)

  * :program:`libtasn1-6` (:uv:cve:`2024-12133`) (:uv:bug:`57966`)

  * :program:`linux` (:uv:cve:`2022-49034`, :uv:cve:`2023-52916`,
    :uv:cve:`2024-26595`, :uv:cve:`2024-27407`, :uv:cve:`2024-35870`,
    :uv:cve:`2024-35956`, :uv:cve:`2024-36479`, :uv:cve:`2024-36899`,
    :uv:cve:`2024-37021`, :uv:cve:`2024-41014`, :uv:cve:`2024-42252`,
    :uv:cve:`2024-42315`, :uv:cve:`2024-42319`, :uv:cve:`2024-43098`,
    :uv:cve:`2024-44950`, :uv:cve:`2024-45828`, :uv:cve:`2024-46809`,
    :uv:cve:`2024-46841`, :uv:cve:`2024-46896`, :uv:cve:`2024-47143`,
    :uv:cve:`2024-47408`, :uv:cve:`2024-47745`, :uv:cve:`2024-48881`,
    :uv:cve:`2024-49571`, :uv:cve:`2024-49861`, :uv:cve:`2024-49891`,
    :uv:cve:`2024-49897`, :uv:cve:`2024-49898`, :uv:cve:`2024-49899`,
    :uv:cve:`2024-49909`, :uv:cve:`2024-49911`, :uv:cve:`2024-49915`,
    :uv:cve:`2024-49917`, :uv:cve:`2024-49925`, :uv:cve:`2024-49929`,
    :uv:cve:`2024-49934`, :uv:cve:`2024-49939`, :uv:cve:`2024-49951`,
    :uv:cve:`2024-49994`, :uv:cve:`2024-49996`, :uv:cve:`2024-50014`,
    :uv:cve:`2024-50047`, :uv:cve:`2024-50051`, :uv:cve:`2024-50055`,
    :uv:cve:`2024-50121`, :uv:cve:`2024-50146`, :uv:cve:`2024-50164`,
    :uv:cve:`2024-50248`, :uv:cve:`2024-50258`, :uv:cve:`2024-50275`,
    :uv:cve:`2024-50304`, :uv:cve:`2024-52332`, :uv:cve:`2024-53099`,
    :uv:cve:`2024-53105`, :uv:cve:`2024-53124`, :uv:cve:`2024-53125`,
    :uv:cve:`2024-53128`, :uv:cve:`2024-53141`, :uv:cve:`2024-53142`,
    :uv:cve:`2024-53145`, :uv:cve:`2024-53146`, :uv:cve:`2024-53148`,
    :uv:cve:`2024-53150`, :uv:cve:`2024-53151`, :uv:cve:`2024-53154`,
    :uv:cve:`2024-53155`, :uv:cve:`2024-53156`, :uv:cve:`2024-53157`,
    :uv:cve:`2024-53158`, :uv:cve:`2024-53161`, :uv:cve:`2024-53164`,
    :uv:cve:`2024-53165`, :uv:cve:`2024-53170`, :uv:cve:`2024-53171`,
    :uv:cve:`2024-53172`, :uv:cve:`2024-53173`, :uv:cve:`2024-53174`,
    :uv:cve:`2024-53175`, :uv:cve:`2024-53180`, :uv:cve:`2024-53181`,
    :uv:cve:`2024-53183`, :uv:cve:`2024-53184`, :uv:cve:`2024-53190`,
    :uv:cve:`2024-53194`, :uv:cve:`2024-53196`, :uv:cve:`2024-53197`,
    :uv:cve:`2024-53198`, :uv:cve:`2024-53206`, :uv:cve:`2024-53207`,
    :uv:cve:`2024-53208`, :uv:cve:`2024-53210`, :uv:cve:`2024-53213`,
    :uv:cve:`2024-53214`, :uv:cve:`2024-53215`, :uv:cve:`2024-53217`,
    :uv:cve:`2024-53220`, :uv:cve:`2024-53226`, :uv:cve:`2024-53227`,
    :uv:cve:`2024-53229`, :uv:cve:`2024-53230`, :uv:cve:`2024-53231`,
    :uv:cve:`2024-53233`, :uv:cve:`2024-53237`, :uv:cve:`2024-53239`,
    :uv:cve:`2024-53240`, :uv:cve:`2024-53241`, :uv:cve:`2024-53680`,
    :uv:cve:`2024-53685`, :uv:cve:`2024-53690`, :uv:cve:`2024-55881`,
    :uv:cve:`2024-55916`, :uv:cve:`2024-56369`, :uv:cve:`2024-56531`,
    :uv:cve:`2024-56532`, :uv:cve:`2024-56533`, :uv:cve:`2024-56539`,
    :uv:cve:`2024-56546`, :uv:cve:`2024-56548`, :uv:cve:`2024-56551`,
    :uv:cve:`2024-56557`, :uv:cve:`2024-56558`, :uv:cve:`2024-56562`,
    :uv:cve:`2024-56567`, :uv:cve:`2024-56568`, :uv:cve:`2024-56569`,
    :uv:cve:`2024-56570`, :uv:cve:`2024-56571`, :uv:cve:`2024-56572`,
    :uv:cve:`2024-56574`, :uv:cve:`2024-56575`, :uv:cve:`2024-56576`,
    :uv:cve:`2024-56578`, :uv:cve:`2024-56579`, :uv:cve:`2024-56581`,
    :uv:cve:`2024-56582`, :uv:cve:`2024-56584`, :uv:cve:`2024-56585`,
    :uv:cve:`2024-56586`, :uv:cve:`2024-56587`, :uv:cve:`2024-56589`,
    :uv:cve:`2024-56590`, :uv:cve:`2024-56593`, :uv:cve:`2024-56594`,
    :uv:cve:`2024-56595`, :uv:cve:`2024-56596`, :uv:cve:`2024-56597`,
    :uv:cve:`2024-56598`, :uv:cve:`2024-56599`, :uv:cve:`2024-56600`,
    :uv:cve:`2024-56601`, :uv:cve:`2024-56602`, :uv:cve:`2024-56603`,
    :uv:cve:`2024-56604`, :uv:cve:`2024-56605`, :uv:cve:`2024-56606`,
    :uv:cve:`2024-56608`, :uv:cve:`2024-56610`, :uv:cve:`2024-56614`,
    :uv:cve:`2024-56615`, :uv:cve:`2024-56616`, :uv:cve:`2024-56619`,
    :uv:cve:`2024-56622`, :uv:cve:`2024-56623`, :uv:cve:`2024-56625`,
    :uv:cve:`2024-56626`, :uv:cve:`2024-56627`, :uv:cve:`2024-56628`,
    :uv:cve:`2024-56629`, :uv:cve:`2024-56630`, :uv:cve:`2024-56631`,
    :uv:cve:`2024-56633`, :uv:cve:`2024-56634`, :uv:cve:`2024-56636`,
    :uv:cve:`2024-56637`, :uv:cve:`2024-56640`, :uv:cve:`2024-56642`,
    :uv:cve:`2024-56643`, :uv:cve:`2024-56644`, :uv:cve:`2024-56645`,
    :uv:cve:`2024-56648`, :uv:cve:`2024-56650`, :uv:cve:`2024-56651`,
    :uv:cve:`2024-56658`, :uv:cve:`2024-56659`, :uv:cve:`2024-56660`,
    :uv:cve:`2024-56661`, :uv:cve:`2024-56662`, :uv:cve:`2024-56663`,
    :uv:cve:`2024-56664`, :uv:cve:`2024-56665`, :uv:cve:`2024-56670`,
    :uv:cve:`2024-56672`, :uv:cve:`2024-56675`, :uv:cve:`2024-56677`,
    :uv:cve:`2024-56678`, :uv:cve:`2024-56679`, :uv:cve:`2024-56681`,
    :uv:cve:`2024-56683`, :uv:cve:`2024-56687`, :uv:cve:`2024-56688`,
    :uv:cve:`2024-56690`, :uv:cve:`2024-56691`, :uv:cve:`2024-56693`,
    :uv:cve:`2024-56694`, :uv:cve:`2024-56698`, :uv:cve:`2024-56700`,
    :uv:cve:`2024-56701`, :uv:cve:`2024-56703`, :uv:cve:`2024-56704`,
    :uv:cve:`2024-56705`, :uv:cve:`2024-56707`, :uv:cve:`2024-56708`,
    :uv:cve:`2024-56709`, :uv:cve:`2024-56715`, :uv:cve:`2024-56716`,
    :uv:cve:`2024-56717`, :uv:cve:`2024-56718`, :uv:cve:`2024-56720`,
    :uv:cve:`2024-56722`, :uv:cve:`2024-56723`, :uv:cve:`2024-56724`,
    :uv:cve:`2024-56725`, :uv:cve:`2024-56726`, :uv:cve:`2024-56727`,
    :uv:cve:`2024-56728`, :uv:cve:`2024-56739`, :uv:cve:`2024-56741`,
    :uv:cve:`2024-56745`, :uv:cve:`2024-56746`, :uv:cve:`2024-56747`,
    :uv:cve:`2024-56748`, :uv:cve:`2024-56751`, :uv:cve:`2024-56754`,
    :uv:cve:`2024-56755`, :uv:cve:`2024-56756`, :uv:cve:`2024-56759`,
    :uv:cve:`2024-56763`, :uv:cve:`2024-56765`, :uv:cve:`2024-56766`,
    :uv:cve:`2024-56767`, :uv:cve:`2024-56769`, :uv:cve:`2024-56770`,
    :uv:cve:`2024-56774`, :uv:cve:`2024-56776`, :uv:cve:`2024-56777`,
    :uv:cve:`2024-56778`, :uv:cve:`2024-56779`, :uv:cve:`2024-56780`,
    :uv:cve:`2024-56781`, :uv:cve:`2024-56783`, :uv:cve:`2024-56785`,
    :uv:cve:`2024-56787`, :uv:cve:`2024-57791`, :uv:cve:`2024-57792`,
    :uv:cve:`2024-57798`, :uv:cve:`2024-57807`, :uv:cve:`2024-57838`,
    :uv:cve:`2024-57849`, :uv:cve:`2024-57850`, :uv:cve:`2024-57874`,
    :uv:cve:`2024-57876`, :uv:cve:`2024-57887`, :uv:cve:`2024-57892`,
    :uv:cve:`2024-57907`, :uv:cve:`2024-57946`) (:uv:bug:`57913`,
    :uv:bug:`57948`)

  * :program:`linux-signed-amd64` (:uv:cve:`2023-52916`,
    :uv:cve:`2024-27407`, :uv:cve:`2024-35870`, :uv:cve:`2024-35956`,
    :uv:cve:`2024-36479`, :uv:cve:`2024-36899`, :uv:cve:`2024-37021`,
    :uv:cve:`2024-41014`, :uv:cve:`2024-42252`, :uv:cve:`2024-42315`,
    :uv:cve:`2024-44950`, :uv:cve:`2024-46809`, :uv:cve:`2024-49861`,
    :uv:cve:`2024-49891`, :uv:cve:`2024-49897`, :uv:cve:`2024-49898`,
    :uv:cve:`2024-49899`, :uv:cve:`2024-49909`, :uv:cve:`2024-49911`,
    :uv:cve:`2024-49915`, :uv:cve:`2024-49917`, :uv:cve:`2024-49925`,
    :uv:cve:`2024-49929`, :uv:cve:`2024-49939`, :uv:cve:`2024-49951`,
    :uv:cve:`2024-49994`, :uv:cve:`2024-49996`, :uv:cve:`2024-50014`,
    :uv:cve:`2024-50047`, :uv:cve:`2024-50055`, :uv:cve:`2024-50121`,
    :uv:cve:`2024-50146`, :uv:cve:`2024-50164`, :uv:cve:`2024-50248`,
    :uv:cve:`2024-50258`, :uv:cve:`2024-50275`, :uv:cve:`2024-50304`,
    :uv:cve:`2024-53099`, :uv:cve:`2024-53105`, :uv:cve:`2024-53124`,
    :uv:cve:`2024-53125`, :uv:cve:`2024-53128`, :uv:cve:`2024-53141`,
    :uv:cve:`2024-53142`, :uv:cve:`2024-53164`, :uv:cve:`2024-53170`,
    :uv:cve:`2024-53229`, :uv:cve:`2024-53240`, :uv:cve:`2024-53241`,
    :uv:cve:`2024-53685`, :uv:cve:`2024-56551`, :uv:cve:`2024-56582`,
    :uv:cve:`2024-56599`, :uv:cve:`2024-56608`, :uv:cve:`2024-56631`,
    :uv:cve:`2024-56664`, :uv:cve:`2024-56703`, :uv:cve:`2024-56709`,
    :uv:cve:`2024-56715`, :uv:cve:`2024-56718`, :uv:cve:`2024-56759`,
    :uv:cve:`2024-57887`, :uv:cve:`2024-57892`, :uv:cve:`2024-57907`)
    (:uv:bug:`57930`, :uv:bug:`57948`)

  * :program:`nvidia-graphics-drivers` (:uv:cve:`2024-0126`)
    (:uv:bug:`57925`)

  * :program:`openjpeg2` (:uv:cve:`2021-3575`, :uv:cve:`2023-39327`,
    :uv:cve:`2024-56826`, :uv:cve:`2024-56827`) (:uv:bug:`57928`)

  * :program:`python-tornado` (:uv:cve:`2023-28370`,
    :uv:cve:`2024-52804`) (:uv:bug:`57918`)

  * :program:`python-urllib3` (:uv:cve:`2023-43804`,
    :uv:cve:`2023-45803`, :uv:cve:`2024-37891`) (:uv:bug:`57931`)

  * :program:`python3.11` (:uv:cve:`2023-27043`, :uv:cve:`2024-11168`,
    :uv:cve:`2024-6923`, :uv:cve:`2024-7592`, :uv:cve:`2024-9287`)
    (:uv:bug:`57915`)

  * :program:`qemu` (:uv:cve:`2024-7409`) (:uv:bug:`57922`)

  * :program:`rsync` (:uv:cve:`2024-12084`, :uv:cve:`2024-12085`,
    :uv:cve:`2024-12086`, :uv:cve:`2024-12087`, :uv:cve:`2024-12088`,
    :uv:cve:`2024-12747`) (:uv:bug:`57932`)

  * :program:`setuptools` (:uv:cve:`2024-6345`) (:uv:bug:`57917`)

  * :program:`tiff` (:uv:cve:`2023-25433`, :uv:cve:`2023-26965`,
    :uv:cve:`2023-26966`, :uv:cve:`2023-2908`, :uv:cve:`2023-3618`,
    :uv:cve:`2023-52356`, :uv:cve:`2024-7006`) (:uv:bug:`57921`)

  * :program:`util-linux` (:uv:cve:`2024-28085`) (:uv:bug:`57929`)

  * :program:`xen` (:uv:cve:`2023-28746`, :uv:cve:`2023-46841`,
    :uv:cve:`2023-46842`, :uv:cve:`2024-2193`, :uv:cve:`2024-2201`,
    :uv:cve:`2024-31142`, :uv:cve:`2024-31143`, :uv:cve:`2024-31145`,
    :uv:cve:`2024-31146`, :uv:cve:`2024-45817`, :uv:cve:`2024-45818`,
    :uv:cve:`2024-45819`) (:uv:bug:`57912`)


.. _debian:

* The following updated packages from Debian 0.0 are included:

  :program:`FIXME`

.. _maintained:

* The following packages have been moved to the maintained repository of UCS:

.. _changelog-umc:

*****************************
Univention Management Console
*****************************

.. _changelog-umc-user:

User management
===============

* The Message-ID header has been added to emails sent via Self Service to
  prevent rejection by certain email providers (:uv:bug:`57512`).

.. _changelog-deployment:

*******************
Software deployment
*******************

* Fix the link to the 5.2 changelog for the preup check (:uv:bug:`57973`).

.. _changelog-service:

***************
System services
***************

.. _changelog-service-saml:

SAML
====

* Fixed an issue that causes `univention-keycloak` to crash on system that were
  not running UCR (:uv:bug:`57964`).

* Fixed the link to the 5.2 changelog in `univention-keycloak-migration-status`
  (:uv:bug:`57973`).

.. _changelog-service-proxy:

Proxy services
==============

* You can now manually configure the squid cache settings. Any value other than
  `ufs` in the UCRV `squid/cache/format` disables the cache configuration in
  `squid.conf`. A custom squid cache configuration can be added to
  `/etc/squid/local.conf` (:uv:bug:`57775`).

