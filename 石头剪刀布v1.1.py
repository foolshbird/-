#石头剪刀布
#1=石头 2=剪刀 3=布
import sys
import random
computer_lie=["石头","剪刀","布"]
while True:
	computer_number=random.randint(1,3)
	computer_chose=computer_lie[computer_number-1]

	user=input("石头 剪刀还是布？\n")
	if user==computer_chose:
		print(f"\n我们都出了{user} 平局")
	elif (user=="石头"and 						computer_chose=="剪刀")or \
		(user=="剪刀"and computer_chose=="布")or \
		(user=="布"and computer_chose=="石头"):
		print(f"\n你赢了 我出的是{computer_chose}")
	else:
		print(f"\n老兄你输了我出的是{computer_chose}")
	play_again=input("老兄你还要玩吗\n是的(点击y     退出(点击n)")
	if play_again=="n":
		print("欢迎再来玩呀 老兄")
		sys.exit()
	if play_again=="y":
		print("\n好的老兄")