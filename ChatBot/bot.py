import discord
import responses
import credentials as cr
import requests, json

async def send(ms, user_ms, is_private):
    try:
        response = responses.respond(user_ms)
        if response != "":
            await ms.author.send(response) if is_private else await ms.channel.send(response)
    
    except Exception as e:
        print(e)


def get_weather(city):

    # defaults city to cairo if it was empty
    if city == "":
        city = "cairo"
    try:
        base_url = "http://api.weatherapi.com/v1/current.json?key=" + cr.WEATHERKEY
        complete_url = base_url + "&q=" + city + "&aqi=no"
        response =  requests.get(complete_url) 
        result = response.json()
        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed

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
        if user_ms[0:7] == "weather":
            user_ms = user_ms[8:]
            print("LOL")
            await ms.channel.send(embed=get_weather(user_ms))
        else:
            await send(ms, user_ms, is_private)

    client.run(cr.TOKEN)

