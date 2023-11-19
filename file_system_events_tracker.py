import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "D:/Downloads"
to_dir = "D:/Desktop/Coding/stuff"



# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("heAY, {event.src_path} has been creaated!")
    def on_deleted(self, event):
        print("WOAHHHh someone deleted {event.src.path}!")
    def on_moved(self, event):
        print("yoo, {event.src_path} has been moved!")
    def on_modified(self, event):
        print("I feel {event.src_path}'s presence changed")


                
       # print(event)
       # print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("STTTOPpED!")
    observer.stop()

    