# cipher to encrypt conversion using python

def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char = text[i]

        # to encrypt the uppercase characters

        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26 +65)

        # to encrypt lowercase characters

        else:
            result+=chr((ord(char)+s-97)%26+97)

    return result

text = input("Enter your text: ")

s= int(input("Enter your number in which you want to Add: "))

print(encrypt(text,s))