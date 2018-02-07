# -*- coding: utf-8 -*-

import sys
import wx
import openstudioAudio
import openstudioGUI

#inherit from the MainFrame created in wxFowmBuilder and create MainFrame
class MainFrame(openstudioGUI.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        openstudioGUI.MainFrame.__init__(self,parent)
        self.audioWrapper_1 = openstudioAudio.openstudioAudioInstance()

    def play(self,event):
        self.audioWrapper_1.playAudio()

    def stop(self,event):
        self.audioWrapper_1.stopAudio()

    def close(self,event):
        sys.exit(0)

#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)

#create an object of MainFrame
frame = MainFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
