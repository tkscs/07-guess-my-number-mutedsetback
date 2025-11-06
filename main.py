# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit

print("pick a number between 1 and 100.")
x = 1
y = 100
z = ""
while z != "correct":
    Programguess = (x + y) // 2
    print(f"My guess is: {Programguess}")
    z = input("Is it Correct, Higher, or Lower? ")
    if z == "higher":
            x = Programguess + 1
    elif z == "lower":
            y = Programguess - 1
print("I guessed your number")