import tkinter

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

class MusicPlayer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("600x600")
        self.var = tkr.StringVar()
        self.songs = self.browse()
        self.playlist = tkr.Listbox(self,font="Helvetica 12 bold",bg="white",fg="black",selectmode="single")
        for song in self.songs:
            pos = 0
            self.playlist.insert(pos, song)
            pos = pos + 1

        pygame.init()
        pygame.mixer.init()
        songTitle = tkr.Label(self,font="Helvetica 12 bold",fg="black",textvariable = self.var)
        self.visual(songTitle)
        self.mainloop()


    def visual(self,songTitle):
        playButt=tkr.Button(self,width=5,height=3,font="Helvetica 12 bold",text="Play",bg="gray",fg="black",command=self.play)
        stopButt=tkr.Button(self,width=5,height=3,font="Helvetica 12 bold",text="Stop",bg="red",fg="black",command=self.stop)
        pauseButt=tkr.Button(self,width=5,height=3,font="Helvetica 12 bold",text="Pause",bg="yellow",fg="black",command=self.pause)
        unpauseButt=tkr.Button(self,width=5,height=3,font="Helvetica 12 bold",text="Unpause",bg="green",fg="black",command=self.unpause)
        songTitle.pack()
        playButt.pack(fill="x")
        stopButt.pack(fill="x")
        pauseButt.pack(fill="x")
        unpauseButt.pack(fill="x")
        self.playlist.pack(fill="both",expand="yes")

    def browse(self):
        directory = askdirectory()
        os.chdir(directory)
        return os.listdir()

    def play(self):
        pygame.mixer.music.load(self.playlist.get(tkr.ACTIVE))
        self.var.set(self.playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()
    def stop(self):
        pygame.mixer.music.stop()
    def pause(self):
        pygame.mixer.music.pause()
    def unpause(self):
        pygame.mixer.music.unpause()
    def next(self):
        pass
    def prev(self):
        pass

MusicPlayer()