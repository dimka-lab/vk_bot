# vk_bot
# Chat Bot for social media vk
## Using
Download the script 
```bash
git clone https://github.com/rus121/vk_bot.git
```
Open the folder
```bash
cd vk_bot
```
Make sure the python binaries are in /usr/bin/python3 as usual e.g in ubuntu 
```bash
which python3
```
Install libraries:
```bash
pip install -r requirements.txt
```
Move projects files into folder with user's binaries
```bash
sudo mv common_bot.py /usr/local/bin/myfolder_with_bot_files
```
```bash
sudo mv picture.jpg /usr/local/bin/myfolder_with_bot_files
```
```bash
sudo mv private_bot.py /usr/local/bin/myfolder_with_bot_files
```
Move systemd units in required folder:
```bash
sudo mv private_bot.service /etc/systemd/system
```
```bash
sudo mv common_bot.service /etc/systemd/system
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
