import sys
import random
import os


class FileCreator:

    def __init__(self, read_file, write_file, number_of_clicks):
        self.read_filename = ""
        self.write_filename = ""
        self.num_lines = 0
        self.read_filename = read_file
        self.write_filename = write_file
        self.num_lines = number_of_clicks
        self.curr_file_num = 0

        self.unique_xy = []
        self.unique_delay = []

        self.get_unique_positions()
        self.create_file()

    def get_unique_positions(self):
        fp = open(self.read_filename, "r")
        lines = fp.readlines()
        unique_pos = []

        i = 0
        while i < len(lines):
            x = lines[i]
            y = lines[i+1]
            delay = lines[i+2]

            if (x, y) not in self.unique_xy:
                self.unique_xy.append((x, y))

            if delay not in self.unique_delay:
                self.unique_delay.append(delay)

            i += 3

        return unique_pos

    def create_file(self):
        self.write_filename = self.write_filename
        if os.path.isfile(self.write_filename):
            os.remove(self.write_filename)
            fp = open(self.write_filename, "a")
        else:
            fp = open(self.write_filename, "a")

        for i in range(0, self.num_lines):
            rand_xy = random.choice(self.unique_xy)
            rand_x = rand_xy[0]
            rand_y = rand_xy[1]
            rand_delay = random.choice(self.unique_delay)

            fp.write(rand_x)
            fp.write(rand_y)
            fp.write(rand_delay)
