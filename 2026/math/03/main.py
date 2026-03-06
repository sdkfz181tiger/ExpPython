# coding: utf-8

"""
Pythonで高校数学
"""

CHARS_HEX = ["0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F"]

def dec2bin(num:int, digits:int)->list[int]:
    """ 10進数 -> 2進数 """
    result = [0] * digits
    if 0 <= num:
        i = 0
        while num != 0:
            odd = num % 2
            num = num // 2
            result[i] = odd
            i += 1
        result.reverse()
    else:
        result = dec2bin(abs(num), digits)
        # Flip
        for i in range(digits):
            result[i] ^= 1 # XOR
        # Add 1
        carry = 1 # Carry
        for i in range(digits):
            d = digits - i - 1
            if carry == 1 and result[d] == 1:
                result[d] = 0
                carry = 1
            else:
                result[d] = 1 if carry != result[d] else 0
                carry = 0
    return result

def main():
    """ メイン処理 """
    
    result = dec2bin(-64, digits=8)
    print("dec2bin:", result)

if __name__ == "__main__":
    main()