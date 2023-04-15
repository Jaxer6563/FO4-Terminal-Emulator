from pynput import keyboard

done = False  # flag on loop runs


def stop_run():  # function to stop the program
    global done
    done = True


# register a hotkey, and call stop_run() when it is pressed
with keyboard.GlobalHotKeys({'<ctrl>+q': stop_run}) as h:
    while done == False:
        print("Running ... ")