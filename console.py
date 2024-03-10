#!/usr/bin/python3
"""
The Console Module
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """command interpreter class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        """
        return True

    def help_quit(self):
        """
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
