# -*- coding: utf-8 -*-

from pybass import *
#import time

@SYNCPROC
def onEndPlay(handle, buffer, length, user):
    print("playing finished.")

def main():
    BASS_Init(-1, 44100, 0, 0, 0)
    handle = BASS_StreamCreateFile(False, b"test.mp3", 0, 0, 0)
    BASS_ChannelSetSync(handle, BASS_SYNC_END, 0, onEndPlay, 0)
    play_handle(handle, show_tags=False)
    #BASS_ChannelPlay(handle, False)
    #time.sleep(20)
    BASS_Free()

if __name__ == "__main__":
    main()
