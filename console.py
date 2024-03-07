#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    This file contains the entry point of the 
    command interpreter for our Airbnb project
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """This command exits the program"""
        return True


    def do_EOF(self, line):
        """Terminates the command console if EOF is encountered"""
        return True


    def emptyline(self):
        """If an empty line is encountered or ENTER: do nothing"""
        pass


    def help_EOF(self):
        """"Prints help for the EOF command"""
        print("EOF: Exits the command interpreter on Ctrl+D")
        print("\n")


    def help_quit(self):
        """Prints help for the quit command"""
        print('"quit command exits the program"')
        print("\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
