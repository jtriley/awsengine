#!/usr/bin/env python
import logging
from logger import logger
logger.setLevel(logging.DEBUG)

from PyQt4.QtCore import *
from PyKDE4.kdecore import *
from PyKDE4 import plasmascript

import starcluster

class AWSEngine(plasmascript.DataEngine):
    def __init__(self,parent,args=None):
        plasmascript.DataEngine.__init__(self,parent)

    def init(self):
        self.setMinimumPollingInterval(20000)

    def sources(self):
        sources = ["instances", "images"]
        return sources

    def sourceRequestEvent(self, name):
        return self.updateSourceEvent(name)

    def updateSourceEvent(self, name):
        if name == "images":
            images = starcluster.ec2utils.get_registered_images()
            for image_name in images:
                image = images[image_name]
                image = dict(zip(image.keys(), [QVariant(val) for val in image.values()]))
                self.setData(name, image_name, QVariant(image))
        return True

def CreateDataEngine(parent):
    return AWSEngine(parent)
