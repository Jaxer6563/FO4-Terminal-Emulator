import shutil
from Lib.clear import clear 
input("Press Enter to start")
clear.clear()
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines
print(columns)
print(lines)
input()
clear.clear()
middle = int((lines / 2)-2)
print("\n"*middle)
print("This is the middle of the terminal window".center(columns))
input()
clear.clear()
input("Now hit enter after maximizing the window")
clear.clear()
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines
print(columns)
print(lines)
input()
clear.clear()
middle = int((lines / 2)-2)
print("\n"*middle)
print("This is now the middle of the terminal window".center(columns))
input()
exit()