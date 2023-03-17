import os
import pprint
import importlib as il
from time import sleep
from tkinter import *

def menu():
    while True:
        print(''' Select the Operation from following list \n
            1. To Insert new Student Record \n
            2. To Update the Details of Existing Student\n
            3. To Delete the Student Details \n
            4. To Display all the Information of the Student \n
            5. To Exit from the Application \n\n
            Enter the Choice : ''')
        ch = int(input())
        match ch:
            case 1:
                insert()
            case 2:
                pass
                update()
            case 3:
                delete()
            case 4:
                print('''\n\t1. Only Details
                2. Only IA
                3. Only EA
                4. All
                Enter the choice: ''')
                inp = int(input())
                print('Enter the USN to Display the Details ')
                usn = input()
                usn += '.py'
                if os.path.isfile(usn):
                    display(inp, usn)
                else:
                    print(usn, " Does not Exists")
            case 5:
                exit(0)
            case default:
                print(" Invalid Input ")


def insert():
    name = str(input(" Enter the Name of Student: "))
    usn = str(input(" Enter the USN "))
    fname = usn + '.py'
    os.chdir(os.getcwd())
    bol = os.path.isfile(os.getcwd() + '\\' + fname)
    if bol:
        print('\n\nDetails of ', name, ' already Exists !!!!\n Try using the Update Option!!')
        sleep(1)
        return
    else:
        f = open(str(fname), 'w')
    Details = {'name': name, 'usn': usn, 'phno': input("Enter the Mobile Number "),
               'email': input("Enter the E-Mail ID "), 'gen': input("Enter the Gender "),
               'sem': int(input("Enter the Current sem  ")), 'course': input("Enter the Current Course ")}
    f.write('Details = ' + pprint.pformat(Details) + '\n')
    print(" Enter the Academic Score of ", name)
    EA = {}
    if Details['sem'] > 1:
        sem1 = Details['sem']
        sem2 = 1
        while sem2 != sem1:
            print(" Enter the SGPA of ", name, ' in ', sem2)
            EA[sem2] = float(input())
            sem2 += 1
    f.write('EA= ' + pprint.pformat(EA) + '\n')
    temp = int(input('Enter 1 if internals are conducted , else enter 0: '))
    sem2 = 1
    IA = {}
    if temp:
        n = int(input('Enter the Number of Subjects : '))
        for i in range(1, n + 1):
            code = input(" Enter the Subject code : ")
            print(" Enter the marks obtained in ", code)
            m = int(input())
            IA[code] = m
    f.write('IA =' + pprint.pformat(IA) + '\n')

def delete():
    print('Enter the USN to delete the Details ')
    usn = input()
    usn += '.py'
    if os.path.isfile(usn):
        os.unlink(usn)
        print("\n\nDeleted successfully \n\n")
    else:
        print(usn, " Doesn't Exists ")


def update():
    print('Enter the USN to Update the Details ')
    usn = input()
    usn += '.py'
    if os.path.isfile(usn):
        usn1 = usn
        while True:
            print('''\n\nWhat do you want to modify :\n
                1.Details
                2.IA marks 
                3.EA marks''')
            inp = int(input('Enter 5 to save and exit else enter choice from above menu : '))
            usn = il.import_module(usn1[:-3], package=None)
            match inp:
                case 1:
                    print("\n \t Existing Details are : ")
                    display(1, usn1)
                    temp = input('Enter the key name to update ')
                    if temp == 'sem':
                        temp = int(temp)
                        usn.Details[temp] = int(input('Enter the new Value :  '))
                    else:
                        usn.Details[temp] = input('Enter the new Value :  ')
                case 2:
                    print("\n \t Existing IA Marks are : ")
                    display(2, usn1)
                    temp = input('Enter the Subject Code : ')
                    usn.IA[temp] = int(input('Enter the Marks  :  '))
                case 3:
                    print("\n \t Existing EA Marks are : ")
                    display(3, usn1)
                    temp = int(input('Enter the Sem number : '))
                    usn.EA[temp] = float(input('Enter the SGPA : '))
                case 4:
                    pass
                case 5:
                    D = usn.Details
                    iamarks = usn.IA
                    eamarks = usn.EA
                    upfile = open(usn1, 'w')
                    upfile.write('Details = ' + pprint.pformat(D) + '\n')
                    upfile.write('IA = ' + pprint.pformat(iamarks) + '\n')
                    upfile.write('EA = ' + pprint.pformat(eamarks) + '\n')
                    return
    else:
        print(usn, " Doesn't Exists ")
    
def display(ch, usn):
    if os.path.isfile(usn):
        usn = il.import_module(usn[:-3],package=None)
        match ch:
            case 1:
                print('\n\n Student Details :\n')
                disp(usn.Details)
            case 2:
                print('\n\n Student IA Marks :\n')
                disp(usn.IA)
            case 3:
                print('\n\n Student EA Marks :\n')
                disp(usn.EA)
            case 4:
                print('\n\n Student Details :\n')
                disp(usn.Details)
                print('\n\n Student IA Marks :\n')
                disp(usn.IA)
                print('\n\n Student EA Marks :\n')
                disp(usn.EA)
    else:
        print(usn, " Doesn't Exists ")

def disp(dict):
    win = Tk()
    win.geometry("500x400")
    text = Text(win, width=50, height=30)
    if dict is None:
        print("\n\nIts Empty \n")
    else:
        for k, v in dict.items():
            text.insert(END, '\n'+str(k)+' : '+str(v)+'\n')
    text.pack()
    win.mainloop()

menu()