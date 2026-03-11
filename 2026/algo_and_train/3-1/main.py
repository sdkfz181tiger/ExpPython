# coding: utf-8

"""
アルトレ第二版
3.1: 成績評価を行う
"""

def grade_evaluation(in_data):
    e_result = None
    if 80 <= in_data:
        e_result = "評価A"
    elif 60 <= in_data:
        e_result = "評価B"
    else:
        e_result = "評価C"
    return e_result

def main():
    """ メイン処理 """
    print("Test01:", grade_evaluation(85))
    print("Test02:", grade_evaluation(70))

if __name__ == "__main__":
    main()