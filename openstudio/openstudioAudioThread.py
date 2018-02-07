# -*- coding: utf-8 -*-

from pybass import *
from threading import Thread
import time

#@SYNCPROC
#def onEndPlay(handle, buffer, length, user):
#    print("playing finished.")

class openstudioAudioChannel(Thread):

    def __init__(self, handle, app):
        Thread.__init__(self)
        self.handle = handle
        self.app = app

    def run(self):

        #BASS_ChannelSetSync(self.handle, BASS_SYNC_END, 0, onEndPlay, 0)
        BASS_ChannelPlay(self.handle, False)

        channel_length = BASS_ChannelGetLength(self.handle, BASS_POS_BYTE)
        channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)

        while channel_position < channel_length:
            channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)
            value = '%.2f' % BASS_ChannelBytes2Seconds(self.handle, channel_position)
            self.app.updateTiming(value)
            time.sleep(.02)

        BASS_Free()
        self.stop()
