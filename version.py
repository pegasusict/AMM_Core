#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Mattijs Snepvangers.
# This file is part of Audiophiles' Music Manager or AMM for short.
#
# Audiophiles' Music Manager is free software: you can redistribute it and/or modify  it under the terms of the GNU
# General Public License as published by  the Free Software Foundation, either version 3 of the License or any later
# version.
#
# Audiophiles' Music Manager is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Audiophiles' Music Manager.  If not, see <https://www.gnu.org/licenses/>.
# import semantic_version as sem_ver
from collections import namedtuple
import re


class VersionError(Exception):
    pass


class Version(namedtuple('VersionBase', 'major minor patch identifier revision')):
    _version_re = re.compile(r"(\d+)(?:[._](\d+)(?:[._](\d+)[._]?(?:(dev|a|alpha|b|beta|rc|final)[._]?(\d+))?)?)?$")

    _identifiers = {'dev': 0, 'alpha': 1, 'a': 1, 'beta': 2, 'b': 2, 'rc': 3, 'final': 4}

    def __new__(cls, major, minor=0, patch=0, identifier='final', revision=0):
        if identifier not in cls.valid_identifiers():
            raise VersionError("Should be either 'final', 'dev', 'alpha', 'beta' or 'rc'")
        identifier = {'a': 'alpha', 'b': 'beta'}.get(identifier, identifier)
        try:
            major = int(major)
            minor = int(minor)
            patch = int(patch)
            revision = int(revision)
        except (TypeError, ValueError):
            raise VersionError("major, minor, patch and revision must be integer values")
        return super(Version, cls).__new__(cls, major, minor, patch, identifier, revision)

    @classmethod
    def from_string(cls, version_str):
        match = cls._version_re.search(version_str)
        if match:
            (major, minor, patch, identifier, revision) = match.groups()
            major = int(major)
            if minor is None:
                return Version(major)
            minor = int(minor)
            if patch is None:
                return Version(major, minor)
            patch = int(patch)
            if identifier is None:
                return Version(major, minor, patch)
            revision = int(revision)
            return Version(major, minor, patch, identifier, revision)
        raise VersionError("String '%s' does not match regex '%s'" % (version_str,
                                                                      cls._version_re.pattern))

    @classmethod
    def valid_identifiers(cls):
        return set(cls._identifiers.keys())

    def to_string(self, short=False):
        if short and self.identifier in ('alpha', 'beta'):
            version = self._replace(identifier=self.identifier[0])
        else:
            version = self
        if short and version.identifier == 'final':
            if version.patch == 0:
                version_str = '%d.%d' % version[:2]
            else:
                version_str = '%d.%d.%d' % version[:3]
        elif short and version.identifier in ('a', 'b', 'rc'):
            version_str = '%d.%d.%d%s%d' % version
        else:
            version_str = '%d.%d.%d.%s%d' % version
        return version_str

    @property
    def sort_key(self):
        return self[:3] + (self._identifiers.get(self.identifier, 0), self.revision)

    def __str__(self):
        return self.to_string()

    def __lt__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key < other.sort_key

    def __le__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key <= other.sort_key

    def __gt__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key > other.sort_key

    def __ge__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key >= other.sort_key

    def __eq__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key == other.sort_key

    def __ne__(self, other):
        if not isinstance(other, Version):
            other = Version(*other)
        return self.sort_key != other.sort_key

    def __hash__(self):
        return super().__hash__()


def build(year, month, day):
    return None