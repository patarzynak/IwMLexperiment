#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')

import gtk
import time

class Application():
    
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Example GTK Application")

        self.start = time.time()
        self.folder = "./new/"
        self.samples = ["title.JPG", "1.JPG", "2.JPG", "3.JPG", "4.JPG", "5.JPG", "6.JPG", "7.JPG", "8.JPG", "9.JPG", "10.JPG", "11.JPG", "12.JPG", "13.JPG", "14.JPG", "15.JPG", "16.JPG", "17.JPG", "18.JPG", "19.JPG", "20.JPG"]
        self.track = 0
        self.create_widgets()
        self.connect_signals()
        
        self.window.show_all()
        gtk.main()
    
    
    def create_widgets(self):
        self.vbox = gtk.VBox(spacing=10)

        

        self.hbox_1 = gtk.HBox(spacing=10)
        #post image
        self.image = gtk.Image()
        self.image.set_from_file(self.folder+self.samples[0])
        self.image.show()
        self.legend = gtk.Image()
        self.legend.set_from_file("./new/legend.JPG")
        self.legend.show()
        self.hbox_1.pack_start(self.image)
        self.hbox_1.pack_start(self.legend)
        
        self.hbox_2 = gtk.HBox(spacing=10)
        self.button_next = gtk.Button("Next")
        self.hbox_2.pack_start(self.button_next)

        self.button_exit = gtk.Button("Exit")
        #self.hbox_2.pack_start(self.button_exit)
        
        self.vbox.pack_start(self.hbox_1)
        self.vbox.pack_start(self.hbox_2)
        
        self.window.add(self.vbox)
    
    
    def connect_signals(self):
        self.button_next.connect("clicked", self.callback_next)
        self.button_exit.connect("clicked", self.callback_exit)
    
    
    def callback_ok(self, widget, callback_data=None):
        name = self.entry.get_text()
        print name


    def callback_next(self, widget, callback_data=None):
    	end = time.time()
    	print(end - self.start)
    	if self.track < len(self.samples)-1:
    		self.track += 1
    		self.image.set_from_file(self.folder+self.samples[self.track])
    	else:
    		gtk.main_quit()

    	self.start = time.time()
    
    def callback_exit(self, widget, callback_data=None):
        gtk.main_quit()
    

if __name__ == "__main__":
    app = Application()