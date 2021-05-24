#Variables
row = 0
hexList = []
rgbVal = ""
message = ""
finalMessage = ""

#Open file
file = open('image1.html', 'r')
myArray = file.readlines()

#Splits the file into lines that contain hex values and appends to hexList
for line in myArray:
    bits = line.split()
    for item in bits:
        if item[0] == "#":
            hexList.append(item[1:7])

#Obtains the 3 LSB bits for the RGB values
for i in range(len(hexList)):
    binaryStr = (bin(int(hexList[i], 16))[2:])
    rgbVal += binaryStr[7] + binaryStr[15] + binaryStr[-1]

#Finds the length of the message(First 32 bits)
msgLength = rgbVal[0:33]
msgLength = msgLength[::-1]
msgLength = int(msgLength, 2)
print("The length of the message is: " + str(msgLength))

#Calculate the message from here
msgString = (rgbVal[32:])
word = ""
for letter in msgString:
    if len(word) != 8:
        word += letter
    else:
        #Reverse word, convert to binary, then to ascii
        word = word[::-1]
        word = int(word, 2)
        word = chr(word)
        message += word
        word = letter
finalMessage = message[0:msgLength]

#Check for possible values and calculates the percentage
check = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
checkCount = 0
for letter in finalMessage:
    if letter in check:
        checkCount += 1
percentage = checkCount/len(finalMessage) * 100

print("The final message is: " + finalMessage)
print("The percentage of total possible values containing the message is: " + str(round(percentage, 2))+ "%")