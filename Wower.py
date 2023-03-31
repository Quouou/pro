import time
import pyautogui
import PySimpleGUI as sg
import sys
import threading



Checker = False
Healing = 0
offSwitch = False
startSwitch = False

def gui():
    global offSwitch, startSwitch
    layout = [[sg.Text("Training Bot")], [sg.Button("Start")], [sg.Button("Stop")]]
    window = sg.Window("Demo", layout)
    while True:
        event, values = window.read(timeout=500)
    # End program if user closes window or
    # presses the OK button
        if event in (None, 'Start'):
            startSwitch = True
            while(startSwitch == True):
                automaticBattle()
        elif event == "Stop" or event == sg.WIN_CLOSED:
             offSwitch = True
             break
            

    window.close()


def foundImg(img, detail = 0.8):
    return pyautogui.locateOnScreen('./assets/'+img+'.png', confidence=detail) != None
def locateImg(img):
    return pyautogui.locateCenterOnScreen('./assets/'+img+'.png', confidence=0.8)
def isGameOpen():
    return foundImg('game_open') != None or foundImg('game_open2') != None
def isInBattle():
    return foundImg('battle')
def is_your_turn():
    return foundImg('your_turn')
def no_pp():
    return foundImg('noPP')
def secnd_turn():
    return foundImg('second')
def budew():
    return foundImg('budew')
# Mt Moon
def geodude():
     return foundImg('geodude')
def paras():
     return foundImg('paras')
def sandshrew():
     return foundImg('sandshrew')
def zubat():
     return foundImg('zubat')
# Rock Tunner
def golbat():
     return foundImg('golbat')
attack_to_use = 3
outOfPPFirst = False
outOfPPSecond = False
outOfPPThirs = False
outOfPPFourth = False

def kadabraDead():
     return foundImg('kadead')
def kadabralive():
     return foundImg('kadabralive')

# def goToJoy():
#     pyautogui.press('d')
#     if foundImg('nursejoy2') and foundImg('kadead'):
#             talkWithJoy()

# def talkWithJoy():
#     global Healing
#     pyautogui.press('space')
#     if foundImg('nurse1'):
#             pyautogui.press('space')
#     if foundImg('nurse2'):
#             pyautogui.press('1')
#     if foundImg('nurse3'):
#             pyautogui.press('space')
#     if foundImg('nurse4'):
#             pyautogui.press('space') 
#             Healing+=1
#             print('Amount of times healed: ' + str(Healing))
#             automaticBattle()


def attack_mode():
    global attack_to_use
    global outOfPP
    while is_your_turn():
        print('Your turn')
        pyautogui.press('1')
        pyautogui.press('1')

# def attack_mode_mtMoon():
#      global attack_to_use
#      global outOfPP
#      while is_your_turn():
#         print('Your turn')
#         if no_pp():
#             print('First move is out of PP!')
#             pyautogui.press('1')
#             pyautogui.press('4')
#         if geodude() | sandshrew() :
#                 pyautogui.press('1')
#                 pyautogui.press('2')
#         if zubat() | paras() :
#             if budew():
#                 pyautogui.press('2')
#                 pyautogui.press('2')
#             elif secnd_turn():
#                 pyautogui.press('1')
#                 pyautogui.press('3')
#         else:
#               pyautogui.press('1')
#               pyautogui.press('2')
def attack_mode_RockMoon():
     global attack_to_use
     global outOfPPFirst, outOfPPSecond, outOfPPThirs, outOfPPFourth
     while is_your_turn():
        print('Your turn')
        if no_pp():
            print('First move is out of PP!')
            pyautogui.press('1')
            pyautogui.press('3')
            # if no_pp():
            #      outOfPPSecond = True
            #      if(outOfPPSecond == True):
            #             print('Second move is out of PP!')
            #             pyautogui.press('1')
            #             pyautogui.press('2')
            #             if no_pp():
            #                  outOfPPThirs = True
            #                  if(outOfPPThirs == True):
            #                        print('Third move is out of PP!')
            #                        pyautogui.press('1')
            #                        pyautogui.press('4')
        
                            


        # if geodude() | sandshrew() :
        #         pyautogui.press('1')
        #         pyautogui.press('2')
        # if golbat() | paras() :
        #     if budew():
        #         pyautogui.press('2')
        #         pyautogui.press('2')
        #     elif secnd_turn():
        #         pyautogui.press('1')
        #         pyautogui.press('3')
        else:
              pyautogui.press('1')
              pyautogui.press('1')

def catch():
    if is_your_turn():
        print('Attempting to Catch')
        pyautogui.press('3')
        pyautogui.press('1')

def automaticBattle():
        if  isInBattle():   
            print("IN BATTLE")
            attack_mode_RockMoon()
        else:
            print("Not in battle")
            pyautogui.keyDown('a')
            time.sleep(0.5)
            pyautogui.keyUp('a')
            pyautogui.keyDown('d')
            time.sleep(0.5)
            pyautogui.keyUp('d')
            



while isGameOpen():
            # if  kadabraDead():
            #     goToJoy()
            # else:
            if(offSwitch == False):
                print("Looking for a Battle")
                automaticBattle()
            else:
                 sys.exit("Ended")
