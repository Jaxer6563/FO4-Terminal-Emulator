import clear, os
def createFile():
    while True:
        try:
            fileName = input('Enter Name of file: ')
            f = open(fileName+'.txt', 'x')
            print('File ' + fileName +'.txt created')
            break
        except FileExistsError:
            print('File exists already. Try a different name')
            
            
def editFile():
    done = False
    while True:
        try:
            fileName = input('Enter Name of file: ')
            f = open(fileName+'.txt', 'a')
            f.write(input('Enter text here:\n'))
            f.close
            break
        except:
            print('\nFile does not exist')
            
def deleteFile():
    while True:
        fileName = input('Enter Name of file: ')
        if os.path.exists(fileName+'.txt'):
            os.remove(fileName+'.txt')
            print(fileName+'.txt has been successfully deleted')
            break
        else:
            print('\nThe file does not exist')
def viewFile():
    while True:
        try:
            fileName = input('Enter Name of file: ')
            f = open(fileName+'.txt', 'r')
            print(f.readlines())
            f.close()
            break
        except:
            print('\nThe file does not exist')
   
def commands():
    while True:
        cmd = input()
        if cmd == '?':
            print('Here is a list of commands for the RobCo Industries (TM) TermLink System')
            print('\n? - This page of Documentation')
            print('\nls - See all files in the Current Working Directory')
            print('\ncd - Change the Current Working Directory')
            print('\ncd .. - Change the Current Working Directory to one level above the current Directory')
            print('\ncwd - See the Current Working Directory')
            print('\nmkdir - Create a new Directory')
            print('\nmkfile - Create a new File')
            print('\nrmvfile - Delete a file')
            print('\neditfile - Edit the contents of a file')
            print('\nreadfile - Read the contents of a file')
        elif cmd == 'ls':
            print('Current Working Directory: ' +os.getcwd())
            os.listdir()
        elif cmd == 'cd':
            pass
        elif cmd == 'cd ..':
            pass
        elif cmd == 'cwd':
            print(os.getcwd)
        elif cmd == 'mkdir':
            name=input('Enter name of new folder')
            os.mkdir(name)
        elif cmd == 'mkfile':
            createFile()
        elif cmd == 'rmvfile':
            deleteFile()
        elif cmd == 'editfile':
            editFile()
        elif cmd == 'readfile':
            viewFile()


clear.clear()

commands()
input()