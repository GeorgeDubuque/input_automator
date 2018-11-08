from pynput.mouse import Controller, Listener
import os
import sys
import time


class MouseRecorder:

    def __init__(self):
        print("initting")
        self.curr_time = time.time()
        self.prev_time = time.time()
        self.action = input("Action:\n")
        self.actionable = input("On:\n")
        self.filename = input("Write file:\n")
        if self.actionable != "":
            self.filename = "./" + self.action + "/" + self.actionable + "/" + self.filename
        else:
            self.filename = "./" + self.action + "/" + self.filename

        self.mouse = Controller()
        if os.path.isfile(self.filename):
            os.remove(self.filename)
            self.f = open(self.filename, "a")
        else:
            self.f = open(self.filename, "a")

        with Listener(on_click=self.on_click,
                      on_move=self.on_move) as listener:
            listener.join()

        self.f.close()

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.f = open(self.filename, "a")
            self.curr_time = time.time()
            delay = self.curr_time - self.prev_time
            print(delay)
            print("click")
            self.f.write(str(x) + "\n")
            self.f.write(str(y) + "\n")
            self.f.write(str(delay) + "\n")
            self.prev_time = time.time()
            self.f.close()


MouseRecorder()





