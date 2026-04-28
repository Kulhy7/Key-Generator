# Made by Luboš Kulhan | alias Adam Kaiser
# Example: aG58-Bsww-12sF-55Fn

import random

def reg_key_gen():
    god_list = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'A', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', '2', '3', '4', '5', '6', '7', '9']
    gen_list = []
    i = 0
    while i < 19:
        i += 1
        if i == 5 or i == 10 or i == 15:
            gen_list.append('-')
        else:
            gen_list.append(random.choice(god_list))
    reg_key = "".join(gen_list)
    print("Your registration key: " + reg_key)
