#Coded By Dark Slad3
#A Product Of ToxicNoob

import os
import time
import sys

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

print("\033[92m")
os.system("clear")
time.sleep(0.8)
os.system("figlet ToxicNoob")
print("\033[3;90m  		      Security Is An Illusion \033[0;92m")
print("\n")
time.sleep(0.6)
psb("\n[!] Loading...")
time.sleep(0.8)
psb("\n[!] Please Wait.....")
time.sleep(1)


import sys
import time
import os

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)

def logo():
	os.system("clear")
	print("\033[92m")
	logopsb(" _____ ____                           \n|_   _/ ___| __ _ _ __ ___   ___  ___ \n  | || |  _ / _` | '_ ` _ \ / _ \/ __|\n  | || |_| | (_| | | | | | |  __/\__ \ \n  |_| \____|\__,_|_| |_| |_|\___||___/\n                                      ")
	logopsb("			A Product Of ToxicNoob")
	time.sleep(0.5)
	print
	logopsb("\033[34m\n|****************************************************| \n|\033[3m Author   : DarkSlad3                               \033[0;34m|\n|\033[3m Tool     : Termux Games                            \033[0;34m|\n|\033[3m Version  : 1.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : DarkSlad3        		     	     \033[0;34m|\n|\033[3m Note     : Add Termux Extra Keys Before Playing    \033[0;34m|\n******************************************************")
	print("\033[3;92m")
	time.sleep(0.6)

logo()
print("[01] Install PacMan Game.")
print("[02] Install Tetris Game.")
print("[03] Install Moon-Buggy Game.")
print("[04] Install nInvaders Game.")
print("[05] Install Snake Game.")
print("[06] Install Greed Game.")
print("[07] Install Nethack Game.")
print("[08] Install Sudoku Game.")
print("[09] Install All Games Together.")
print("[10] Details About The Games.")
print("[11] Add Extra Termux Keys.")
print("[12] Exit Program.")
time.sleep(0.7)

op = input("\n\n[*] Enter Your Choice:> ")

if(op==""):
 print("\033[31m\n[*] Please Select an Option.....")
 time.sleep(1)
 os.system("python Tgames.py")

elif(op=="1"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install pacman4console > /dev/null 2>&1")
 print("\033[92m")
 psb("\n[*] PacMan Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type pacman in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="2"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install bastet > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Tetris Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type bastet in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="3"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install moon-buggy > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Moon-Buggy Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type moon-buggy in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="4"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install ninvaders > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] nInvaders Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type ninvaders in the Terminal...\033[0;37m")
 print
 time.sleep(0.8)
 exit()


elif(op=="5"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install nsnake > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Snake Game Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type nsnake in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="6"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install greed > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Greed Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type greed in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="7"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install nethack > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Nethack Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type nethack in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="8"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install nudoku > /dev/null 2>&1 && apt install nudoku > /dev/null 2>&1")
 print("\033[92m\n")
 psb("[*] Sudoku Installed Successfully...")
 print("\n")
 time.sleep(0.8)
 psb("[*] To Play The Game, Type nudoku in the Terminal...\033[0;37m")
 print("\n")
 time.sleep(0.8)
 exit()


elif(op=="9"):
 psb("[*] Please Wait Some Time....")
 os.system("pkg install pacman4console bastet moon-buggy ninvaders nsnake greed nudoku > /dev/null 2>&1 && apt install nudoku > /dev/null 2>&1")
 print("\033[92m\n")
 psb("All Games Installed Successfully....")
 print("\n")
 psb("For playing The Games....")
 print("\n")
 psb("[*] Type pacman to play PacMan")
 time.sleep(0.4)
 psb("[*] Type bastet to play Tetris")
 time.sleep(0.4)
 psb("[*] Type moon-buggy to play Moon-Buggy")
 time.sleep(0.4)
 psb("[*] Type ninvaders to play nInvaders")
 time.sleep(0.4)
 psb("[*] Type nsnake to play Snake Game")
 time.sleep(0.4)
 psb("[*] Type greed to play Greed")
 time.sleep(0.4)
 psb("[*] Type nethack to play Nethack")
 time.sleep(0.4)
 psb("[*] Type nudoku to play Sudoku")
 time.sleep(0.7)
 print("\n")
 psb("[!] Enjoy.....\033[0;37m")
 print("\n")
 time.sleep(1)
 exit()


elif(op=="10"):
 os.system("clear")
 print("\033[0;92m")
 os.system("figlet Details")
 print("\n")
 psb("\n\033[3;92m[#] Details About The Games are Below...\n")
 time.sleep(1)
 psb("\n[01] PacMan Details:\n")
 time.sleep(0.8)
 psb("[*] PacMan is a Maze Arcade game.")
 time.sleep(0.6)
 psb("[*] Size : 152 KB")
 time.sleep(0.8)
 psb("\n[02] Tetris Details:\n")
 time.sleep(0.8)
 psb("[*] Tetris is a Tile matching puzzle game.")
 time.sleep(0.6)
 psb("[*] Size : 471 KB")
 time.sleep(0.8)
 psb("\n[03] Moon-Buggy Details:\n")
 time.sleep(0.8)
 psb("[*] Moon-Buggy is a Stable game in termux.")
 time.sleep(0.6)
 psb("[*] Size : 131KB")
 time.sleep(0.8)
 psb("\n[04] nInvaders Details:\n")
 time.sleep(0.8)
 psb("[*] nInvaders is A terminal version of Space-Invaders where you can shoot bullets with space-bar and move in the X-axis.")
 time.sleep(0.6)
 psb("[*] Size : 90KB")
 time.sleep(0.8)
 psb("\n[05] Snake Game Details:\n")
 time.sleep(0.8)
 psb("[*] We all Remember and Know about The Snake Game.")
 time.sleep(0.6)
 psb("[*] Size : 90KB")
 time.sleep(0.8)
 psb("\n[06] Greed Details:\n")
 time.sleep(0.8)
 psb("[*] In Greed You have to Erase as Numbers as possible.")
 time.sleep(0.6)
 psb("[*] Press P to find out all the possible moves.")
 time.sleep(0.6)
 psb("[*] Press Q and then y to Quit the game.")
 time.sleep(0.6)
 psb("[*] Press ? on your keyboard to Read all the details about the game.")
 time.sleep(0.6)
 psb("[*] Size :70KB")
 time.sleep(0.8)
 psb("\n[07] Nethack Details:\n")
 time.sleep(0.8)
 psb("[*] NetHack is a single-player dungeon exploration game.")
 time.sleep(0.6)
 psb("[*] Size : 7466KB")
 time.sleep(0.8)
 psb("\n[08] Sudoku Details:\n")
 time.sleep(0.8)
 psb("[*] Sudoku is a Logic-based game where we have to put unique numbers in the 9X9 grid and it should not have same number in the same column and row.")
 time.sleep(0.6)
 psb("[*] Size : 7KB")
 time.sleep(1)
 psb("\n[*] Thanks You......\n\033[0;37m")
 time.sleep(1)


elif(op=="11"):
 print("\033[0;37m")
 time.sleep(0.5)
 os.system("git clone https://github.com/toxicnoobs/Tkey > /dev/null 2>&1")
 os.system("cd Tkey && python2 key.py && python2 key.py")
 os.system("cd ..")
 os.system("rm -rf Tkey")
 os.system("clear")
 print("\033[92m")
 logo()
 print("[*] Termux Extra Keys Added Successfully....\033[0;37m")
 time.sleep(1)
 os.system("python Tgames.py")


elif(op=="12"):
 print("\033[31m\n[!] Have A Nice Day....\n\033[0;37;40m")
 time.sleep(0.7)
 exit()
