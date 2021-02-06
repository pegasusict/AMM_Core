#!/bin/env python3
import os
from pymediainfo import MediaInfo as info


class AmmFile:
    """File class of AMM"""

    def scan_dir(self, directory):
        """Scans given directory recursively and hands each file to file_checker()"""
        file_list = os.scandir(directory)
        for file in file_list:
            self.file_checker(file)
        return self

    def file_checker(self, file):
        file_info = info.parse(file)

        return self
