# This script is made to do the google minesweeper:
# https://www.google.com/search?q=minesweeper&oq=&ie=UTF-8

# This function completes minesweeper using screenshot and colour matching.
# To work it you have to have your browser (using Brave browswer) on the
# left side of the screen (1080p screen).


# grid is 18x14

# top left          pixel 210x 397y
# bottom right      pixel 750x 817y

# 30 pixel change. 15 pixel offset

import pyautogui
import pyautogui as pag
import random
import time
import numpy as np
import win32api, win32con
import mss
from pyclick import HumanClicker
hc = HumanClicker()

def click():
    # time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def bomb():
    # time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

# if the coordinate is out of bounds, returns 88
def safe_get(arr, row, col):
    if 0 <= row < len(arr) and 0 <= col < len(arr[row]):
        return arr[row][col]
    return 88

map = [[0 for _ in range(18)] for _ in range(14)]

region = {"left": 210, "top": 397, "width": 540, "height": 420}

pag.moveTo(480, 606, 0)
click()
time.sleep(0.02)
click()

time.sleep(1)

while pyautogui.pixel(219, 346)[1] == 117:
    # takes screenshot of the area and looks for colours for all squares.
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = np.array(screenshot)
        
        for j in range(14):
            for i in range(18):
                b, g, r, _ = img[15 + 30 * j, 16 + 30 * i]
                if 209 <= g <= 221:
                    map[j][i] = 0
                elif 184 <= g <= 194:
                    map[j][i] = 8
                elif abs(g - 118) <= 3:
                    map[j][i] = 1
                elif abs(g - 142) <= 3:
                    map[j][i] = 2
                elif abs(g - 47) <= 3:
                    map[j][i] = 3
                elif abs(g - 31) <= 3:
                    map[j][i] = 4
                

                b, g, r, _ = img[10 + 30 * j, 8 + 30 * i]
                if abs(g - 54) <= 3:
                    map[j][i] = 9
                
                b, g, r, _ = img[13 + 30 * j, 15 + 30 * i]
                if abs(r - 255) <= 3:
                    map[j][i] = 5
                if abs(g - 151) <= 3:
                    map[j][i] = 6

    # randomizes the order the script looks at each square 
    rand18 = list(range(0, 18))
    random.shuffle(rand18)
    rand14 = list(range(0, 14))
    random.shuffle(rand14)

    for m in rand14:
        for n in rand18:
            
            count = 0 
            count2 = 0
            count3 = 0
            check = [[99 for _ in range(2)] for _ in range(9)]
            check2 = [[99 for _ in range(2)] for _ in range(9)]
            l = 0

            # looks at the a 3x3 area around the position
            if map[m][n] >= 1:
                x = safe_get(map, m-1, n-1)
                if x in (0, 9, 10):
                    if x == 0:
                        check[l][0] = m-1
                        check[l][1] = n-1
                        l += 1
                    if x == 9:
                        count2 += 1
                    if x == 10:
                        check2[count3][0] = m-1
                        check2[count3][1] = n-1
                        count3 += 1
                    count += 1
                xx = safe_get(map, m-1, n)
                if xx in (0, 9, 10):
                    if xx == 0:
                        check[l][0] = m-1
                        check[l][1] = n
                        l += 1
                    if xx == 9:
                        count2 += 1
                    if xx == 10:
                        check2[count3][0] = m-1
                        check2[count3][1] = n
                        count3 += 1
                    count += 1
                xxx = safe_get(map, m-1, n+1)
                if xxx in (0, 9, 10):
                    if xxx == 0:
                        check[l][0] = m-1
                        check[l][1] = n+1
                        l += 1
                    if xxx == 9:
                        count2 += 1
                    if xxx == 10:
                        check2[count3][0] = m-1
                        check2[count3][1] = n+1
                        count3 += 1
                    count += 1
                y = safe_get(map, m, n-1)
                if y in (0, 9, 10):
                    if y == 0:
                        check[l][0] = m
                        check[l][1] = n-1
                        l += 1
                    if y == 9:
                        count2 += 1
                    if y == 10:
                        check2[count3][0] = m
                        check2[count3][1] = n-1
                        count3 += 1
                    count += 1
                yy = safe_get(map, m, n+1)
                if yy in (0, 9, 10):
                    if yy == 0:
                        check[l][0] = m
                        check[l][1] = n+1
                        l += 1
                    if yy == 9:
                        count2 += 1
                    if yy == 10:
                        check2[count3][0] = m
                        check2[count3][1] = n+1
                        count3 += 1
                    count += 1
                z = safe_get(map, m+1, n-1)
                if z in (0, 9, 10):
                    if z == 0:
                        check[l][0] = m+1
                        check[l][1] = n-1
                        l += 1
                    if z == 9:
                        count2 += 1
                    if z == 10:
                        check2[count3][0] = m+1
                        check2[count3][1] = n-1
                        count3 += 1
                    count += 1
                zz = safe_get(map, m+1, n)
                if zz in (0, 9, 10):
                    if zz == 0:
                        check[l][0] = m+1
                        check[l][1] = n
                        l += 1
                    if zz == 9:
                        count2 += 1
                    if zz == 10:
                        check2[count3][0] = m+1
                        check2[count3][1] = n
                        count3 += 1
                    count += 1
                zzz = safe_get(map, m+1, n+1)
                if zzz in (0, 9, 10):
                    if zzz == 0:
                        check[l][0] = m+1
                        check[l][1] = n+1
                        l += 1
                    if zzz == 9:
                        count2 += 1
                    if zzz == 10:
                        check2[count3][0] = m+1
                        check2[count3][1] = n+1
                        count3 += 1
                    count += 1

                # checks if the squares around match how many bombs and if it lines
                # up it places bombs in those squares
                if count == map[m][n]:
                    k = 0
                    while check[k][0] != 99:
                        map[check[k][0]][check[k][1]] = 9
                        pag.moveTo(225 + 30 * check[k][1], 412 + 30 * check[k][0], 0)
                        # hc.move((225 + 30 * check[k][1], 412 + 30 * check[k][0]), 0.1)
                        bomb()
                        k += 1
                    k = 0
                    while check2[k][0] != 99:
                        map[check2[k][0]][check2[k][1]] = 9
                        pag.moveTo(225 + 30 * check2[k][1], 412 + 30 * check2[k][0], 0)
                        # hc.move((225 + 30 * check2[k][1], 412 + 30 * check2[k][0]), 0.1)
                        bomb()
                        k += 1
                
                # if there is already enough bombs around the position, click in
                # all the clear places
                if count2 == map[m][n]:
                    k = 0
                    while check[k][0] != 99:
                        map[check[k][0]][check[k][1]] = 8
                        pag.moveTo(225 + 30 * check[k][1], 412 + 30 * check[k][0], 0)
                        # hc.move((225 + 30 * check[k][1], 412 + 30 * check[k][0]), 0.1)
                        click()
                        k += 1
                    k = 0
                    while check2[k][0] != 99:
                        map[check2[k][0]][check2[k][1]] = 8
                        pag.moveTo(225 + 30 * check2[k][1], 412 + 30 * check2[k][0], 0)
                        # hc.move((225 + 30 * check2[k][1], 412 + 30 * check2[k][0]), 0.1)
                        click()
                        k += 1
                
                # if theres one bomb and two squares open then make them temp
                # equal 10
                if count == map[m][n] + 1 and count2 == map[m][n] - 1 and count2 < map[m][n]:
                    k = 0
                    while check[k][0] != 99:
                        map[check[k][0]][check[k][1]] = 10
                        k += 1
                
                # If the position needs one more bomb and there is two 10 squares 
                # nearby as well as an open square assume that the open square is free.
                if count2 + count3 - 1 == map[m][n] and count2 < map[m][n]:
                    k = 0
                    while check[k][0] != 99:
                        map[check[k][0]][check[k][1]] = 8
                        pag.moveTo(225 + 30 * check[k][1], 412 + 30 * check[k][0], 0)
                        # hc.move((225 + 30 * check[k][1], 412 + 30 * check[k][0]), 0.1)
                        click()
                        k += 1
                
                # if the position needs two more bombs and there is two 10 squares nearby
                # as well as an open square assume that the open square is a bomb too.
                if count2 + count3 == map[m][n] and count == map[m][n] + 1 and count2 < map[m][n] and count3 == 2 and count - count2 - count3 == 1 and map[m][n] < 4:
                    k = 0
                    while check[k][0] != 99:
                        map[check[k][0]][check[k][1]] = 9
                        pag.moveTo(225 + 30 * check[k][1], 412 + 30 * check[k][0], 0)
                        # hc.move((225 + 30 * check[k][1], 412 + 30 * check[k][0]), 0.1)
                        bomb()
                        k += 1
    # for w in range(14):
    #     print(map[w])
    # print()

    # slows it down so the screenshot doesn't take in any animation debris.
    time.sleep(0.65)

for w in range(14):
    print(map[w])

