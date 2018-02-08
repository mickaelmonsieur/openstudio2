# -*- coding: utf-8 -*-

import sys
import wx
import openstudioAudio
import openstudioGUI
import sqlite3 as lite

#inherit from the MainFrame created in wxFowmBuilder and create MainFrame
class MainFrame(openstudioGUI.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        print (sys.version)
        openstudioGUI.MainFrame.__init__(self,parent)
        self.audioWrapper_1 = openstudioAudio.openstudioAudioInstance(self)
        self.con = lite.connect('openstudio.db')
        self.songsColumn1 = self.songs.AppendTextColumn( u"ID", 0, width=50 )
        self.songsColumn2 = self.songs.AppendTextColumn( u"Artist", 1, width=400 )
        self.songsColumn3 = self.songs.AppendTextColumn( u"Title", 2, width=400 )
        self.songsColumn4 = self.songs.AppendTextColumn( u"Duration", 3, width=50 )
        self.getSongs()

    def play(self,event):
        self.playSong1.Disable()
        self.audioWrapper_1.playAudio()

    def stop(self,event):
        self.audioWrapper_1.stopAudio()
        self.playSong1.Enable()

    def rewind(self,event):
        self.audioWrapper_1.rewindAudio()

    def close(self,event):
        sys.exit(0)

    def updatePosition(self,position):
        m, s = divmod(position, 60)
        h, m = divmod(m, 60)
        self.position.SetLabel("%02d:%02d:%02d" % (h, m, s))

    def updateCountdown(self,countdown):
        m, s = divmod(countdown, 60)
        h, m = divmod(m, 60)
        self.countdown.SetLabel("%02d:%02d:%02d" % (h, m, s))

    def getPath(self):
        currentId = self.songs.GetValue(self.songs.GetSelectedRow(), 0)
        cur = self.con.cursor()
        cur.execute('SELECT filename FROM song WHERE songId=?', currentId)
        return cur.fetchone()[0]

    def getSongs(self):

        with self.con:

            cur = self.con.cursor()
            cur.execute("SELECT songId, name, title, duration FROM song INNER JOIN artist on artist.artistId=song.artistId")

            while True:

                row = cur.fetchone()

                if row == None:
                    break

                self.songs.AppendItem( [str(row[0]),row[1],row[2],str(row[3]) ])

#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)

#create an object of MainFrame
frame = MainFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
