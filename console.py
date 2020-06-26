#!/usr/bin/python3
""" main program executable """

import cmd
import json
from models.base_model import BaseModel
import models.base_model


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Close """
        exit()

    def help_quit(self):
        """ quit help """
        print("Quit command to exit program\n")

    def do_EOF(self, arg):
        """ close """
        exit()

    def help_EOF(self):
        """ eof help """
        print("Quit command to exit program\n")

    def do_create(self, arg):
        """ create new instance """
        pass

    def help_create(self):
        """ create help """
        print("Cerate an instance of a class")
        print("Usage: create <class name>\n")

    def do_show(self, arg):
        """ prints string of an instance """
        pass

    def help_show(self):
        """ show help """
        pass

    def do_destroy(self, arg):
        """ remove obj from JSON File """
        pass

    def help_destroy(self):
        """ help destroy """
        pass

    def do_all(self, arg):
        """ show all objects """
        pass

    def help_all(self):
        """ show help """
        pass

    def do_update(self, arg):
        """ updates an object """
        pass

    def help_update(self):
        """ update help """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
