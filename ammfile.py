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
from uuid import uuid4

from pip._internal.configuration import Configuration
from pymediainfo import MediaInfo


class AmmFile:
    """File class of AMM"""

    _file: str = ''
    _extensions = ('mp2', 'mp3', 'mp4', 'm4a', 'wav', 'wpc', 'aac', 'flac')


    def file_checker(self):
        """Checks file by:
        - checking the extension against a whitelist
        - retrieving the media information from the file
        :returns boolean"""
        file = self._file
        extension = os.path.splitext(file)[-1]
        if not self._extensions.__contains__(extension):
            self.move_to_trash()
        file_info = MediaInfo.parse(file)

        return self

    def move_to_holding_area(self, filepath):
        pass

    def move_to_trash(self):
        os.rename(self._file, Configuration.get_value(Configuration,'trashdir')
