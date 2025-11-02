#石头剪刀布
#1=石头 2=剪刀 3=布
import sys
import random
while True:
	computer=random.randint(1,3)
	if computer==(1):
		computer=("石头")
	elif computer==(2):
		computer=("剪刀")
	elif computer==(3):
		computer=("布")
#用随机数获得电脑的输出结果

	user=input("石头 剪刀还是布？\n")
	if user==computer:
		print(f"\n我们都出了{user} 平局")
	elif (user=="石头"and 						computer=="剪刀")or \
		(user=="剪刀"and computer=="布")or \
		(user=="布"and computer=="石头"):
		print(f"\n你赢了 我出的是{computer}")
	else:
		print(f"\n老兄你输了我出的是{computer}")
	play_again=input("老兄你还要玩吗\n是的(点击y     退出(点击n)")
	if play_again=="n":
		print("欢迎再来玩呀 老兄")
		sys.exit()
	if play_again=="y":
		print("\n好的老兄")