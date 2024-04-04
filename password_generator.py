import string
import random

def password_generator(length):
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.digits)

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(length * (30 / 100))
    part2 = round(length * (20 / 100))

    result = []


    for i in range(part1):
        result.append(s1[i])
        result.append(s2[i])


    for i in range(part2):
        result.append(s3[i])
        result.append(s4[i])

    random.shuffle(result)
    password = ''.join(result)
    print(password)
    return password

if __name__ == '__main__':
    password_generator(10)