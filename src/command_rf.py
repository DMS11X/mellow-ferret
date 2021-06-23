#
# Title:command_rf.py
# Description: tune receiver but not store frequency
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class CommandRf:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command, bc780):
        self.logger.info(f"command:{command}")
        self.bc780.tune_receiver(123)
        return bc780.ok

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***