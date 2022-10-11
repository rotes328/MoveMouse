import pyautogui
import random
from re import findall as findall
from time import sleep as sleep


def wait(seconds, index=0):
    a, b = index, 0
    list = ["[|]", "[/]", "[-]", "[\]"]
    while b < seconds:
        print("\r{}Running{}".format(list[a],list[a]), end="")
        sleep(0.5)
        a = (a + 1) % 4
        b += 1
    return a


def move_mouse(x):
    position = findall("\d+", str(pyautogui.position()))
    direction = random.randint(1,4)
    if direction == 1:
        pyautogui.moveTo((int(position[0]) + x), (int(position[1]) + x))
    elif direction == 2:
        pyautogui.moveTo((int(position[0]) + x), (int(position[1]) - x))
    elif direction == 3:
        pyautogui.moveTo((int(position[0]) - x), (int(position[1]) + x))
    else:
        pyautogui.moveTo((int(position[0]) - x), (int(position[1]) - x))
    pyautogui.moveTo((int(position[0]), (int(position[1]))))


def main():
    index = 0
    while(True):
        try:
            x = random.randint(1, 40)    # Random pixel range
            y = random.randint(10, 30)   # Random wait range
            move_mouse(x)
            index = wait(y, index)
        except KeyboardInterrupt:
            print("\nExiting")
            quit()


if __name__ == "__main__":
    main()