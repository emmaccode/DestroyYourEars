#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2020 Emmett Boudreau <emmett@emmett-kabylake>
# 
# pygtk-foobar is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys
UI_FILE = "gtkui.ui"
#UI_FILE = "/usr/local/share/pygtk_foobar/ui/pygtk_foobar.ui"
import winsound

class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')


		window.show_all()

	def on_window_destroy(self, window):
		Gtk.main_quit()
	def play_sound(self):
		dur = self.builder.get_object("durbox")
		freq = self.build.get_object("freqbox")
		winsound.Beep(freq, dur)
def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())

