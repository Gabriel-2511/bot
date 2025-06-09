import random

def gen_pass(pass_length):
    elements = ".,:;[]<>+-/*!&$%#()?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
