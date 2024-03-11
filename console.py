#!/usr/bin/python3

import cmd
import shlex
import models
from models.base_model import BaseModel


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

    
    def do_create(self, arg):
        """Creates new instance of class-BaseModel saves it, and prints the id"""
        new_arg = shlex.split(arg)
        
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__CLASSNAMES:
            print("** class doesn't exist **")
        else:
            print(eval(new_arg[0])().id)
            storage.save()
    
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        new_arg = shlex.split(arg)
        objdict = storage.all()

        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__CLASSNAMES:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id, saves it"""
        new_arg = shlex.split(arg)
        objdict = storage.all()

        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__CLASSNAMES:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(new_arg[0], new_arg[1])]
            storage.save()
            
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        new_arg = shlex.split(arg)

        if len(new_arg) > 0 and new_arg[0] not in HBNBCommand.__CLASSNAMES:
            print("** class doesn't exist **")
        else:
            new_obj = []
            for obj in storage.all().values():
                if len(new_arg) > 0 and new_arg[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
                elif len(new_arg) == 0:
                    new_obj.append(obj.__str__())
            print(new_obj)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute and saves it"""
        new_arg = shlex.split(arg)
        objdict = storage.all()

        if len(new_arg) == 0:
            print("** class name missing **")
            return False
        if new_arg[0] not in HBNBCommand.__CLASSNAMES:
            print("** class doesn't exist **")
            return False
        if len(new_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(new_arg[0], new_arg[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(new_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(new_arg) == 3:
            try:
                type(eval(new_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        
        if len(new_arg) == 4:
            obj = objdict["{}.{}".format(new_arg[0], new_arg[1])]
            if new_arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[k])
                obj.__dict__[new_arg[2]] = valtype(new_arg[3])
            else:
                obj.__dict__[new_arg[2]] = new_arg[3]
        elif type(eval(new_arg[2])) == dict:
            obj = objdict["{}.{}".format(new_arg[0], new_arg[1])]
            for k, v in eval(new_arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
