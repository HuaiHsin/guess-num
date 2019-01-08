import random

times = 0
print("猜數字遊戲，先決定數字範圍吧～")
min_num = input("請先輸入最小數字： ")
max_num = input("請先輸入最大數字： ")
num = random.randint(int(min_num), int(max_num))

while True:
    guess_num = int(input("請輸入"+ min_num+ "~"+ max_num+ "之間的數字： "))
    if guess_num > int(max_num) or guess_num < int(min_num):
        print("超出數字範圍囉～數字介於",min_num,"和",max_num,"之間")
    elif guess_num > num:
        print("猜錯囉！你的數字比答案大")
        times+=1
    elif guess_num < num:
        print("猜錯囉！你的數字比答案小")
        times+=1
    else:
        print("終於猜對了！")
        times+=1
        print("你總共猜了", times, " 次呢")
        break
