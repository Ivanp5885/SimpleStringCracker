import string
import time

char = list(string.ascii_letters + string.digits + " ")
print(char)

pw = input("Enter password:\n")
length = len(pw)
print("Password length:", length)

pwguess = ""

for xpos in range(length):
    for y in range(len(char)):
        pwguess_try = pwguess + str(char[y])
        print("Trying:", pwguess_try)
        time.sleep(0.02)

        if pwguess_try[xpos] == pw[xpos]:
            pwguess = pwguess_try
            print("Correct!")
            break

print("Password guessed:", pwguess)
