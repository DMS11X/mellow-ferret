#
# Title:bc780.py
# Description: bc780 state
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class Bc780:
    def __init__(self):
        self.logger = logging.getLogger()

        self.system_information = "SI BC245XLT,000000228,102\r"
        self.version_revision = "VR1.00\r"

    def execute(self, command:str):
        pass

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***