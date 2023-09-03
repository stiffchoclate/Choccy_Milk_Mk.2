import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_responses(user_message)
        await message.author.send(response) if is_private else await  message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTE0MDY3NjU4ODk5NjkxOTI5Nw.G2J2RA.Q3ztdjFi0bFZeFj0kU8TTXe_SCXzaMm8FkdSRQ"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running! lesgo')
        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name = "Cooking absolutely nothing") )
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said the follwing: {user_message} | ({channel})') # for debugging

        if user_message[0] == '?': #private messahe
            user_message = user_message[1:] #will remove q mark
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        

    client.run(TOKEN)