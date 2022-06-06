# vk_bot
# Chat Bot for social media vk
Usage example:
![Example](https://github.com/rus121/vk_bot/blob/main/example.gif)
- **private_bot.py** script can send only private messages 
- **common_bot.py** this script send messages in the common chats(беседах) only
## Requirements:
- Python3
- Systemd to run unit
- To interact with the bot, you need a group on the VK social network and access to it - a token with all the necessary permissions
- Common_bot: you need to join community in your chat, also to send and take messages in the chats the admin of the conversation should give the bot full access to the conversation or mention the community like @club012345 or @community_name every time  it's needed
- Private_bot: to begin the communication it's recommended to push button "Начать", without it bot will not be able to interact with the user
## Using
Download the script as user 'user'
```bash
su - user 
```
```bash
git clone https://github.com/rus121/vk_bot.git | cd vk_bot
```
Make sure the python binaries are in /usr/bin/python3 as usual e.g in ubuntu 
```bash
which python3
```
Install libraries:
```bash
pip3 install -r requirements.txt
```
Move projects files into folder with user's binaries
```bash
mv common_bot.py /usr/local/bin/myfolder_with_bot_files
```
```bash
mv picture.jpg /usr/local/bin/myfolder_with_bot_files
```
```bash
mv private_bot.py /usr/local/bin/myfolder_with_bot_files
```
Move systemd units in required folder and run sevices:
```bash
mv private_bot.service /etc/systemd/system
```
```bash
mv common_bot.service /etc/systemd/system
```
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable common_bot.py
```
```bash
sudo systemctl enable private_bot.py
```
```bash
sudo systemctl start private_bot.py
```
```bash
sudo systemctl start common_bot.py
```
```bash
sudo systemctl -l status common_bot.py
```
```bash
sudo systemctl -l status private_bot.py
```

