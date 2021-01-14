import amino
import os
db_1=("1")
db_2=("2")
client = amino.Client()
email=input("Email: ")
password=input("Password: ")
client.login(email=email, password=password)
chatlink=input ("Chat Link: ")
chat=client.get_from_code(chatlink)
chatId=chat.objectId
comId=chat.path[1:chat.path.index('/')]
tranlink=input("Host Link or Chat Link or Your Profile Link: ")
tran=client.get_from_code(tranlink).objectId

def agin():
	coins=input ("Coins: ")
	subclient = amino.SubClient(comId=comId, profile=client.profile)
	try:
		subclient.send_coins(chatId=chatId,coins=coins,transactionId=tran)
		print ("Done Sending")
	except:
		print ("Faild Sending")
	print ("Agin?")
	print ("[1] Yes")
	print ("[2] No")
	u=input("choose: ")
	if u== db_1:
		agin()
	elif u== db_2:
		os._exit(1)
agin()
	