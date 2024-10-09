from random import randint
import math

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

def parse_target(position):
    if len(position) == 1:
        index = int(position) - 1
        if  -1< index < 5:
            return index
    

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

def random_hit():
    return randint(0,1)
        
    
def shoot(target_list, index):
    if is_open(target_list[index]) :
        if random_hit():
            close_target(target_list, index)
            print("Hit on open target")
        else: 
            print("Miss")
        
    elif is_closed(target_list[index]):
        print("Hit on closed target")
    
    
    return

def game():
    splash()
    targets = new_targets()
    for _ in range(0,5):
        view_targets(targets)
        user_input = parse_target(input("Sikta på "))
        if 0>user_input>4
            print("Du måste skjuta mellan 1-5")
            user_input = parse_target(input("Sikta på "))
        shoot(targets, user_input)
    view_targets(targets)
    print(f"Snyggt, du träffade {points(targets)} targets")

