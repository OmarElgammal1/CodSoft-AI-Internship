import discord
import responses
import credentials as cr

async def send(ms, user_ms, is_private):
    try:
        response = responses.respond(user_ms)
        if response != "":
            await ms.author.send(response) if is_private else await ms.channel.send(response)
    
    except Exception as e:
        print(e)


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Confirmation message when bot is online on discord
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    # Condition that makes the bot not reply to its own messages
    @client.event
    async def on_message(ms):
        if ms.author == client.user:
            return
        username = str(ms.author)
        user_ms = str(ms.content)
        channel = str(ms.channel)
        is_private = False
        if user_ms[0] == '.':
            user_ms = user_ms[1:]
            is_private = True

        await send(ms, user_ms, is_private)

    client.run(cr.TOKEN)

