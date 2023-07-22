import discord
import time
from gen_pass import gen_pass_test
from coin_game import coin_game

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

coins = 20
coinsPerMine = 10

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global coins, coinsPerMine

    if message.author == client.user:
        return
    
    if message.content.startswith('/mine'):
        coins += coinsPerMine
        await message.channel.send(f"+{coinsPerMine}")

    elif message.content.startswith('/balance'):
        await message.channel.send(str(coins))
    elif message.content.startswith('/coin'):
        await message.channel.send(str(coin_game()))

    elif message.content.startswith('/upgrade'):
        if coins >= 20:
            coins-=20
            coinsPerMine+=10
            await message.channel.send("Улучшен майнинг\n-20")
        else:
            await message.channel.send("Не хватает монет для улушения")

    


client.run("MTEzMjI3NzQxMDYzNzgyNDA1MQ.GhJaWU.WmYa6R8FRx5HznBZrMhJsdNUzoAgjCFFu38a3c")