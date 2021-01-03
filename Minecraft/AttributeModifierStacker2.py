import random
import sys
import random
k = []
print("UCV's Minecraft Attribute Modifier Stacker\n Format for writing attributes to a datapack function: \n 1. The attributes' 'attributeName' tag. \n 2. The attributes' 'Name' tag. \n 3. The attributes' 'Amount' tag. \n 4. The number of attributes you want to write. \n 5. Either 'start_only', 'end_only', 'continue_only' or 'finished', depending on what you want to do with your function.")
print(" If you want to start writing attributes and dont want to write any more, write 'finished' in the fifth argument. \n If you want to start a function but write more attributes from a different type, write 'start_only' in the last argument and open this program again to finish it. \n If you have already begun a function and want to finish it, write 'end_only' in the last argument. /n If you have already begun a function, want to add more attributes, but don't want to finish it yet, write 'continue_only' and start the program again to add more attributes.")
print(" If you want to make the attribute 'Amount' tag infinity just write 1E99999999 in the third argument(you just need to have a big number after the '1E' bigger than 309).")
print(" This program writes attributes in a Minecraft Datapack Function. You can learn how Minecraft Functions work at https://minecraft.gamepedia.com/Function_(Java_Edition)")
print(" The functions written by this program can be pasted into your Minecraft world's datapack functions folder. That way they can be used ingame to give you your custom weapons. This only works if the world is on version Release 1.13 - 1.15.2!!!")
print(" With this program you can write attributes only from one type. You cannot write more than one type in a single run. You will have to leave the function unfinished and start again adding attributes from other types and then finish it.")
k.append(input("1. AttributeName: "))
k.append(input("2. Name: "))
k.append(input("3.Amount: "))
k.append(input("4.Number of attributes: "))
k.append(input("5.Start new function|end old function|continue old function"))
def InStrRandInt():
  return str(round(random.randint(-10000, 10000)))
filename = str(input("Function Name: "))+".mcfunction"
file = open(filename, "a")
if k[4] == "start_only" or k[4] == "finished" :
    file.write('give @a diamond_helmet{AttributeModifiers:[')
for b in range(int(k[3])) :
    str1 = '{Operation:1,UUIDLeast:'+InStrRandInt()+',UUIDMost:'+InStrRandInt()+',AttributeName:'+str(k[0])+',Name:'+str(k[1])+',Amount:'+str(k[2])+'d},'
    file.write(str1)
if k[4] == "end_only" or k[4] == "finished" :
    file.write(']} 1')
file.close()