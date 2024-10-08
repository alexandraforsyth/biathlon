from random import randint

open = 0
closed = 1

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon"+ "\n")
    print("        a hit or miss game" + "\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return None

def is_open(target):
    return target == open

def is_closed(target):
    return target == closed

def new_targets():
    return [open, open, open, open, open]

def close_target(targets_list, index):
    targets_list[index] = closed
    return targets_list

def points(target_list):
    return target_list.count(closed)

def targets_to_string(target_list):
    string = ""
    for i in target_list:
        if is_closed(i):
            string += "* "
        elif is_open(i):
            string += "0 "
    return string

def view_targets(target_list):
    print("1 2 3 4 5")
    print(targets_to_string(target_list))
    return None

def random_hit():
    if randint(0,1) == 1:
        return True
    else:
        return False
    
def shoot(target_list, index):
    if random_hit and is_open(target_list, index-1):
        close_target(target_list, index-1)
        return "Hit on open target"
    elif is_closed(target_list, index-1) :
        return "Hit on closed target"
    else: 
        return "Miss"

def game():
    splash
    targets = new_targets()
    for _ in range(1,5):
        print(view_targets(targets))
        shoot(targets, int(input("Sikta på")))

