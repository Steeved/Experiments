import random
import sys
import random
def InStrRandInt():
  return str(round(random.randint(-10000, 10000)))
def getName(sysargv):
   return str(sysargv[1])
file = open("attr.mcfunction", "a")
file.write('give @a diamond_helmet{AttributeModifiers:[')
for b in range(int(sys.argv[4])) :
    str1 = '{Operation:1,UUIDLeast:'+InStrRandInt()+',UUIDMost:'+InStrRandInt()+\
    ',AttributeName:' + getName(sys.argv)+',Name:'+str(sys.argv[2])\
    +',Amount:'+str(sys.argv[3])+'},'
    file.write(str1)
file.write(']} 1')
file.close()
#test