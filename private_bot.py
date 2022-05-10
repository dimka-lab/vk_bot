import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import requests
import time
import datetime
from threading import Thread

t1me = datetime.datetime.today().strftime("%H:%M")
t_end = time.time() + 2
#def for writing messages from bot to user:
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)})
#def to schedule write "Good night" at 22:23 every day
def scheduler():
    while time.time() < t_end:
        if t1me == '22:23':
            try:
                write_msg(event.user_id, 'Good night')
                print('ok')
            except:
                print('error')

t = Thread(target=scheduler)
t.start()

token = '<write_your_token_here>'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text 
            if request == 'hi':
                write_msg(event.user_id, 'hi, man!')              
            elif request == 'send picture':
                a = vk.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('picture.jpg', 'rb')}).json()
                c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk.method("messages.send", {"peer_id": event.user_id, "message": "", "attachment": d, "random_id": 0})
            elif request == 'time':
                a = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
                write_msg(event.user_id, a)
  

  
