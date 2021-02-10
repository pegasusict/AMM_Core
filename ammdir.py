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

import os
from ammfile import AmmFile as File


class AmmDir:
    """Directory class of AMM"""

    _path: str = False

    def __init__(self, path: str):
        if os.path.exists(path) and os.path.isdir(path):
            self._path = path

    def scan(self):
        """
        :returns list"""
        file_list = os.scandir(self)
        for dir_entry in file_list:
            dir_entry = str(dir_entry)
            if os.path.isdir(dir_entry):
                sub_dir = AmmDir(dir_entry)
                file_list += sub_dir.scan()
            elif os.path.isfile(dir_entry):
                File.file_checker(File, dir_entry)
        return file_list

    def __to_string__(self):
        if self._path is not None:
            return str(self._path)
