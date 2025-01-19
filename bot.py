from time import sleep
import sys
import keyboard 
import random
import pyautogui 
import threading
import math
import re
from screeninfo import get_monitors

#Optional settings if you dont want to setup the program everytime you run it
number = None #Agent slot
always_use_detected_resolution = False #Set to true if you want to use automatically detected resolution
send_chat_messages = None #Set to true or false depending on whether you want to send chat messages or not

def get_primary_monitor_resolution():
    for monitor in get_monitors():
        monitor_str = str(monitor)
        if "is_primary=True" in monitor_str:
            res = re.search(r'width=(\d+), height=(\d+)', monitor_str)
            if res:
                resx = int(res.group(1))
                resy = int(res.group(2))
                return resx, resy
    return None

primary_res = get_primary_monitor_resolution()

if primary_res:
    resx, resy = primary_res

pyautogui.FAILSAFE = False


art_text = """
   _____  _______________  __.        __________ ___________________
  /  _  \ \_   _____/    |/ _|        \______   \\_____  \__    ___/
 /  /_\  \ |    __) |      <    ______ |    |  _/ /   |   \|    |   
/    |    \|     \  |    |  \  /_____/ |    |   \/    |    \    |   
\____|__  /\___  /  |____|__ \         |______  /\_______  /____|   
        \/     \/           \/                \/         \/             V1.4

Use this tool on your own risk. I dont think you'll get banned but i cant guarantee anything.
"""

keybinds = """
+------------------+---------+------------+
|      Action      | Keybind | Importance |
+------------------+---------+------------+
| Ability 3        | E       | needed     |
| Fire             | J       | needed     |
| Ultimate         | N       | optional   |
| Alternate fire   | K       | optional   |
| Primary weapon   | 1       | optional   |
| Secondary Weapon | 2       | optional   |
| Melee weapon     | 3       | optional   |
| Inspect          | C       | optional   |
| Spray            | Y       | optional   |
+------------------+---------+------------+

"""

explain = """
Example:
+---------+--------+-----------+---------+
|  1.Iso  | 2.Omen |  3.Neon   | 4.Jett  |
+---------+--------+-----------+---------+
| 5.Reyna | 6.Raze | 7.Killjoy | 8.Clove | <-- Agent slot of Killjoy is 7 here
+---------+--------+-----------+---------+
       
"""


print(art_text)
print()

if number == None:
    print("You have to select the agent slot of Killjoy.")
    print("Killjoy is needed so you dont get detected as afk.")
    print("The Agent slot is on which position Killjoy is when selecting an Agent.")
    print(explain)
    print()

    user_input = input("Enter your Agent slot of Killjoy: ")

    # Convert the input to an integer
    try:
        number = int(user_input)
        print(f"Slot {number} selected")
    except ValueError:
        print("That's not a valid integer.")
        exit()
    print()


print(f"Detected screen resolution {resx}x{resy}")
print("[INFO] Stretched maybe wont work as expected!")
print("[INFO] Only tested resolution is 1600x900!")
print("[INFO] It's recommended to set your game to this resolution!")

if not always_use_detected_resolution:
    setres = input("Is this resolution correct? (Y/n): ").strip().lower()
    if setres == 'n':
        # Prompt user for screen resolution
        resolution = input("Enter your screen resolution (example: 1920x1080): ")

        # Split the resolution into width and height
        try:
            width, height = resolution.split('x')
            resx = int(width)
            resy = int(height)
            print(f"Set resolution to {resx}x{resy}")
        except ValueError:
            print("Invalid resolution format. Please enter it in the format 'width x height' (e.g., 1920x1080).")
            exit()

if send_chat_messages == None:
    print()
    noannoy = input("Should the bot send some mildly annoying messages in ingame chat? (Y/n): ").strip().lower()
    noannoy = 1 if noannoy == 'n' else 0
elif send_chat_messages:
    noannoy = 0
else:
    noannoy = 1

if noannoy == 1:
    print("Chat turned off.")
else:
    print("Chat turned on.")

print()
print("Make sure to change your Keybinds to the following:")
print(keybinds)
input("Press any key to continue...")




if number==1 or number==5 or number==9 or number==13 or number==17:
    slotx = 1

elif number==2 or number==6 or number==10 or number==14 or number==18:
    slotx = 2
    
elif number==3 or number==7 or number==11 or number==15 or number==19:
    slotx = 3

elif number==4 or number==8 or number==12 or number==16 or number==20:
    slotx = 4
    
if number == 1 or number == 2 or number == 3 or number == 4:
    sloty = 1

elif number == 5 or number == 6 or number == 7 or number == 8:
    sloty = 2

elif number == 9 or number == 10 or number == 11 or number == 12:
    sloty = 3

elif number == 13 or number == 14 or number == 15 or number == 16:
    sloty = 4

elif number == 17 or number == 18 or number == 19 or number == 20:
    sloty = 5

if sloty == 1:
    ressloty=0.3222222
elif sloty == 2:
    ressloty=0.4230111
elif sloty == 3:
    ressloty=0.5100555
elif sloty == 4:
    ressloty=0.6059722
elif sloty == 5:
    ressloty=0.6888888
    
if slotx == 1:
    resslotx=0.04375
elif slotx == 2:
    resslotx=0.09726563
elif slotx == 3:
    resslotx=0.14765625
elif slotx == 4:
    resslotx=0.19921875


res0x = math.ceil(0.5 * resx)
res0y = 2
res1x = math.ceil(0.559765625 * resx)
res1y = math.ceil(0.880555555556 * resy)
res2x = math.ceil(resslotx * resx)
res2y = math.ceil(ressloty * resy)
res3x = math.ceil(0.4886719 * resx)
res3y = math.ceil(0.68 * resy)
res4x = math.ceil(0.5114754 * resx)
res4y = math.ceil(0.7666667 * resy)
res5x = math.ceil(0.6368627 * resx)
res5y = math.ceil(0.225 * resy)

def main():
    global noannoy
    global queue
    global running
    running=True
    queue=1
    print('\nHold the q-key to stop the program')
    print("Hold the u-key to toggle the chat function")
    print("Hold the i-key to disable queuing again")
    print("Hold the p-key to pause")
    print('Starting bot in 5 sec ')
    print()
    sleep(5)

    # check if valorant is active than run
    try:
        focusOnValorant()
        sleep(1)
        # came here means valo is active and chat_afk() function executed
        global bot_flag 
        bot_flag = True # will be used to terminate the bot / thread
        # creating thread  or  yes u can pass function XD
        t1 = threading.Thread(target = no_afk ) 
        # starting thread  or  calling no_afk in parallel
        t1.start()
        while bot_flag == True:
            sleep(0.2)
            if keyboard.is_pressed('q'):
                bot_flag = False
                return
            elif keyboard.is_pressed('u'):
                if noannoy == 1:
                    noannoy = 0
                    print("Chat turned on.")
                else:
                    noannoy = 1
                    print("Chat turned off.")
            elif keyboard.is_pressed('i'):
                if queue == 1:
                    queue = 0
                    print("Queueing again has been disabled!")
                    print("Hold the i-key to reenable")
                else:
                    queue = 1
                    print("Queueing again has been reenabled")
            elif keyboard.is_pressed('p'):
                if running:
                    print("Program paused")
                    running = False
                else:
                    print("Program unpaused")
                    running = True


        # end of try block        
    except:
        print()
        # thinking...

    print('\n       THATS DONE!!    ')


def focusOnValorant():
            chat_afk()

def chat_afk():
    if noannoy == 0:
        sleep(0.5)
        keyboard.press_and_release('enter')
        sleep(1)
        pyautogui.typewrite('Im going AFK , my bot is on! :)')
        sleep(0.5)
        keyboard.press_and_release('enter')
    pyautogui.moveTo(res1x, res1y)
    sleep(1)
    pyautogui.click()
    

def no_afk():
    sleep(0.5)
    global noannoy
    global queue
    global running
    while bot_flag == True:
        while running:
            choice = random.randint(1,80) # 1 to 10
            sleeptime = random.randint(1,2)
            
            #sed lyf no switch case :(
            # W
            if choice == 1:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('w')
                sleep(sleeptime)
                keyboard.release('w')
            # A
            elif choice == 2:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('a')
                sleep(sleeptime)
                keyboard.release('a')
            # S
            elif choice == 3:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(sleeptime)
                keyboard.release('s')
            # D
            elif choice == 4:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('d')
                sleep(sleeptime)
                keyboard.release('d')
            # jump
            elif choice == 5:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('space')
                sleep(sleeptime)
                keyboard.release('space')
            # crouch
            elif choice == 6:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('control')
                sleep(sleeptime)
                keyboard.release('control')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('k')

            # lets have some fun 
            # lOL    
            elif choice == 7 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite(' LOL :)')
                sleep(1)
                keyboard.press_and_release('enter')
                # sleep(sleeptime)
            # afk 
            elif choice == 8 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Sorry boiz Im AFK')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(sleeptime)
            # Im a bot
            elif choice == 9 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Sry im just a bot in this game dont blame me')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(sleeptime)
            # buy
            elif choice == 10: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                for _ in range(30):
                    keyboard.press_and_release('c')
                    sleep(0.1)
            
            elif choice == 11: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('y')
                
            elif choice == 12 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Im just a bot so i cant really play, enjoy the free win!')
                sleep(1)
                keyboard.press('shift')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                keyboard.release('shift')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 13 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Remember that im a free kill at spawn!')
                sleep(1)
                keyboard.press('shift')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                keyboard.release('shift')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 14 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('/ff')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(3)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('ff guys')
                sleep(1)
                keyboard.press_and_release('enter')

            elif choice == 15: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 16 and noannoy == 0: 
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('ez')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 17 and noannoy == 0: 
                randomm = random.randint(1,15)
                if randomm == 15:
                    keyboard.press_and_release('f5')
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    pyautogui.typewrite('sry for being afk im back now')
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(10)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    pyautogui.typewrite('jk im not coming back XD')
                    sleep(1)
                    keyboard.press_and_release('enter')
                    sleep(1)
                    keyboard.press_and_release('k')
                    sleep(1)
                    keyboard.press_and_release('k')
            elif choice == 18:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.release('s')
            elif choice == 19:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('w')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.release('w')
            elif choice == 20:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('w')
                sleep(1)
                keyboard.press('a')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.release('w')
                sleep(1)
                keyboard.release('a')
            elif choice == 21:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('w')
                sleep(1)
                keyboard.press('d')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.press_and_release('space')
                sleep(1)
                keyboard.release('w')
                sleep(1)
                keyboard.release('d')
            elif choice == 22:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('w')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press('a')
                sleep(10)
                keyboard.release('a')
                sleep(1)
                keyboard.press('d')
                sleep(5)
                keyboard.release('d')
                sleep(1)
                keyboard.press('a')
                sleep(5)
                keyboard.release('a')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press('d')
                sleep(5)
                keyboard.release('d')
                sleep(1)
                keyboard.press('a')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(5)
                keyboard.release('a')
                sleep(1)
                keyboard.press('d')
                sleep(5)
                keyboard.release('d')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press('a')
            elif choice == 23 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('n')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Atleast i can ult')
                sleep(1)
                keyboard.press('shift')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                keyboard.release('shift')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('k')
                sleep(1)
                keyboard.press_and_release('k')
            elif choice == 24 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('Drop me an Odin please!!!')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(10)
                keyboard.press_and_release('1')
                sleep(1)
                keyboard.press('j')
                sleep(3)
                keyboard.release('j')
                sleep(1)
                keyboard.press('j')
                sleep(3)
                keyboard.release('j')
                sleep(1)
                keyboard.press('j')
                sleep(3)
                keyboard.release('j')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
                keyboard.press_and_release('j')
                sleep(1)
            elif choice == 25 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('NT Guys!!! Keep it up :)')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 26: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(6)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 27: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(6)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 28: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(6)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 29: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(3)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 30: 
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(3)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 32:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press('s')
                sleep(1)
                keyboard.release('s')
                sleep(1)
                keyboard.press_and_release('e')
                sleep(2)
                keyboard.press_and_release('j')
            elif choice == 33 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('im smurf btw')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 34 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('If you want a boost add me')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 35 and noannoy == 0:
                keyboard.press_and_release('f5')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('ew')
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(3)
                keyboard.press_and_release('enter')
                sleep(1)
                pyautogui.typewrite('aimlabs.com is free btw')
                sleep(1)
                keyboard.press_and_release('enter')
            elif choice == 36:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                for _ in range(30):
                    keyboard.press_and_release('2')
                    sleep(0.1)
                    keyboard.press_and_release('3')
                    sleep(0.1)
            elif choice == 37:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                for _ in range(4):
                    keyboard.press_and_release('.')
                    sleep(0.5)
                    keyboard.press_and_release('1')
                    sleep(0.5)
                    keyboard.press_and_release('1')
                    sleep(1)
            elif choice == 38 or choice == 39:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                pyautogui.moveTo(res4x, res4y)
                sleep(0.3)
                pyautogui.click()
            elif choice == 40 or choice == 41:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                pyautogui.moveTo(res5x, res5y)
                sleep(0.3)
                pyautogui.click()
            elif choice <= 47:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                if queue == 1:
                    pyautogui.moveTo(res0x, res0y)
                    sleep(1)
                    pyautogui.click()
                    sleep(1)
                    pyautogui.moveTo(res1x, res1y)
                    sleep(1)
                    pyautogui.click()
            elif choice >= 48:
                if noannoy == 0:
                    keyboard.press_and_release('f5')
                sleep(1)
                pyautogui.moveTo(res2x, res2y)
                sleep(0.3)
                pyautogui.click()
                sleep(0.3)
                pyautogui.moveTo(res3x, res3y)
                sleep(0.5)
                pyautogui.click()
                sleep(0.5)
                pyautogui.moveTo(1, 1)
                sleep(0.5)
                pyautogui.click()
            
    #end of while loop
# end of afk function 

# ******** Main Function ********** # 
# calling main function
if __name__ == "__main__":
    main()
