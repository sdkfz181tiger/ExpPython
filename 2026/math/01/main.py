# coding: utf-8

"""
Pythonで高校数学
"""

CHARS_HEX = ["0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F"]

def dec2bin(num:int)->str:
    """ 10進数 -> 2進数 """
    result = []
    while num != 0:
        odd = num % 2
        result.append(str(odd))
        num = num // 2
    result.reverse()
    return "".join(result)

def dec2hex(num:int)->str:
    """ 10進数 -> 16進数 """
    result = []
    while num != 0:
        odd = num % 16
        result.append(CHARS_HEX[odd])
        num = num // 16
    result.reverse()
    return "".join(result)

def bin2dec(text:str)->int:
    """ 2進数 -> 10進数 """
    result = 0
    for i in range(len(text)):
        num = int(text[i])
        result += num * 2 ** (len(text)-i-1)
    return result

def bin2hex(text:str)->str:
    """ 2進数 -> 16進数 """
    result = []
    size = len(text)
    offset = 4
    for i in range(0, size, offset):
        t = size - i
        f = max(t-offset, 0)
        num = bin2dec(text[f:t])
        result.append(CHARS_HEX[num])
    result.reverse()
    return "".join(result)

def main():
    """ メイン処理 """
    
    result = dec2bin(26)
    print("dec2bin:", result)

    result = dec2hex(26)
    print("dec2hex:", result)

    result = bin2dec("10111110000")
    print("bin2dec:", result)

    result = bin2hex("10111110000")
    print("bin2hex:", result)

if __name__ == "__main__":
    main()