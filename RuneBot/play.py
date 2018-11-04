import time
import pyautogui
import random
import os
from sequences import *

hour = 3600


class Bot:

    def __init__(self):
        self.action = input("What action would you like to perform?\n")
        self.bot_time = float(input("For how long? (hrs)\n")) * hour
        self.start_time = time.time()
        self.curr_time = time.time()
        self.prev_time = self.start_time

        print(self.bot_time, self.action)

        self.do(self.action)

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def read_mouse(self, filename):

        filename = self.find(filename, ".")
        print("filename", filename)
        fp = open(filename, "r")
        lines = fp.readlines()
        print("reading", filename)
        i = 0
        time.sleep(3)
        while i < len(lines)-1:
            x = int(lines[i].replace("\n", ""))
            y = int(lines[i+1].replace("\n", ""))
            delay = float(lines[i+2].replace("\n", ""))
            i += 3
            pyautogui.moveTo(x, y, pause=delay)
            pyautogui.click(x, y)

    def randomize_sequence(self, sequence_files):
        sequence = []

        for files in sequence_files:
            choice = random.choice(files)
            sequence.append(choice)

        return sequence

    def do(self, action):
        print("do", action)
        if action == "mine_iron":
            self.do_sequence(mine_iron_sequence)
        elif action == "mine_coal":
            self.do_sequence(mine_coal_sequence)
        elif action == "smelt":
            self.do_sequence(smelt_sequence)
        elif action == "sell_iron_ore":
            self.do_sequence(sell_iron_bar_sequence)

    def do_sequence(self, sequence):
        self.curr_time = time.time()
        print(self.curr_time - self.prev_time, self.bot_time)
        while self.curr_time - self.prev_time < self.bot_time:
            random_sequence = self.randomize_sequence(sequence)
            print("sequence", random_sequence)
            for file in random_sequence:
                self.read_mouse(file)
        self.prev_time = time.time()
