#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import gtk
import pygame

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbutton import ToolButton
from sugar.activity.widgets import StopButton

from gettext import gettext as _

import sugargame.canvas

import Jump

class JumpActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.sound_enable = True

        self.game = Jump.SolitaireMain()
        self.build_toolbar()
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()

        self._pygamecanvas.run_pygame(self.game.SuperLooper)

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        separator1 = gtk.SeparatorToolItem()
        separator1.props.draw = True
        separator1.set_expand(False)
        toolbar_box.toolbar.insert(separator1, -1)
        separator1.show()

        item1 = gtk.ToolItem()
        label1 = gtk.Label()
        label1.set_text(_('Levels') + ' ')
        item1.add(label1)
        toolbar_box.toolbar.insert(item1, -1)

        item2 = gtk.ToolItem()

        levels = (_('Cross'),
            _('Cross 2'),
            #TRANS:'chimney' - the place where you make fire
            _('Hearth'),
            _('Arrow'),
            _('Pyramid'),
            _('Diamond'),
            _('Solitaire'))
        combo = Combo(levels)
        item2.add(combo)
        combo.connect('changed', self.change_combo)
        toolbar_box.toolbar.insert(item2, -1)

        separator2 = gtk.SeparatorToolItem()
        separator2.props.draw = True
        separator2.set_expand(False)
        toolbar_box.toolbar.insert(separator2, -1)
        separator2.show()

        sound_button = ToolButton('speaker-100')
        sound_button.set_tooltip(_('Sound'))
        sound_button.connect('clicked', self.sound_control)
        toolbar_box.toolbar.insert(sound_button, -1)

        separator3 = gtk.SeparatorToolItem()
        separator3.props.draw = False
        separator3.set_expand(True)
        toolbar_box.toolbar.insert(separator3, -1)
        separator3.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()


        self.show_all()

    def change_combo(self, combo):
        level = combo.get_active()
        self.game.change_level(level)

    def sound_control(self, button):
        self.sound_enable = not self.sound_enable
        self.game.change_sound(self.sound_enable)
        if not self.sound_enable:
            button.set_icon('speaker-000')
            button.set_tooltip(_('No sound'))
        else:
            button.set_icon('speaker-100')
            button.set_tooltip(_('Sound'))

    def read_file(self, file_path):
        pass

    def write_file(self, file_path):
        pass


class Combo(gtk.ComboBox):

    def __init__(self, options):

        self.liststore = gtk.ListStore(str)

        for o in options:
            self.liststore.append([o])

        gtk.ComboBox.__init__(self, self.liststore)

        cell = gtk.CellRendererText()
        self.pack_start(cell, True)
        self.add_attribute(cell, 'text', 0)

        self.set_active(0)

