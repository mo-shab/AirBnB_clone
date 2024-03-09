#!/usr/bin/python3
"""
The Console Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered
        """
        pass

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
