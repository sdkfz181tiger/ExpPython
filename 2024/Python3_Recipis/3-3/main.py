# coding: utf-8

"""
関数の引数
"""

#==========
# Main

def main():
    print("main!!")

    # 位置引数
    sample_func_a("spam", "ham", "egg")

    # キーワード引数
    sample_func_a(param3="punch", param2="kick", param1="chop")


# 位置引数, キーワード引数
def sample_func_a(param1, param2, param3):
    print(f'{param1}, {param2}, {param3}')

# キーワード引数


if __name__ == "__main__":
    main()
