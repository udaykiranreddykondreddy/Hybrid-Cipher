import random, sys

class Decryption():
    def __init__(self,parameters):
        #assign char_to_int_assign to every character
        self.char_to_int_assign={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '1', 53: '2', 54: '3', 55: '4', 56: '5', 57: '6', 58: '7', 59: '8', 60: '9', 61: '0', 62: '!', 63: '@', 64: '#', 65: '$', 66: '%', 67: '^', 68: '&', 69: '*', 70: '(', 71: ')', 72: '-', 73: '_', 74: '=', 75: '+', 76: '[', 77: ']', 78: '{', 79: '}', 80: ';', 81: ':', 82: "'", 83: '"', 84: '|', 85: ',', 86: '.', 87: '/', 88: '<', 89: '>', 90: '?', 91: '~', 92: '`', 93: ' '}
        self.int_to_char_assign={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51, '1': 52, '2': 53, '3': 54, '4': 55, '5': 56, '6': 57, '7': 58, '8': 59, '9': 60, '0': 61, '!': 62, '@': 63, '#': 64, '$': 65, '%': 66, '^': 67, '&': 68, '*': 69, '(': 70, ')': 71, '-': 72, '_': 73, '=': 74, '+': 75, '[': 76, ']': 77, '{': 78, '}': 79, ';': 80, ':': 81, "'": 82, '"': 83, '|': 84, ',': 85, '.': 86, '/': 87, '<': 88, '>': 89, '?': 90, '~': 91, '`': 92, ' ': 93}
        self.message = parameters.get("message")
        self.message=[x for x in self.message]

    def exract_key_from_cipher(self):
        self.key_length=self.message[-1]
        del self.message[-1]
        self.key_size_length=len(self.message)-self.int_to_char_assign[self.key_length]
        self.key=self.message[self.key_size_length:]
        del self.message[self.key_size_length:]
        k=int("".join(self.key))
        self.key=self.message[len(self.message)-k:]
        del self.message[len(self.message)-k:]

    def decrypt_message(self):
        first_fib_num,second_fib_num,fib_upto=1,1,11
        while(fib_upto):                   #performing fibonacci series
            for i in range(len(self.message)):
                if(i%2==0):
                    num=self.int_to_char_assign[self.message[i]]-first_fib_num
                    if(num<0):
                        num=num+94
                else:
                    num=self.int_to_char_assign[self.message[i]]+first_fib_num
                    if(num>93):
                        num=num-94
                self.message[i]=self.char_to_int_assign[num]
            first_fib_num,second_fib_num=second_fib_num,first_fib_num+second_fib_num
            fib_upto-=1

        self.exract_key_from_cipher()

        j,self.plane_text=len(self.key)-1,[]
        for i in range(len(self.message)):      #performing the substitution operation
            if(j==-1):
                j=len(self.key)-1
            self.plane_text.append(self.char_to_int_assign[((self.int_to_char_assign[self.key[j]]+self.int_to_char_assign[self.message[i]])%94)])
            j-=1
        return "".join(self.plane_text)          #final plane text'''

if __name__ == "__main__":
    message = input("enter message : ")
    parameters = {"message" : message}
    obj = Decryption(parameters)
    plain_text = obj.decrypt_message()
    print("plain text is ")
    print(plain_text)
