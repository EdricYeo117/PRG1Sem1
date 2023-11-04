import discord
from discord.ext import commands
from discord import app_commands
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#assign bot token
BOT_TOKEN = "MTEyNjgxOTA1Nzc0ODk1MTA4MQ.GfpCur.zMB8HYW5Pu0c0F_YomUL7wjpLmSqTpcX1lF7mI"
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())
blockwords = ["nigger", "black"]
hsr_characters = ["kafka", "jingliu"]

#on ready when able to be used
@bot.event
async def on_ready():
    print("Welcome to Overflow's workshop!")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#channel
BOT_CHANNEL = 1126818413856182374

#Member Join
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(BOT_CHANNEL)
    await channel.send("Welcome {}".format(member.mention))

#member leave
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(BOT_CHANNEL)
    await channel.send("Goodbye, you will not be missed :)")

#message sent
@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    await bot.process_commands(message)
    print("{}: {}".format(author, content))
    if message.author != bot.user:
        for text in blockwords:
            if "Moderator" not in str(message.author.roles) and text.lower() in str(message.content.lower()):
                await message.delete()
                await message.channel.send("STOP BEING RACIST")
        for text in hsr_characters:
            if "Moderator" not in str(message.author.roles) and text.lower() in str(message.content.lower()):
                await message.delete()
                await message.channel.send("xiao mei mei silverwolf is cuter")

#message delete
@bot.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await channel.send("{}: {}".format(author, content))

#message edit
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
       return
    author = before.author
    channel = before.channel
    before_content = before.content
    after_content = after.content
    await channel.send("Before : {}".format (before_content))
    await channel.send("After: {}".format(after_content))


#reaction added
@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    name = user.name
    emoji = reaction.emoji
    content = reaction.message.content
    await channel.send('{} has added {} to the message: {}'.format(name, emoji, content))

#reaction removed
@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    name = user.name
    emoji = reaction.emoji
    content = reaction.message.content
    await channel.send(' {} has removed {} to the message: {}'.format(name, emoji, content))

#embed discord join

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(BOT_CHANNEL)
    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title="Welcome to this discord channel", description="It is a very cool channel", colour=discord.Colour.random())
    embed.set_author(name="{}".format(name))
    embed.set_thumbnail(url="{}".format(pfp))
    embed.add_field(name="This is a field", value="This field is just a value")
    embed.set_footer(text="Hope you enjoy your time in this server!")
    await channel.send(embed=embed)

#embedding again

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    author = before.author
    pfp = author.display_avatar
    before_content = before.content
    after_content = after.content
    channel = before.channel
    embed = discord.Embed(title="Changes were made", colour=discord.Colour.random())
    embed.set_author(name="{}".format(author))
    embed.set_thumbnail(url="{}".format(pfp))
    embed.add_field(name="Before:", value="{}".format(before_content), inline=False)
    embed.add_field(name="After:", value="{}".format(after_content))
    await channel.send(embed=embed)

#prefix things
@bot.command()
async def ping(ctx):
    mention = await ctx.send("Pong")
    await mention.add_reaction(":pong:")

@bot.command()
async def delete(ctx, user: discord.User):
    async for message in ctx.channel.history(limit=None):
        if message.author == user and message.id != ctx.message.id:
            await message.delete()
            break

#slash commands

@bot.event
async def on_ready():
    print("Bot is ready for use!")
    print("---------------------")
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} Command(s)')
    except Exception as e:
        print(e)


@bot.tree.command(description="Greets user")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!")

#subcommands

mygroup = app_commands.Group(name="greetings", description="Welcome users")
bot.tree.add_command(mygroup)

@mygroup.command(description="Pings user")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"ping {interaction.user.mention}! ")

@mygroup.command(description="Pongs user")
async def pong(interaction: discord.Interaction):
    await interaction.response.send_message(f"pong {interaction.user.mention}! ")

@mygroup.command(description="xmm lover")
async def xmm(interaction: discord.Interaction):
    await interaction.response.send_message(f"i love xmms {interaction.user.mention}! ")

@mygroup.command(description="allahu akbar")
async def allahuakbar(interaction: discord.Interaction):
    await interaction.response.send_message(f"ALLAHU AKBAR sAlAkAu {interaction.user.mention}! :exploding_head: ")

#moderation commands

@bot.command()
@commands.has_any_role("Moderator")
async def ban(ctx, user:discord.Member):
    if user is ctx.guild.members:
        await user.ban()
        await ctx.send(f"Banned user: {user.display_name} has been banned for racism!")
    else:
        await ctx.send("User not found")

@bot.command()
@commands.has_any_role("Moderator")
async def unban(ctx, name:str):
    notFound = True
    async for entry in ctx.guild.bans(limit = None):
        user = entry.user
        entryName = user.display_name
        if entryName == name:
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned user: {user.display_name}")
            notFound = False
        if notFound == True:
            await ctx.send("User not found")

 #jokes
def get_joke(category):
    if category == 'general':
        joke_url = "https://official-joke-api.appspot.com/random_joke"
        try:
            response = requests.get(joke_url)
            joke_data = response.json()
            if 'setup' in joke_data and 'punchline' in joke_data:
                return f"{joke_data ['setup']}\n{joke_data['punchline']}"
        except requests.exceptions.RequestException:
            pass
    elif category == 'dadjokes':
        joke_url = 'https://icanhazdadjoke.com/'
        headers = {'Accept' : 'application/json'}
        try:
            response = requests.get(joke_url, headers=headers)
            joke_data = response.json()
            if 'joke' in joke_data:
                return joke_data['joke']
        except requests.exceptions.RequestException:
            pass

@bot.command()
async def joke(ctx, category=None):
    if not category:
        category = 'general'

    joke = get_joke(category)
    if joke:
        await ctx.send(joke)
    else:
        await ctx.send("Sorry, I couldn't find a joke. I'm the clown...")

#spotify
spotify_client_id = "5476bccffc7a4458a071290a3589e2b3"
spotify_client_secret = "288c9169a7b345c4a3ef44d90fc11f490"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))


bot.run(BOT_TOKEN)
    





