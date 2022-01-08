#  Copyright (C) 2021 Samrat Podder - All Rights Might be Reserved but I am not well versed in legal stuff
#  You may use, distribute and modify this code under the
#  terms of what Ethical Developers do, which unfortunately won't be
#  written because i dont know legal things.

#  You should not have any problem with reading the code but I you face any issue then,
#  please write to: samratpodder14@gmail.com / iamsamrat16@outlook.com, or visit : I dont have a Portfolio Website :(

import sys
import os

## Global Variables
currPath = os.getcwd()+"/"
numArgs = len(sys.argv)



## The following fragment handles the requested tasks with functions
#This Section contains all the functions

def printHelp():
    print("Usage :-\n$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n$ ./task del INDEX            # Delete the incomplete item with the given index\n$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n$ ./task help                 # Show usage\n$ ./task report               # Statistics")


def showItemsTobeDone():
    try:
        with open(currPath+"task.txt",'r') as taskF:
            #print(taskF.readlines())
            idx = 1
            for line in taskF.readlines():
                pr = (line.split(" ",1)[0])
                task = line.split(" ",1)[1][0:-1]
                print(str(idx)+". "+task+" ["+pr+"]")
                idx+=1
    except:
        print("There are no pending tasks!")



def showReport():
    idx = 1
    try:
        with open(currPath+"task.txt",'r') as taskF:
            lines = taskF.readlines()
            print("Pending : "+str(len(lines)))
            for line in lines:
                pr = (line.split(" ",1)[0])
                task = line.split(" ",1)[1][0:-1]
                print(str(idx)+". "+task+" ["+pr+"]")
                idx+=1
    except FileNotFoundError:
        print("Pending : 0")
    print()
    idx=1
    try:
        with open(currPath+"completed.txt",'r') as compF:
            lines = compF.readlines()
            print("Completed : "+str(len(lines)))
            for line in lines:
                task = line[0:-1]
                print(str(idx)+". "+task)
                idx+=1
    except FileNotFoundError:
        print("Completed : 0")


def delItem(index,signal):
    tasks = open(currPath+"task.txt","r")
    tasks.seek(0)
    taskList = tasks.readlines()
    print(taskList,len(taskList))
    if(int(index)>len(taskList) or int(index)<=0):
        if(signal==1):
            print("Error: task with index #"+ index+" does not exist. Nothing deleted.")
        elif(signal==0):
            print("Error: no incomplete item with index #"+index+" exists.")
    try:
        compTask = taskList.pop(int(index)-1)
    except:
        print("Error: task with index #"+index+" does not exist. Nothing deleted.")
        #If its not possible to pop items from list which happens for non-existent items then just dont pop and handle the exception.
        #I was actually unable to understand exactly what the problem was and would love to know more about it like what the test is passing 
        #because i handled the corner case of non-existing above still it has some issues.
    tasks.close()
    tasks = open(currPath+"task.txt","w")#Could have also used task.seek(0) to overwrite but this feels convinient to Code
    for line in taskList:
        tasks.write(line)
    tasks.close()
    if(signal==1):
        print("Deleted task #"+index)
    else:
        return compTask


def markasDone(index):
    compTask = delItem(index,0)
    compFile = open(currPath+"completed.txt","a")
    compFile.write(compTask[2:].strip()+"\n")
    compFile.close()
    print("Marked item as done.")


def addtoList(pr,item):
    with open(currPath+"task.txt","a") as tasks:
        tasks.write(str(pr)+" "+item+"\n")
    print("Added task: \""+item+"\" with priority "+pr)






#This Fragment helps with parsing the Command Line Arguments and calls the appropriate Functions to perform the requested task


if(numArgs==1):
    printHelp()
elif(numArgs==2):
    if(sys.argv[1]=="help"):
        printHelp()
    elif(sys.argv[1]=="ls"):
        showItemsTobeDone()
    elif(sys.argv[1]=="report"):
        showReport()
    elif(sys.argv[1]=="add"):
        print("Error: Missing tasks string. Nothing added!")
    elif(sys.argv[1]=="done"):
        print("Error: Missing NUMBER for marking tasks as done.")
    elif(sys.argv[1]=="del"):
        print("Error: Missing NUMBER for deleting tasks.")
    else:
        printHelp()
elif(numArgs==3):
    if(sys.argv[1]=="del"):
        delItem(sys.argv[2],1)
    elif(sys.argv[1]=="done"):
        markasDone(sys.argv[2])
    elif(sys.argv[1]=="add"):
        print("Error: Missing tasks string. Nothing added!")
    else:
        printHelp()
else:
    if(sys.argv[1]=="add"):
        addtoList(sys.argv[2],sys.argv[3])
    else:
        printHelp()
