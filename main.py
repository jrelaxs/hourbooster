import ctypes
import datetime
import os
import subprocess

import steam.client


content = "jrelaxs:Rulit22eg20070000"
account = [x.strip() for x in content.split(":")]
games = [730,1172470,570,466240,105600,290080]

os.system("title Steam Hour Booster")
client = steam.client.SteamClient()
client.cli_login(*account)
client.games_played(games)

os.system("cls")

start = datetime.datetime.now()
while not ctypes.windll.user32.GetAsyncKeyState(0x1B):
    current_time = str(datetime.datetime.now() - start).split(".")[0]
    print(f"\r[Steam Hour Booster] -> Username: [{client.user.name}] | Boosting For: [{current_time}]", end="")
    client.run_forever()
else:
    client.logout()
    client.disconnect()
