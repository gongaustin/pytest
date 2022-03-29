import os
import datetime
import pyinotify
import logging

pos = 0


def printlog():
    global pos
    try:
        fd = open("log_path.conf")
    if pos != 0:
        fd.seek(pos, 0)
    while True:
        line = fd.readline()
        if line.strip():
            print
            line.strip()
        pos = pos + len(line)
        if not line.strip():
            break
    fd.close()
    except Exception,e:
    print
    str(e)


class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        try:
            printlog()

    except Exception, e:
    print
    str(e)


def main():
    printlog()
    wm = pyinotify.WatchManager()
    wm.add_watch("log_path.conf", pyinotify.ALL_EVENTS, rec=True)
    eh = MyEventHandler()
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()


if __name__ == "__main__":
    main()