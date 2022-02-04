print("A program that converts numbers ranging from 0 to 10^67 - 1 into words.\n"
      "Example: 3 -> three; 145 -> one hundred and forty-five")

words = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
         'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion',
         'quinquadecillion', 'sedecillion', 'septendecillion', 'octodecillion', 'novendecillion', 'vigintillion']  # number names after 999


def wordTransfer2(num):
    words2 = ''
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
    if len(num) == 1:words2 = nums[num][0]
    elif len(num) == 2:
        if num[0] + num[1] == '00':words2 = ''
        elif num[0] == '0':words2 = nums[num[1]][0]
        elif num[1] == '0':words2 = nums[num[0]][2]
        elif num[0] == '1':words2 = nums[num[1]][1]
        else:words2 = nums[num[0]][2] + '-' + nums[num[1]][0]
    elif len(num) == 3:
        if num[0] + num[1] + num[2] == '000':words2 = ''
        elif num[0] + num[1] == '00':words2 = nums[num[2]][0]
        elif num[0] == '0':
            if num[2] == '0':words2 = nums[num[1]][2]
            elif num[1] == '1':words2 = nums[num[2]][1]
            else:words2 = nums[num[1]][2] + '-' + nums[num[2]][0]
        elif num[1] + num[2] == '00':words2 = nums[num[0]][0] + ' hundred'
        elif num[1] == '0':words2 = nums[num[0]][0] + ' hundred and ' + nums[num[2]][0]
        elif num[2] == '0':words2 = nums[num[0]][0] + ' hundred and ' + nums[num[1]][2]
        elif num[1] == '1':words2 = nums[num[0]][0] + ' hundred and ' + nums[num[2]][1]
        else:words2 = nums[num[0]][0] + ' hundred and ' + nums[num[1]][2] + '-' + nums[num[2]][0]
    return words2


def wordTransfer(num):
    y = 0  # Check if the numbers starts with zeroes
    for x in range(len(num)):
        if num[x] == '0':
            y += 1
        else:
            break
    num = num[y:-1] + num[-1]

    if len(num) > 3*(len(words)):  # Check if the number is too big for the program to process
        input('Number is too big!')
        quit()
    # Convert the number into words using the array "words" to pull names like "thousand", "million",
    # "trillion", ... and string them together
    word = ''
    if len(num) % 3 != 0:  # make the lenght of the number a divisible of 3
        num = '0' * (3 - len(num) % 3) + num
    z =len(num) // 3
    for cdigit in range(z):
        cnums = wordTransfer2(num[-3-cdigit*3] + num[-2-cdigit*3] + num[-1-cdigit*3])
        if cnums != '':  # Check if it has to pull a word(it doesnt need to pull a word to name '000')
            if cdigit == 0 and 'hundred' not in cnums and cnums != '':
                word = ' and ' + cnums + ' ' + words[cdigit] + word
            else:
                word = ' ' + cnums + ' ' + words[cdigit] + word
    return word


input(wordTransfer(str(input())))
