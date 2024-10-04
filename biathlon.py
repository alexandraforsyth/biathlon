from random import randint

targets = ["*", "*", "*", "*", "*"]
shotnr = 0

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n" + "              Biathlon" + "\n" + "\n" + "        a hit or miss game" + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n" "You got 5 shots" + "\n")

while shotnr<5:
    print ("1 2 3 4 5")
    print (targets[0], targets[1], targets[2], targets[3], targets[4])
    shotnr = shotnr+1
    shottargetinput = int(input(f"Shot nr {shotnr} at: "))
    if shottargetinput>5 or shottargetinput<1:
        print("You can only shoot between 1 and 5")
        shotnr = shotnr-1
    else:
        if targets[shottargetinput-1] == "*":
            if randint(0,1):
                targets[shottargetinput-1] = 0
                print("Hit on open target")
            else:
                print("Miss")
        else:
            if randint(0,1):
                print("Hit on closed target")
            else:
                print("Miss")
print ("1 2 3 4 5")
print (targets[0], targets[1], targets[2], targets[3], targets[4])
counthits = targets.count(0)
print("\n" + f"You hit {counthits} of 5 targets")