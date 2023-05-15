import os, shutil, time
from Lib import typing_, clear, imageviewer, videoplayer
def cmd_help():
    typing_.typingPrint('Here is a list of commands for the RobCo Industries (TM) TermLink System')
    typing_.typingPrint('\n? or help - This page of Documentation')
    typing_.typingPrint('\nls or dir - See all files in the Current Working Directory')
    typing_.typingPrint('\ncd - Change the Current Working Directory')
    typing_.typingPrint('\ncd .. - Change the Current Working Directory to one level above the current Directory')
    typing_.typingPrint('\nmkdir - Create a new Directory')
    typing_.typingPrint('\nmkfile - Create a new File')
    typing_.typingPrint('\nrmvfile - Delete a file')
    typing_.typingPrint('\neditfile - Edit the contents of a file')
    typing_.typingPrint('\nreadfile - Read the contents of a file')
    typing_.typingPrint('\nrmvtree - Delete a folder')
    typing_.typingPrint('\nexit - Exits the terminal.\n \t exit -n - Shuts down the TermLink System. \n \t -r Restarts the TermLink System.')
    typing_.typingPrint('\nview - Opens a video or image')
    typing_.typingPrint('\npy or python - Runs a python script. (Meant for simple python scripts)\n')

def ls(): #Prints out the current directory.
    typing_.typingPrint(os.getcwd()+'\n')
    delimiter = '\n'
    files = delimiter.join(os.listdir())
    typing_.typingPrint(files+'\n')

def cd(name): #Changes the directory.
    try:
        path = os.path.abspath(name)
        os.chdir(path)
    except FileNotFoundError:
        typing_.typingPrint('No Directory with that name')
        
def shutdown(): # Closes the program.
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    middle = int((lines / 2)-2)
    cmiddle = int((columns/2))
    clear.clear()
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
    print("\n"*middle)
    typing_.typingPrint('   Thank you for using RobCo Industries (TM) TermLink!\n')
    print(" "*cmiddle)
    typing_.typingPrintDelay("     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", 5)
    clear.clear()
    exit()

def mkFile(fileName): #Creates a new file.
    while True:
        try:
            f = open(fileName, 'x')
            typing_.typingPrint('File ' + fileName +' created\n')
            break
        except FileExistsError:
            typing_.typingPrint('File exists already. Try a different name\n')
            break

def rmvFile(fileName): #Deletes a file.
    while True:
      if os.path.exists(fileName):
          os.remove(fileName)
          typing_.typingPrint(fileName+' has been successfully deleted\n')
          break
      else:
            typing_.typingPrint('\nThe file does not exist\n')
            break

def bypass(): #Allows for empty input.
    pass

def editFile(fileName): #Allows the User to edit files.
    viewFile(fileName)
    while True:
        with open(fileName, 'a') as f:
            try:
                f.write(typing_.typingInput('\n_')+'\n')
            except KeyboardInterrupt:
                print('\n')
                break

def viewFile(fileName): #Allows the User to read files.
    while True:
        try:
            f = open(fileName, 'r')
            typing_.typingPrint(f.read())
            f.close()
            break
        except:
            typing_.typingPrint('\nThe file does not exist\n')
            break

def view(fileName): #Allows the user to view images and videos
    file_name, file_extension = os.path.splitext(fileName)
    if file_extension == '.png' or file_extension == '.jpg' or file_extension == '.jpeg':
        try:
            imageviewer.viewImage(fileName)
        except KeyboardInterrupt:
            pass
        except FileNotFoundError:
            typing_.typingPrint('File does not exist\n')
            pass
    elif file_extension == '.mp4' or file_extension == '.avi' or file_extension == '.webm':
        try:
            videoplayer.viewVideo(fileName)
            #print('I am a work in progress')
        except KeyboardInterrupt:
            pass
        except FileNotFoundError:
            typing_.typingPrint('File does not exist\n')
            pass
    else:
        typing_.typingPrint("Please supply a .png, .jpg, or .mp4 file.")
        pass

def python(fileName): #Runs python scripts from within the program.
    while True:
        file_name, file_extension = os.path.splitext(fileName)
        if file_extension == '.py':
            with open(fileName) as f:
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

cmd_funcs = {  #List of all acceptable commands.
    '?': cmd_help,
    'help': cmd_help,
    'ls': ls,
    'cd': cd,
    'mkdir': os.mkdir,
    'mkFile': mkFile,
    'rmvFile': rmvFile,
    'editFile': editFile,
    'readFile': viewFile,
    'rmvtree': shutil.rmtree,
    'shutdown': shutdown,
    ' ': bypass,
    'view':view,
    'py':python,
    'python':python,  
}
def commands(): # All the commands on the terminal system.
    while True:
        try:
            rawcmd = typing_.typingInput('> ').split() # Splits the command into 2 parts.
            try:
                global cmd
                cmd = rawcmd[0]
            except IndexError:
                cmd = ' ' 
        except:
            pass
        try:
            cmd_funcs[rawcmd[0]](*rawcmd[1:])
        except KeyError:
            print("Invalid command:", rawcmd[0])
        except TypeError:
            print("Invalid command arguments:", *rawcmd[1:]) 
