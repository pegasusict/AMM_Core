#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyleft 🄯 2021 Mattijs Snepvangers.
#  This file is part of Audiophiles' Music Manager, hereafter named AMM.
#
#  AMM is free software: you can redistribute it and/or modify  it under the terms of the
#   GNU General Public License as published by  the Free Software Foundation, either version 3
#   of the License or any later version.
#
#  AMM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#   along with AMM.  If not, see <https://www.gnu.org/licenses/>.
from os.path import basename
from PPL import load
# from ammfile import AmmFile

Version = load(variant="version", args=(0, 0, 0, 'dev', 0, '20210208.0'))

AMM_ORG_NAME = "Pegasus ICT Dienstverlening"
AMM_SUITE_NAME_SHORT = "AMM"
AMM_SUITE_NAME_FULL = "Audiophiles' Music Manager"
AMM_DISPLAY_NAME = AMM_SUITE_NAME_FULL + " Core"
AMM_APP_ID = "org.pegasus-ict.amm_core"
AMM_APP_NAME = "AMM Core"
AMM_VERSION = Version.to_string()
AMM_SCRIPT = basename(__file__)

cfg = load(group="configuration", variant=filetype, args=(filename='config.ini', filetype=filetype))
