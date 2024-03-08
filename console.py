#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from shlex import split


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass
    
    def do_create(self, line):
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"BaseModel.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"BaseModel.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        args = split(line)
        if args and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            print([str(obj) for key, obj in all_objs.items() if not args or key.startswith(args[0])])

    def do_update(self, line):
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"BaseModel.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                if args[2] not in ["id", "created_at", "updated_at"]:
                    setattr(all_objs[key], args[2], args[3])
                    all_objs[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()