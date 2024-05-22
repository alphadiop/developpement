# -*- coding: utf-8 -*-
"""
 Verification de la presence du drive odbc attendu
"""

from packaging import version


def compare_version(version_actuel, version_require) -> bool:
    return version.parse(version_actuel) >= version.parse(version_require)
