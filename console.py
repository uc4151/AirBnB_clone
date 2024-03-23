#!/usr/bin/python3

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This file contains the entry point of the 
    command interpreter for our Airbnb project
    """
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]


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

    
    def do_create(self, line):
        """Creates new instance of class-BaseModel saves it, and prints the id"""
        new_arg = shlex.split(line)
        
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_item = eval(f"{new_arg[0]}()")
            new_item.save()
            print(new_item.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        new_arg = shlex.split(line)

        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()

            key = "{}.{}".format(new_arg[0], new_arg[1])
            if key in store:
                print(store[key])
            else:
                print("** no instance found **")


    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id, saves it"""
        new_arg = shlex.split(line)

        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()
            
            key = "{}.{}".format(new_arg[0], new_arg[1])
            if key in store:
                del store[key]
                storage.save()
            else:
                print("** no instance found **")
            
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        store = storage.all()
        store_list = []

        new_arg = shlex.split(line)
        if len(new_arg) == 0:
            for v in store.values():
                store_list.append(v.__str__())
        elif new_arg[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            for v in store.values():
                if len(new_arg) > 0 and new_arg[0] == v.__class__.__name__:
                    store_list.append(v.__str__())

        print(store_list)



    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute and saves it"""
        new_arg = shlex.split(line)

        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()

            key = "{}.{}".format(new_arg[0], new_arg[1])
            if key not in store:
                 print("** no instance found **")
            elif len(new_arg) == 2:
                print("** attribute name missing **")
            elif len(new_arg) == 3:
                print("** value missing **")
            else:
                item = store[key]

                attribute_name = new_arg[2]
                attribute_value = new_arg[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(item, attribute_name, attribute_value)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
