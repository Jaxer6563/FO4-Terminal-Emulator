from pynput import keyboard

def on_activate_q():
    continue

def for_canonical_q(f):
    return lambda k: f(l.canonical(k))

quit = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+q'),
    on_activate_q)
with keyboard.Listener(
        on_press=for_canonical_q(quit.press),
        on_release=for_canonical_q(quit.release)) as l:
    l.join()
   