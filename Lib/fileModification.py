import os, shutil, time
from Lib import typing_, clear

def createFile(fileName):
    while True:
        try:
            f = open(fileName, 'x')
            typing_.typingPrint('File ' + fileName +' created\n')
            break
        except FileExistsError:
            typing_.typingPrint('File exists already. Try a different name\n')
            break
            
            
def editFile(fileName):
    '''
    while True:
        try:
            f = open(fileName, 'a')
            f.write(typing_.typingInput('Enter text here:\n')+'\n')
            f.close()
            break
        except:
            typing_.typingPrint('\nFile does not exist')
            break
    '''
    while True:
        with open(fileName, 'a') as f:
            try:
                f.write(typing_.typingInput('\n_')+'\n')
            except KeyboardInterrupt:
                print('\n')
                break
def deleteFile(fileName):
    while True:
        if os.path.exists(fileName):
            os.remove(fileName)
            typing_.typingPrint(fileName+' has been successfully deleted\n')
            break
        else:
            typing_.typingPrint('\nThe file does not exist\n')
            break
def viewFile(fileName):
    while True:
        try:
            f = open(fileName, 'r')
            typing_.typingPrint(f.read())
            f.close()
            break
        except:
            typing_.typingPrint('\nThe file does not exist\n')
            break

def commands():
    while True:
        try:
            rawcmd = typing_.typingInput('> ').split()
            cmd = rawcmd[0]
            
            
            if cmd == '?' or 'help':
                typing_.typingPrint('Here is a list of commands for the RobCo Industries (TM) TermLink System')
                typing_.typingPrint('\n? or help - This page of Documentation')
                typing_.typingPrint('\nls or dir - See all files in the Current Working Directory')
                typing_.typingPrint('\ncd - Change the Current Working Directory')
                typing_.typingPrint('\ncd .. - Change the Current Working Directory to one level above the current Directory')
                typing_.typingPrint('\ncwd - See the Current Working Directory')
                typing_.typingPrint('\nmkdir - Create a new Directory')
                typing_.typingPrint('\nmkfile - Create a new File')
                typing_.typingPrint('\nrmvfile - Delete a file')
                typing_.typingPrint('\neditfile - Edit the contents of a file')
                typing_.typingPrint('\nreadfile - Read the contents of a file')
                typing_.typingPrint('\nrmvtree - Delete a folder')
                typing_.typingPrint('\nexit - Exits the terminal')
                typing_.typingPrint('\npy or python - runs a python script. (Meant for simple python scripts)\n')
            elif cmd == 'ls' or cmd == 'dir':
                typing_.typingPrint('Current Working Directory: ' +os.getcwd()+'\n')
                delimiter = '\n'
                files = delimiter.join(os.listdir())
                typing_.typingPrint(files+'\n')
            elif cmd == 'cd':
                path = os.path.abspath(rawcmd[1])
                os.chdir(path)          
            elif cmd == 'cwd':
                typing_.typingPrint(os.getcwd())
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
                columns = shutil.get_terminal_size().columns
                lines = shutil.get_terminal_size().lines
                middle = int((lines / 2)-2)
                cmiddle = int((columns/2))
                clear.clear()
                print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
                print("\n"*middle)
                typing_.typingPrint('                                Thank you for using RobCo Industries (TM) TermLink Hardware! Goodbye!\n\n')
                print(" "*cmiddle)
                typing_.typingPrintDelay("                                                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", 5)
                time.sleep(5)
                clear.clear()
                exit()
            elif cmd == 'py' or 'python':
                
                    
                while True:
                
                    file_name, file_extension = os.path.splitext(rawcmd[1])
                    if file_extension == '.py':
                        with open(rawcmd[1]) as f:
                            try:
                                exec(f.read())
                                break
                            except KeyboardInterrupt:
                                break
                            except FileNotFoundError:
                                typing_.typingPrint('File does not exist\n')
                                break
                    else:
                        typing_.typingPrint("Please supply a python script with the '.py' file extension\n")
                        break
        except KeyboardInterrupt:
            typing_.typingPrint('Please use the command exit to exit the terminal\n')
            commands()
