import logging
import psutil
import pytest

class ClassTest:
    """ This class for calculating cpu and ram usage"""
    def __init__(self, logger):
        """initialization of logger"""
        self.logger = logger

    def test_usage_cpu(self):
        """ This testcase used to calculate cpu usage"""
        usage_cpu = psutil.cpu_percent(7)
        assert usage_cpu < 90, "Usage of cpu crossed"
        return usage_cpu

    def test_usage_ram(self):
        """This testcase used to calculate Ram usage"""
        usage_ram = psutil.virtual_memory()[2]
        assert usage_ram < 90, "Usage of Ram crossed"
        return usage_ram

logging.basicConfig(filename='usage.log', level=logging.INFO,
                    format=' %(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
obj_Exe = ClassTest(logger)
logging.info("usage count started")
logging.info(f"usage of ram : {obj_Exe.test_usage_ram()}")
logging.info(f"usage of cpu :{obj_Exe.test_usage_cpu()}")
