# -*- coding: utf-8 -*-

import sys
import wx
import openstudioAudio
import openstudioGUI
import sqlite3 as lite
from mutagen.mp3 import MP3

#inherit from the MainFrame created in wxFowmBuilder and create MainFrame
class MainFrame(openstudioGUI.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        openstudioGUI.MainFrame.__init__(self,parent)
        print (sys.version)
        self.audioWrapper_1 = openstudioAudio.openstudioAudioInstance(self)
        self.con = lite.connect('openstudio.db')
        self.songsColumn1 = self.songs.AppendTextColumn( u"ID", 0, width=70 )
        self.songsColumn2 = self.songs.AppendTextColumn( u"Artist", 1, width=400 )
        self.songsColumn3 = self.songs.AppendTextColumn( u"Title", 2, width=400 )
        self.songsColumn4 = self.songs.AppendTextColumn( u"Duration", 3, width=70 )
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
        cur.execute('SELECT filename FROM song WHERE songId=?', (currentId,))
        return cur.fetchone()[0]

    def getSongs(self):

        with self.con:

            cur = self.con.cursor()
            cur.execute("SELECT songId, name, title, duration FROM song INNER JOIN artist on artist.artistId=song.artistId")

            while True:

                row = cur.fetchone()

                if row == None:
                    break
                m, s = divmod(int(row[3]), 60)
                h, m = divmod(m, 60)
                self.songs.AppendItem( [str(row[0]),row[1],row[2],"%02d:%02d:%02d" % (h, m, s) ])

    def importFile(self,event):
        frame = ImportFrame(None)
        frame.Show(True)

    def refresh(self,event):
        self.songs.DeleteAllItems()
        self.getSongs()

class ImportFrame(openstudioGUI.ImportFrame):

    def __init__(self,parent):
        openstudioGUI.ImportFrame.__init__(self,parent)
        self.con = lite.connect('openstudio.db')
        self.con.text_factory = str

    def importFile(self,event):
        if self.filePicker.GetPath():
            audio = MP3(self.filePicker.GetPath())

            if "TPE1" in audio and "TIT2" in audio:
                artist = str(audio["TPE1"])
                title = str(audio["TIT2"])
                cur = self.con.cursor()
                artistId=self.getArtistId(artist)

                if not artistId:
                    print artist
                    print type(artist)
                    cur.execute("""INSERT INTO artist(name) VALUES(?)""", (artist,))
                    artistId = cur.lastrowid
                    print('Artist created with Id: %d' % artistId)
                else:
                    print('Artist exists with Id: %d' % artistId)

                cur.execute("""INSERT INTO song(artistId,title,duration,filename) VALUES(?, ?, ?, ?)""", (artistId, title, "%.2f" % audio.info.length, self.filePicker.GetPath()))
                id = cur.lastrowid
                if id:
                    print('Song created with Id: %d' % id)
                    self.Info('Song created with Id: %d' % id)
                    self.con.commit()
                else:
                    self.Warn("Unknown error.")
            else:
                print "Artist or title error. Check ID2 tags."
                self.Warn("Artist or title error. Check ID2 tags.")
        else:
            print "No file selected!"

    def Warn(parent, message, caption = 'Error!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()

    def Info(parent, message, caption = 'OpenStudio 2'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def getArtistId(self, name):
        cur = self.con.cursor()
        cur.execute('SELECT artistId FROM artist WHERE name=?', (name,))
        artistId = cur.fetchone()
        artistId = artistId and artistId[0] or False
        return artistId


#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)

#create an object of MainFrame
frame = MainFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
