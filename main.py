# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bg_img = cv2.imread("/home/jason/icon_data/211.jpg")
    bg_img = cv2.resize(bg_img, (1280, 720))
    print_hi('PyCharm')
    blank_img = np.zeros((720, 1280, 3), np.uint8)
    cv2.namedWindow("pp", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("pp", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("pp", bg_img)
    while True:
        key = cv2.waitKey(10)
        if key == ord('q'):
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
