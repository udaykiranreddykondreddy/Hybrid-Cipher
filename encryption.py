import random
#assign values to every character
values={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '1', 53: '2', 54: '3', 55: '4', 56: '5', 57: '6', 58: '7', 59: '8', 60: '9', 61: '0', 62: '!', 63: '@', 64: '#', 65: '$', 66: '%', 67: '^', 68: '&', 69: '*', 70: '(', 71: ')', 72: '-', 73: '_', 74: '=', 75: '+', 76: '[', 77: ']', 78: '{', 79: '}', 80: ';', 81: ':', 82: "'", 83: '"', 84: '|', 85: ',', 86: '.', 87: '/', 88: '<', 89: '>', 90: '?', 91: '~', 92: '`', 93: ' '}
values1={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51, '1': 52, '2': 53, '3': 54, '4': 55, '5': 56, '6': 57, '7': 58, '8': 59, '9': 60, '0': 61, '!': 62, '@': 63, '#': 64, '$': 65, '%': 66, '^': 67, '&': 68, '*': 69, '(': 70, ')': 71, '-': 72, '_': 73, '=': 74, '+': 75, '[': 76, ']': 77, '{': 78, '}': 79, ';': 80, ':': 81, "'": 82, '"': 83, '|': 84, ',': 85, '.': 86, '/': 87, '<': 88, '>': 89, '?': 90, '~': 91, '`': 92, ' ': 93}
message=input("just enter message  : ")        #input of message to encrypt                                               
k=len(message)//2                              #calculating the k value to generate random key                
keylength=random.randrange(k,len(message))     #Generating the keylegth randomly
alphaascii,key=list(range(94)),[]
for i in range(keylength):
    random.shuffle(alphaascii)
    key.append(values[alphaascii[0]])          #generating random key of k charecteres
#print("key is : ",end='')                     #printing the key
#print(key)
print("key length is %d "%(keylength))        #printing the key length  
j,cipher1=len(key)-1,[]
for i in range(len(message)):                 #performing substitution operation with reverse key 
    if(j==-1):
        j=len(key)-1
    cipher1.append(values[((values1[message[i]]-values1[key[j]])%94)])
    j-=1
cipher1=cipher1+key                            #concatinating the message and key
#print("Cipher text after XOR : ",end='')
#print("".join(cipher1))
a,b,j=1,1,11
while(j):                                     #performing Fibonacci series
    for i in range(len(cipher1)):
        if(i%2==0):
            num=values1[cipher1[i]]+a
            if(num>93):
                num=num-94
        else:
            num=values1[cipher1[i]]-a
            if(num<0):
                num=num+94
        cipher1[i]=values[num]
    a,b=b,a+b	
    j-=1
keysize=len(str(keylength))
cipher1.append(str(keylength))
cipher1.append(values[keysize])
print("Final Cipher message is : ",end='')
print("".join(cipher1))                       #final cipher message
