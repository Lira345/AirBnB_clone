#!/usr/bin/python3
""" The Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This programme Contains the workings of the HolbertonBNB console"""

    # It finds the prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Writes/prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Revise the command line for advanced command syntax formatting.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Optional fields are indicated by brackets Example of usage.)
        """
        _cmd = _cls = _id = _args = ''  # initializes the line elements

        # search for general formatting - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse the line from left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and confirm <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if there are arguments within parentheses, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline converts to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # potential bug detected:
                # empty quotes are recorded as empty _id when replaced

                # if arguments extend beyond _id
                pline = pline[2].strip()  # pline has been converted to str
                if pline:
                    # checks for *args or **kwargs
                    if pline[0] is '{' and pline[-1] is'}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints when isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Exit method for the HolbertonBNB console"""
        exit()

    def help_quit(self):
        """ Display the help documentation for quit  """
        print("Terminate the program with formatting\n")

    def do_EOF(self, arg):
        """ Manages EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Display the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method in CMD """
        pass

    def do_create(self, args):
        """ Instantiate an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Retrieve help information for the create method """
        print("Instantiate a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Implement a method to display individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # protect againt trailing arguments
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Retrieve help information for the show command """
        print("Displays an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Retrieve help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Displays all objects or objects of a specific class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing arguments
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for m, m in storage._FileStorage__objects.items():
                if m.split('.')[0] == args:
                    print_list.append(str(n))
        else:
            for m, n in storage._FileStorage__objects.items():
                print_list.append(str(n))

        print(print_list)

    def help_all(self):
        """ Retrieve help info for the all commands """
        print("Displays all objects or objects of specific class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count the current number of class instances"""
        count = 0
        for m, n in storage._FileStorage__objects.items():
            if args == m.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a specific object with new information """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolates cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not here
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # invalid class name
            print("** class doesn't exist **")
            return

        # isolates id from arguments
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not here
            print("** instance id missing **")
            return

        # generate key based on class and id
        key = c_name + "." + c_id

        # determine the presence of a key
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # revise kwargs into list, ex: [<name>, <value>, ...]
            for m, n in kwargs.items():
                args.append(m)
                args.append(n)
        else:  # isolate arguments
            args = args[2]
            if args and args[0] is '\"':  # check for quoted argumemt
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted argument
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # check for quoted val argument
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dict of all current objects
        new_dict = storage.all()[key]

        # iterate through attribute names and values
        for i, att_name in enumerate(args):
            # execute the block on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # the following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update the dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save the updates on file

    def help_update(self):
        """ Retrieve help info for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
