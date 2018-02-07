# -*- coding: utf-8 -*-

from pybass import *
from threading import Thread
import openstudioAudioThread

class openstudioAudioInstance():

    def __init__(self,app):
        self.app = app
        BASS_Init(-1, 44100, 0, 0, 0)
        self.handle = BASS_StreamCreateFile(False, b"test.mp3", 0, 0, 0)
        self.thread_1 = openstudioAudioThread.openstudioAudioChannel(self.handle, self.app)

    def playAudio(self):
        if(self.thread_1.is_alive() == 0):
            self.thread_1.start()
            print('Start thread')
        else:
            BASS_ChannelPlay(self.handle, False)

    def stopAudio(self):
        BASS_ChannelStop(self.handle)

    def rewindAudio(self):
        BASS_ChannelSetPosition(self.handle, 0, BASS_POS_BYTE)
