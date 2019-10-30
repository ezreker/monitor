import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FILEPATH = ""
FILENAME = "monitor_log_"
VERSION = 0
FILETYPE = ".txt"

def output(path,action):
	file = open(FILEPATH + FILENAME + str(VERSION) + FILETYPE,"a")
	file.write("File: " + path
		+ " Time: " + time.strftime("%m/%d/%Y - %H:%M:%S")
		+ " Action: " + action + "\n")

class DirectoryEventHandler(FileSystemEventHandler):

	def on_modified(self,event):
		output(event.src_path, "Modified")

	def on_created(self,event):
		output(event.src_path, "Created")

	def on_moved(self,event):
		output(event.src_path, "Moved")

	def on_deleted(self,event):
		output(event.src_path, "Deleted")

if __name__ == "__main__":
	event_handler = DirectoryEventHandler()
	observer = Observer()
	observer.schedule(event_handler,path='/Users/brandirosenbluth/My_Documents/Resume',recursive=False)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
