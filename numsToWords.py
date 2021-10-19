#
# This program converts integers ranging from 0-10^33-1 into words(ex. 2 - two, 35 - thirty five, 79 - seventy nine...)
#

def wordTransfer2(num):
    words = ''
    nums = {
        '0': ['zero'],
        '1': ['one', 'eleven', 'ten'],
        '2': ['two', 'twelve', 'twenty'],
        '3': ['three', 'thirteen', 'thirty'],
        '4': ['four', 'fourteen', 'forty'],
        '5': ['five', 'fifteen', 'fifty'],
        '6': ['six', 'sixteen', 'sixty'],
        '7': ['seven', 'seventeen', 'seventy'],
        '8': ['eight', 'eighteen', 'eighty'],
        '9': ['nine', 'nineteen', 'ninety']
    }
    if len(num) == 1:words = nums[num][0]
    elif len(num) == 2:
        if num[0] + num[1] == '00':words = ''
        elif num[0] == '0':words = nums[num[1]][0]
        elif num[1] == '0':words = nums[num[0]][2]
        elif num[0] == '1':words = nums[num[1]][1]
        else:words = nums[num[0]][2] + '-' + nums[num[1]][0]
    elif len(num) == 3:
        if num[0] + num[1] + num[2] == '000':words = ''
        elif num[0] + num[1] == '00':words = nums[num[2]][0]
        elif num[0] == '0':
            if num[2] == '0':words = nums[num[1]][2]
            elif num[1] == '1':words = nums[num[2]][1]
            else:words = nums[num[1]][2] + '-' + nums[num[2]][0]
        elif num[1] + num[2] == '00':words = nums[num[0]][0] + ' hundred'
        elif num[1] == '0':words = nums[num[0]][0] + ' hundred and ' + nums[num[2]][0]
        elif num[2] == '0':words = nums[num[0]][0] + ' hundred and ' + nums[num[1]][2]
        elif num[1] == '1':words = nums[num[0]][0] + ' hundred and ' + nums[num[2]][1]
        else:words = nums[num[0]][0] + ' hundred and ' + nums[num[1]][2] + '-' + nums[num[2]][0]
    return words


def wordTransfer(num):
    y = 0
    for x in range(len(num)):
        if num[x] == '0':
            y += 1
        else:
            break
    num = num[y:-1] + num[-1]
    if len(num) > 33:
        input('Number is too big!')
        quit()
    word = ''
    if len(num) % 3 != 0:
        num = '0' * (3 - len(num) % 3) + num
    words = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion'
             'septillion', 'octillion', 'nonillion', 'decillion']
    for cdigit in range(len(num) // 3):
        cnums = wordTransfer2(num[-3-cdigit*3] + num[-2-cdigit*3] + num[-1-cdigit*3])
        word = ' ' + cnums + ' ' + words[cdigit] + word
    return word


print(wordTransfer(str(input())))
