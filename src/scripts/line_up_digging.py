import ctypes
import keyboard
import mouse
import os
import time


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
SCREEN_WIDTH = screensize[0]
SCREEN_HEIGHT = screensize[1]


def move_mouse_to_percent_coor(x_percent: float, y_percent: float):
    mouse.move(
        int(SCREEN_WIDTH * x_percent),
        int(SCREEN_HEIGHT * y_percent),
        absolute=True,
        duration=0.0
    )


def move_mouse_to_bottom_middle(*args, **kwargs):
    move_mouse_to_percent_coor(0.5, 1)


def move_mouse_to_top_middle(*args, **kwargs):
    move_mouse_to_percent_coor(0.5, 0)


def move_mouse_to_left_middle(*args, **kwargs):
    move_mouse_to_percent_coor(0, 0.5)


def move_mouse_to_right_middle(*args, **kwargs):
    move_mouse_to_percent_coor(1, 0.5)


def click_mouse(*args, **kwargs):
    mouse.click()


if __name__ == '__main__':
    keyboard.on_press_key('up', move_mouse_to_top_middle)
    keyboard.on_press_key('down', move_mouse_to_bottom_middle)
    keyboard.on_press_key('left', move_mouse_to_left_middle)
    keyboard.on_press_key('right', move_mouse_to_right_middle)
    keyboard.on_press_key('`', click_mouse)

    while True:
        time.sleep(.3)
