import requests, time, re
from colorama import Fore


userid = '1'

profileFormat = f'https://www.roblox.com/users/{userid}/profile'
inventoryFormat = f'https://www.roblox.com/users/{userid}/inventory'
friendsFormat = f'https://www.roblox.com/users/{userid}/friends'

dataProfile = {'url': f'{profileFormat}','capture_all': 'on'}
ProfileSave = requests.post(f'https://web.archive.org/save/{profileFormat}', data=dataProfile)
if ProfileSave.status_code == 200:
    print(Fore.GREEN + f'[200] Successfully saved your profile page')
else:
    print(Fore.RED + f'[{ProfileSave.status_code}] Could not save your profile page')
time.sleep(3)

dataInventory = {'url': f'{inventoryFormat}','capture_all': 'on'}
inventorySave = requests.post(f'https://web.archive.org/save/{inventoryFormat}', data=dataInventory)
if inventorySave.status_code == 200:
    print(Fore.GREEN + f'[200] Successfully saved your inventory page')
else:
    print(Fore.RED + f'[{inventorySave.status_code}] Could not save your inventory page')
time.sleep(3)

dataFriends = {'url': f'{friendsFormat}','capture_all': 'on'}
FriendsSave = requests.post(f'https://web.archive.org/save/{friendsFormat}', data=dataFriends)
if FriendsSave.status_code == 200:
    print(Fore.GREEN + f'[200] Successfully saved your friends page')
else:
    print(Fore.RED + f'[{FriendsSave.status_code}] Could not save your friends page')
time.sleep(3)
