import os
import cv2
import numpy as np
import pyautogui
import time
import keyboard
from win10toast import ToastNotifier

authorName = "Sahil Rajwar" 
homePage ="https://github.com/Sahil-Rajwar-2004/SS-n-SR"

running = True

def take_screenshot(delay = 0):
    if delay < 0:
        return "Invalid argument"
    if delay > 0:
        print(f"Taking a screenshot in {delay} seconds...")
        time.sleep(delay)

    screenshot = pyautogui.screenshot()
    notify = ToastNotifier()
    notify.show_toast("tools.py","Screenshot taken successfully",duration = 5)
    print("Captured screenshot")
    fileName = str(input("file name? "))
    filePath = os.path.join(os.getcwd(),fileName+".png")
    print(filePath)

    if not filePath:
        print("Screenshot couldn't saved!")
        return

    screenshot.save(filePath)
    print(f"Screenshot saved at '{filePath}'")

def record_screen(delay = 0):
    screen_width, screen_height = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fileName = str(input("file name? "))
    output_filename = os.path.join(os.getcwd(),fileName+".avi")
    if delay > 0:
        print(f"screen recording will start in {delay} seconds...")
        time.sleep(delay)
    else:
        print("delay time shouldn't be negative or a string")
        return
    fps = 30
    out = cv2.VideoWriter(output_filename,fourcc,fps,(screen_width, screen_height))
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live",(480,270))
    print("Recording... Press 'q' to stop.")
    while not keyboard.is_pressed("q"):
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
        out.write(frame)
        cv2.imshow("Live",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()
    print("Screen recording stopped.")
    print(f"file saved at {output_filename}")


while running:
    prompt = str(input("(ss/sr/exit/about)? ")).lower()
    if prompt == "ss":
        delayTime = float(input("delay? "))
        try:
            take_screenshot(delayTime)
        except Exception as e:
            print(e)
    elif prompt == "sr":
        delayTime = float(input("delay? "))
        try:
            record_screen(delayTime)
        except Exception as e:
            print(e)
    elif prompt == "about":
        print(authorName)
        print(homePage)
    elif prompt == "exit":
        running = False
    else:
        print("invalid prompt")


