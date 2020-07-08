# 0x00 - AirBnB_clone

[Holberton School Partner Proramming](https://github.com/Jilroge7/AirBnB_clone.git)

## This repo contains the group project "AirBnB clone" for Holberton School.

### Instructions on how to operate console

The console is a command line interpreter that takes options and arguments from the command line, parses the input, and then directs the input to it's called command to interpret back to standard output.

1. To begin the console, enter ./console.py into the command line.
2. A prompt will appear. Here you can type 'help' to see a list of all available commands.
3. EOF (^C) and 'quit' will exit the console.
4. 'create' plus a class name will create a new instance of a class. Class options are BaseModel, Place, City, State, User, Amenity, and Review. If successful, the program will return a string representation of the instance along with the newly created id. ex. 'create BaseModel'
5. 'show' plus a class name will print a string representation of the class name and id. ex 'show BaseModel'
6. 'destroy' plus the class name and id number, will delete the class instance. ex. 'destroy BaseModel 1234 1234'
7. 'all' with no arguments prints a list of all instances of any class. 'all' with a class name will print only instances of that class. ex 'all BaseModel'
8. 'update' plus an instance id, along with an attribute and value (either creating or updating) will update or create an attribute with the assigned value to the instance. ex. 'update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"'

Command line example:
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
