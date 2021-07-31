import discord
from discord.ext import commands
from random import shuffle, seed
import time
import datetime
import os

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='.', description="Bot para Summoners Rift", intents=intents)

#@bot.command()
#async def help(ctx):
#	embed = discord.Embed(title="Nunu help!",
#	 description=".generate - Genera 2 equipos al azar de los usuarios que estén en el canal de voz.")
#	await ctx.send(embed=embed)


@bot.command()
async def generate(ctx, opt):
	if not opt == "random":
		return
	print()
	voice = ctx.author.voice
	if voice is not None:
		members = voice.channel.members
		if len(members) == 2 or len(members) == 1:
			return await ctx.send("El channel en el que estás sólo hay 2 personas")

		seed(time.time())
		shuffle(members)
		embed = discord.Embed(title="EQUIPOS GENERADOS ALEATORIAMENTE", description="-",
					timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		
		team_one = []
		team_two = []
		for member in members:
			if(len(team_one) < len(members)/2):
				team_one.append(member)
			else:
				team_two.append(member)

		print(ctx.author, "generated teams:")
		print("Team Blue:", [x.name for x in team_one])
		print("Team Red", [x.name for x in team_two])

		one_msg = ""
		for player in team_one:
			one_msg = one_msg + player.mention + "\n"
		embed.add_field(name=":blue_circle: Equipo Azul:", value=one_msg, inline=True)
		two_msg = ""
		for player in team_two:
			two_msg = two_msg + player.mention + "\n"
		embed.add_field(name=":red_circle: Equipo Rojo 2:", value=two_msg, inline=False)
		embed.set_thumbnail(url="https://i.imgur.com/V6lhORZ.png")
		
		await ctx.send(embed=embed)
		
		return
	else:
		await ctx.send(':x: Error. Tenés que estar en un canal de voz.', delete_after=1300)

@bot.event
async def on_ready():
	print('El bot está inicializado.')


BOT_KEY = os.environ.get('BOT_KEY')

bot.run(BOT_KEY)