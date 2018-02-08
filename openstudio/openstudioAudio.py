# -*- coding: utf-8 -*-

from pybass import *
from threading import Thread
import openstudioAudioThread
import unicodedata

class openstudioAudioInstance():

    def __init__(self,app):
        self.app = app
        BASS_Init(-1, 44100, 0, 0, 0)

    def playAudio(self):

        self.thread_1 = openstudioAudioThread.openstudioAudioChannel(self.app)
        self.thread_1.path = self.app.getPath().encode("utf-8")
        self.thread_1.start()
        #print(self.thread_1.path)
        print('Start thread')

    def stopAudio(self):
        self.thread_1.stop()
        self.thread_1 = None

    def rewindAudio(self):
        BASS_ChannelSetPosition(self.thread_1.handle, 0, BASS_POS_BYTE)
