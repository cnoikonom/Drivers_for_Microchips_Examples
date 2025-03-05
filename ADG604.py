from Modules.PCA9671 import pca9671
import time
import numpy as np

class adg604:
    def __init__(self):
        self.selector = pca9671(0x20)

    def selectSwitch(self, switch):
        if switch < 0 or switch > 3:
            raise ValueError("Switch value must be 0-3")

        s1 = (switch & 0x01) != 0
        s2 = (switch & 0x02) != 0


        self.selector.writePort(10, s1)
        self.selector.writePort(12, s2)
