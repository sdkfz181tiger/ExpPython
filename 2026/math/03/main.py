# coding: utf-8

"""
Pythonで高校数学
"""

DIGITS = 8

CHARS = ["0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F"]

def dec2bin(num:int)->list[int]:
    result = [0] * DIGITS

    # Positive
    if 0 < num:
        for i in range(DIGITS):
            odd = num % 2
            num = num // 2
            result[i] = odd
        result.reverse()
        return result

    # Negative
    result = dec2bin(abs(num))
    result = flip_bit(result)
    result = add_one(result)
    return result

def flip_bit(arr:list[int])->list[int]:
    for i in range(DIGITS):
        arr[i] = arr[i] ^ 1
    return arr

def add_one(arr:list[int])->list[int]:
    carry = 1 # Carry
    for i in range(DIGITS):
        d = DIGITS - i - 1
        if carry == 1 and arr[d] == 1:
            arr[d] = 0
            carry = 1
        else:
            arr[d] = 1 if carry != arr[d] else 0
            carry = 0
    return arr

def main():
    """ メイン処理 """

    result = dec2bin(28)
    print("result:", result)

    result = dec2bin(-28)
    print("result:", result)


if __name__ == "__main__":
    main()