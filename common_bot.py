from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random, requests
import time, datetime
import vk_api, vk
from vk_api.utils import get_random_id
from vk_api.upload import VkUpload

def write_msg(chat_id, message):
    vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': get_random_id()})

group_id = '<write_your_group_id(address)_here' #e.g if group address is https://vk.com/club0000001 you should write: group_id = '0000001'
token = '<write_your_token_here'
vk = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk, group_id, wait=20)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
                if 'hello' in str(event):
                    try:
                        write_msg(event.chat_id, 'goodbye')
                    except:
                        write_msg(event.chat_id, 'error')                        
                elif 'send picture' in str(event):
                    try:
                        a = vk.method("photos.getMessagesUploadServer")
                        b = requests.post(a['upload_url'], files={'photo': open('picture.jpg', 'rb')}).json()
                        c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                        d = "photo{}_{}".format(c["owner_id"], c["id"])
                        vk.method("messages.send", {"chat_id": event.chat_id, "message": "", "attachment": d, "random_id": 0})
                        write_msg(event.chat_id, 'please')
                    except:
                        write_msg(event.chat_id, 'Error 404')
                        
                   





                    
                    
