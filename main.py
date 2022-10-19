import pyautogui
import random
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
    positionX, positionY = pyautogui.position()
    direction = random.randint(1,4)
    match direction:
        case 1:
            pyautogui.moveTo(positionX + x, positionY + x)
            currentX, currentY = pyautogui.position()
            if positionX != (currentX - x) and positionY != (currentY - x):
                return
        case 2:
            pyautogui.moveTo(positionX + x, positionY - x)
            currentX, currentY = pyautogui.position()
            if positionX != (currentX - x) and positionY != (currentY + x):
                return
        case 3:
            pyautogui.moveTo(positionX - x, positionY + x)
            currentX, currentY = pyautogui.position()
            if positionX != (currentX + x) and positionY != (currentY - x):
                return
        case 4:
            pyautogui.moveTo(positionX - x, positionY - x)
            currentX, currentY = pyautogui.position()
            if positionX != (currentX + x) and positionY != (currentY + x):
                return
    pyautogui.moveTo(positionX, positionY)


def main():
    index = 0
    while(True):
        try:
            x = random.randint(1, 5)    # Random pixel range
            y = random.randint(10, 30)   # Random wait range
            move_mouse(x)
            index = wait(y, index)
        except KeyboardInterrupt:
            print("\nExiting")
            quit()


if __name__ == "__main__":
    main()