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
        newObj = assignCls(arg)
        if newObj is None:
            return
        newObj.save()
        print(newObj.id)

    def help_create(self):
        """ create help """
        print("Create an instance of a class")
        print("Usage: create <class name>\n")

    def do_show(self, arg):
        """ prints string of an instance """
        name = condChk(arg)
        if name is None:
            return
        with open('file.json', 'r') as f:
            objDict = json.load(f)
        if name not in objDict:
            print("** no instance found **")
            return
        kwarg = objDict[name]
        print(BaseModel(**kwarg))

    def help_show(self):
        """ show help """
        pass

    def do_destroy(self, arg):
        """ remove obj from JSON File """
        name = condChk(arg)
        if name is None:
            return
        with open('file.json', 'r') as f:
            objDict = json.load(f)
        if name not in objDict:
            print("** no instance found **")
            return
        objDict.pop(name)
        with open('file.json', 'w') as f:
            objDict = json.dump(objDict, f, sort_keys=True, indent=4)

    def help_destroy(self):
        """ help destroy """
        pass

    def do_all(self, arg):
        """ show all objects """
        clsList = [
            'User', 'State', 'City',
            'Amenity', 'Place',
            'Review', 'BaseModel'
        ]
        if arg not in clsList:
            print("** class doesn't exist **")
            return
        allList = []
        with open('file.json', 'r') as f:
            objDict = json.load(f)
        for key in objDict:
            obj = BaseModel(objDict[key])
            allList.append(str(obj))
            del(obj)
        print(allList)

    def help_all(self):
        """ show help """
        pass

    def do_update(self, arg):
        """ updates an object """
        name = condChk(arg)
        if name is None:
            return
        with open('file.json', 'r') as f:
            objDict = json.load(f)
        if name not in objDict:
            print("** no instance found **")
            return
        updateObj = arg.split(" ")
        length = len(updateObj)
        if length < 3:
            print("** attribute name missing **")
            return
        if length < 4:
            print("** value missing **")
            return
        attributeName = updateObj[2]
        print("\t{}!!!!!".format(updateObj[3]))
        updateObj.pop(2)
        updateObj.pop(1)
        updateObj.pop(0)
        value = ' '.join(updateObj).replace('"', '')
        print("\t{}!!!!!".format(value))
        newObj = BaseModel(**objDict[name])
        """ to do """
        setattr(newObj, attributeName, value)
        newObj.save()
        del newObj

    def help_update(self):
        """ update help """
        pass


def assignCls(arg):
    """assigning class obj """
    if not arg:
        print("** class name missing **")
        return None
    clsList = [
        'User', 'State', 'City',
        'Amenity', 'Place',
        'Review', 'BaseModel'
    ]
    if arg == 'User':
        return None
    if arg == 'State':
        return None
    if arg == 'City':
        return None
    if arg == 'Amenity':
        return None
    if arg == 'Place':
        return None
    if arg == 'Review':
        return None
    if arg == 'BaseModel':
        return BaseModel()
    if arg not in clsList:
        print("** class doesn't exist **")
        return None


def condChk(arg):
    """ checking on conditionals for obj """
    clsList = [
        'User', 'State', 'City',
        'Amenity', 'Place',
        'Review', 'BaseModel'
    ]
    argList = arg.split(" ")
    length = len(argList)
    if argList == [""]:
        print("** class name missing **")
        return None
    if argList[0] not in clsList:
        print("** class doesn't exist **")
        return None
    if length < 2:
        print("** instance id missing **")
        return None
    return argList[0] + "." + argList[1]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
