import string

char = list(string.ascii_letters + string.digits)
print(char)
print(char[2])

y=0
pw = ""
pwguess = ""
print("Hello World")
pw = input("pass?\n")
lenght = len(pw)
print(lenght)
xpos = 0

while pw !=pwguess:
    pwguess=pwguess+str(char[xpos])
    if pwguess[xpos] != pw[xpos]:
        pwguess = pwguess[:-1] + str(char[y])
        y=y+1
        print(pwguess)
    else:
        xpos= xpos + 1
