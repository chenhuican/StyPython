#-*- coding:utf-8 -*-
import random
import itchat
import time
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
bless_list = [u'嘻嘻',u'哈哈',u'其实我是个聊天机器人',u'你吃饭了没',u'周末有空一起去看电影不？',
             u'你说啥']

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	return handle_text_msg(msg)

def handle_text_msg(msg):
	if u'在干嘛' in msg['Text']:
		return random.choice(bless_list)
	else:
		return random.choice(bless_list)

def qunfa(chatroomName,text):
	itchat.get_chatrooms(update=True)
	chatrooms = itchat.search_chatrooms(name=chatroomName)
	if chatrooms is None:
		print(u'没有找到群聊:' + chatroomName)
	else:
		chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
		for friend in chatroom['MemberList']:
			friend = itchat.search_friends(userName = friend['UserName'])
			itchat.send(text %(friend['DisplayName'] or friend['NickName']), friend['UserName'])
			time.sleep(3)

if __name__ == '__main__':
	itchat.auto_login(hotReload=True)
	qunfa('TE','Hi %s 哈哈，我不会告诉你其实我是个聊天机器人...')
	itchat.run()