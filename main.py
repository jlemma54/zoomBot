import subprocess
import pyautogui
import time
from datetime import datetime


def sign_in(meetingid, pswd):
    # open zoom meeting
    subprocess.call(r"C:\Users\jlemm\AppData\Roaming\Zoom\bin\Zoom.exe")

    time.sleep(4)

    btn = pyautogui.locateCenterOnScreen("join_btn.png")
    pyautogui.moveTo(btn)
    pyautogui.click()

    time.sleep(1)
    pyautogui.write(meetingid)

    time.sleep(1)
    disconnect_audio_btn = pyautogui.locateCenterOnScreen("disconnect_audio.png")
    pyautogui.moveTo(disconnect_audio_btn)
    pyautogui.click()

    time.sleep(1)
    disconnect_video_btn = pyautogui.locateCenterOnScreen("disconnect_video.png")
    pyautogui.moveTo(disconnect_video_btn)
    pyautogui.click()

    time.sleep(1)
    join2_btn = pyautogui.locateCenterOnScreen("join2.png")
    pyautogui.moveTo(join2_btn)
    pyautogui.click()

    if pswd != "/" and pswd != "/\n":
        time.sleep(5)
        pyautogui.write(pswd)

        time.sleep(1)
        password_btn = pyautogui.locateCenterOnScreen("password_btn.png")
        pyautogui.moveTo(password_btn)
        pyautogui.click()


def getInfo():

    file1 = open('logs.txt', 'r')
    Lines = file1.readlines()
    lineformated = [x.split(",") for x in Lines]
    return lineformated

def formatTime(index):
    temp = getInfo()
    units = temp[index][0].split("-")
    units2 = [int(float(x)) for x in units]
    product = datetime(units2[0], units2[1], units2[2], units2[3], units2[4])
    product2 = str(product)
    product3 = product2.replace("-", ":").replace(" ", ":")
    return product3

def getID(counter):
    return data[counter][1]
def getPswd(counter):
    return data[counter][2]


counter = 1

global data
data = getInfo()

meetingCount = len(data) - 1
while True:
    if counter >= meetingCount:
        break
    currentTime = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    if currentTime == formatTime(counter):
        sign_in(getID(counter=counter), getPswd(counter=counter))
        counter += 1