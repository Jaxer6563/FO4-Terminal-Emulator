import os, shutil, typing

def createFile(fileName):
    while True:
        try:
            f = open(fileName, 'x')
            typing.typingPrint('File ' + fileName +' created\n')
            break
        except FileExistsError:
            typing.typingPrint('File exists already. Try a different name\n')
            break
            
            
def editFile(fileName):
    '''
    while True:
        try:
            f = open(fileName, 'a')
            f.write(typing.typingInput('Enter text here:\n')+'\n')
            f.close()
            break
        except:
            typing.typingPrint('\nFile does not exist')
            break
    '''
    while True:
        with open(fileName, 'a') as f:
            try:
                typing.typingPrint(f.read())
                f.write(typing.typingInput('\n_')+'\n')
            except KeyboardInterrupt:
                break
def deleteFile(fileName):
    while True:
        if os.path.exists(fileName):
            os.remove(fileName)
            typing.typingPrint(fileName+' has been successfully deleted\n')
            break
        else:
            typing.typingPrint('\nThe file does not exist\n')
            break
def viewFile(fileName):
    while True:
        try:
            f = open(fileName, 'r')
            typing.typingPrint(f.read())
            f.close()
            break
        except:
            typing.typingPrint('\nThe file does not exist\n')
            break

def commands():
    while True:
        #global rawcmd
        rawcmd = typing.typingInput('> ').split()
        cmd = rawcmd[0]
        #print (rawcmd)
        #print (cmd)
        
        if cmd == '?':
            typing.typingPrint('Here is a list of commands for the RobCo Industries (TM) TermLink System')
            typing.typingPrint('\n? - This page of Documentation')
            typing.typingPrint('\nls - See all files in the Current Working Directory')
            typing.typingPrint('\ncd - Change the Current Working Directory')
            typing.typingPrint('\ncd .. - Change the Current Working Directory to one level above the current Directory')
            typing.typingPrint('\ncwd - See the Current Working Directory')
            typing.typingPrint('\nmkdir - Create a new Directory')
            typing.typingPrint('\nmkfile - Create a new File')
            typing.typingPrint('\nrmvfile - Delete a file')
            typing.typingPrint('\neditfile - Edit the contents of a file')
            typing.typingPrint('\nreadfile - Read the contents of a file')
            typing.typingPrint('\nrmvtree - Delete a folder')
            typing.typingPrint('\nexit - Exits the terminal\n')
        elif cmd == 'ls':
            typing.typingPrint('Current Working Directory: ' +os.getcwd()+'\n')
            delimiter = '\n'
            files = delimiter.join(os.listdir())
            typing.typingPrint(files+'\n')
        elif cmd == 'cd':
            path = os.path.abspath(rawcmd[1])
            os.chdir(path)          
        elif cmd == 'cwd':
            typing.typingPrint(os.getcwd())
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

