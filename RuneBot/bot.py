from play import *
import pyautogui

print(pyautogui.getWindow("Old School RuneScape").get_position())

pyautogui.getWindow("Old School RuneScape").set_position(0, 0, 1930, 1040)

Bot()
