from app.main_operations import *

while True:
    # OPERATION CHOICE
    choiceOfOperation = input('summer> ')

    # OPERATION EXECUTION
    if choiceOfOperation=="":
        MainOperations.doNothing()
    elif choiceOfOperation=="help":
        MainOperations.help()
    elif choiceOfOperation=="init":
        MainOperations.init()
    elif choiceOfOperation=="update":
        MainOperations.update()
    elif choiceOfOperation=="exit":
        MainOperations.exit()
    else:
        print("Unknown option, type help to show all avaible commands.")