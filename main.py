#Imports
import discord
import os
import requests
import json
import datetime

#intents
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.reactions = True

# Json Text


#body
client = discord.Client()


@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('TestJason'):
    MonthlyJson = discord.Embed(
      title = "Monthlies", url = "https://runescape.wiki/w/Repeatable_events#Monthly_events",
      description = "Monthlies reset in two days, don't forget to do them. ",
      color = 16744175,      
    )
    MonthlyJson.set_footer(text="Ask an admin for monthlies role if you want to receive this notification. UwU")
    MonthlyJson.set_thumbnail(url= "http://www.westnh.org/wp-content/uploads/2014/02/MonthlyIcon.png")
    #MonthlyJson.set_author(name = "Monthly Bot", icon_url = "https://cdn.discordapp.com/embed/avatars/0.png")
    MonthlyJson.add_field(name = ":space_invader: Troll Invasion", value = "Get a Reward book that allows you to claim xp in any skill.",inline = False)
    MonthlyJson.add_field(name = ":statue_of_liberty: God Statues ", value = "Build statues at: Lumbridge, Canifis, Yanille, Burthorpe, Prifddinas. For Construction + Prayer / Slayer experience.",inline = False)
    MonthlyJson.add_field(name = ":moneybag: Giant Oyster", value = "Gain Fishing + Farming xp and a clue scroll reward. wear LOTD. I strongly suggest you use monthly resets on this in hopes of getting a dye.",inline = False)
    MonthlyJson.add_field(name = ":book: Effigy Incubator", value = "Thok Stronk, I dont understand this dumb monthly. Gl idiots lul :cat:.",inline = False)
    MonthlyJson.add_field(name = ":credit_card: Premier Club vault", value = "Spend 1 minute in the vault to get loots. Must be a premier member.",inline = False)

    await message.channel.send("<@&463033145684393994>", embed= MonthlyJson )

  
 
client.run(os.environ['Token'])


