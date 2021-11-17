# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    if len(str(n)) != 1:
        new_n = 0
        for i in str(n):
            new_n += int(i)
        n = new_n
        return digital_root(n)
    else:
        return n

print(digital_root(16))
print(digital_root(942))