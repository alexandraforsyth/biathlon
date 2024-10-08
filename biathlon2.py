from random import randint

open = 0
closed = 1

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon"+ "\n")
    print("        a hit or miss game" + "\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #rspla+ "\n" "You got 5 shots" + "\n")
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
            string += " *"
        elif is_open(i):
            string += " 0"

    return string

def game():
    splash
