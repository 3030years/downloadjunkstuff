from scratchclient import ScratchSession
from time import sleep
import os
x = 1
letterdecode = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8",
                "9", "0", "_", " "]


def PasswordDecode(Password):
    NUMBER = 1
    global Password_maker
    Password_maker = ""
    for i in Password:
        letter = (letterdecode.index(i) + NUMBER) % len(letterdecode)
        Password_maker = "%s%s" % (Password_maker,
                                   letterdecode[letter + NUMBER])
    return Password_maker


Session = ScratchSession(input("User name: "), input("Password: "))
connection = Session.create_cloud_connection(input("Project id: "))
os.system("cls")
while True:
    x = x + 1
    connection.set_cloud_variable("Clock", x)
    sleep(1)
