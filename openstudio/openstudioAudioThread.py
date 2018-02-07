# -*- coding: utf-8 -*-

from pybass import *
from threading import Thread
import time
#import openstudioGUI

@SYNCPROC
def onEndPlay(handle, buffer, length, user):
    print("playing finished.")

class openstudioAudioChannel(Thread):

    def __init__(self, handle):
        Thread.__init__(self)
        self.handle = handle

    def run(self):

        BASS_ChannelSetSync(self.handle, BASS_SYNC_END, 0, onEndPlay, 0)
        BASS_ChannelPlay(self.handle, False)

        channel_length = BASS_ChannelGetLength(self.handle, BASS_POS_BYTE)
        channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)

        while channel_position < channel_length:
            channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)
            value = 'Play second %s of song' % str(int(BASS_ChannelBytes2Seconds(self.handle, channel_position)))
            #openstudio = openstudioGUI.MainFrame(None)
            #openstudio.position.SetLabel('test')
            sys.stdout.write('%s\r' % value.ljust(20))

            sys.stdout.flush()
            time.sleep(1)

        BASS_Free()
