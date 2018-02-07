# -*- coding: utf-8 -*-

from pybass import *
from threading import Thread
import openstudioAudioThread

class openstudioAudioInstance():

    def __init__(self,app):
        self.app = app
        BASS_Init(-1, 44100, 0, 0, 0)
        self.handle = BASS_StreamCreateFile(False, b"X_Perience_-_Magic_Fields.mp3", 0, 0, 0)

    def playAudio(self):
        thread_1 = openstudioAudioThread.openstudioAudioChannel(self.handle, self.app)
        thread_1.start()

    def stopAudio(self):
        BASS_ChannelStop(self.handle)

    def rewindAudio(self):
        BASS_ChannelSetPosition(self.handle, 0, BASS_POS_BYTE)
