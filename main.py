import pyautogui
import random
from time import sleep as sleep
from datetime import datetime

pyautogui.FAILSAFE = False

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
    positionX, positionY = pyautogui.position()
    direction = random.randint(1,4)
    if direction == 1:
        pyautogui.moveTo(positionX + x, positionY + x)
        currentX, currentY = pyautogui.position()
        if positionX != (currentX - x) and positionY != (currentY - x):
            return
    elif direction == 2:
        pyautogui.moveTo(positionX + x, positionY - x)
        currentX, currentY = pyautogui.position()
        if positionX != (currentX - x) and positionY != (currentY + x):
            return
    elif direction == 3:
        pyautogui.moveTo(positionX - x, positionY + x)
        currentX, currentY = pyautogui.position()
        if positionX != (currentX + x) and positionY != (currentY - x):
            return
    else:
        pyautogui.moveTo(positionX - x, positionY - x)
        currentX, currentY = pyautogui.position()
        if positionX != (currentX + x) and positionY != (currentY + x):
            return
    pyautogui.moveTo(positionX, positionY)


def main():
    index = 0
    start = datetime.now().replace(microsecond=0)
    while(True):
        try:
            x = random.randint(1, 5)    # Random pixel range
            y = random.randint(10, 30)   # Random wait range
            move_mouse(x)
            index = wait(y, index)
        except KeyboardInterrupt:
            endtime = datetime.now().replace(microsecond=0)
            execution = endtime - start
            print(f"\nExiting after {execution}")
            quit()


if __name__ == "__main__":
    main()
