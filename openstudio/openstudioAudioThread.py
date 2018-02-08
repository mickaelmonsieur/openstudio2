# -*- coding: utf-8 -*-

from pybass import *
import threading
import time

#@SYNCPROC
#def onEndPlay(handle, buffer, length, user):
#    print("playing finished.")

class openstudioAudioChannel(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.Terminated = False

    def run(self):

        self.handle = BASS_StreamCreateFile(False, self.path, 0, 0, 0)

        #BASS_ChannelSetSync(self.handle, BASS_SYNC_END, 0, onEndPlay, 0)
        if not BASS_ChannelPlay(self.handle, False):
            print get_error_description(BASS_ErrorGetCode())

        print threading.current_thread()
        channel_length = BASS_ChannelGetLength(self.handle, BASS_POS_BYTE)
        channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)

        while channel_position < channel_length:
            if not self.Terminated:
                channel_position = BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE)
                #value = '%.2f' % BASS_ChannelBytes2Seconds(self.handle, channel_position)
                self.app.updatePosition(BASS_ChannelBytes2Seconds(self.handle, channel_position))
                self.app.updateCountdown(BASS_ChannelBytes2Seconds(self.handle, channel_length-channel_position))
                time.sleep(.2)
            else:
                BASS_ChannelStop(self.handle)
                BASS_StreamFree(self.handle)
        print("Process run stop")

    def stop(self):
        print("Terminating...")
        self.Terminated = True
