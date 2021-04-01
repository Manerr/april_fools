import os
import time



os.system("< color 17 & cls")

text="""
  __        __  _               _                           
  \ \      / / (_)  _ __     __| |   ___   __      __  ___    
   \ \ /\ / /  | | | '_ \   / _` |  / _ \  \ \ /\ / / / __|        ___             ___                           ___     __      __      __      __  
    \ V  V /   | | | | | | | (_| | | (_) |  \ V  V /  \__ \        |__      /\      |      /\     |             |__     |__)    |__)    /  \    |__) 
     \_/\_/    |_| |_| |_|  \__,_|  \___/    \_/\_/   |___/        |       /--\     |     /--\    |___          |___    |  \    |  \    \__/    |  \ 

"""

text.replace("|","^|")


print(text)


bill="""

You have used Linux this night.

You'll never recover your session...

Bill Gates hopes that you'll enjoy using in a loong long time Windows again, beacuse it's end, now...


"""


for i in bill:
  print(i,end="")
  time.sleep(.01)
  print("\b "+i,end="")
  time.sleep(.01)

input("\n\nPress enter to quit this shell...")


percent=0

while percent<100:
  print(f"SYSTEM: Destroying {percent}% \a")
  time.sleep(.2)
  percent+=2.5

print("\n"*100)

for nothing in range(5):
  os.system("color")
  for i in range(1,15):
    os.system(f"color 0{i}")

