import clear, os, shutil
def createFile(fileName):
    while True:
        try:
            f = open(fileName, 'x')
            print('File ' + fileName +' created')
            break
        except FileExistsError:
            print('File exists already. Try a different name')
            break
            
            
def editFile(fileName):
    while True:
        try:
            f = open(fileName, 'a')
            f.write(input('Enter text here:\n')+'\n')
            f.close
            break
        except:
            print('\nFile does not exist')
            break
            
def deleteFile(fileName):
    while True:
        if os.path.exists(fileName):
            os.remove(fileName)
            print(fileName+' has been successfully deleted')
            break
        else:
            print('\nThe file does not exist')
            break
def viewFile(fileName):
    while True:
        try:
            f = open(fileName, 'r')
            print(f.readlines())
            f.close()
            break
        except:
            print('\nThe file does not exist')
            break

def commands():
    while True:
        #global rawcmd
        rawcmd = input('> ').split()
        cmd = rawcmd[0]
        #print (rawcmd)
        #print (cmd)
        
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
            print('\nrmvtree - Delete a folder')
            print('\nexit - Exits the terminal')
        elif cmd == 'ls':
            print('Current Working Directory: ' +os.getcwd())
            delimiter = '\n'
            files = delimiter.join(os.listdir())
            print(files)
        elif cmd == 'cd':
            path = os.path.abspath(rawcmd[1])
            os.chdir(path)          
        elif cmd == 'cwd':
            print(os.getcwd())
        elif cmd == 'mkdir':
            name=rawcmd[1]
            os.mkdir(name)
        elif cmd == 'mkfile':
            name = rawcmd[1]
            createFile(name)
        elif cmd == 'rmvfile':
            name = rawcmd[1]
            deleteFile(name)
        elif cmd == 'editfile':
            name = rawcmd[1]
            editFile(name)
        elif cmd == 'readfile':
            name = rawcmd[1]
            viewFile(name)
        elif cmd == 'rmvtree':
            name = rawcmd[1]
            shutil.rmtree(name)
        elif cmd == 'exit':
            exit()

clear.clear()

commands()
input()