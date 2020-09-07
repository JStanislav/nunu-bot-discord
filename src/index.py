import discord
from discord.ext import commands
from random import shuffle, seed
import time
import datetime
import os

bot = commands.Bot(command_prefix='.', description="Bot para Summoners Rift")

@bot.command()
async def help(ctx):
	embed = discord.Embed(title="Nunu help!",
	 description=".generate - Genera 2 equipos al azar de los usuarios que estén en el canal de voz.")
	await ctx.send(embed=embed)


@bot.command()
async def generate(ctx, opt):
	#voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
	#voice_channel = discord.utils.get(ctx.message.guild.voice_channels, name="General")
	if not opt == "random":
		return
	voice = ctx.message.author.voice
	if voice is not None:
		members = voice.channel.members
		if len(members) == 2:
			return await ctx.send("Me estás jodiendo? El channel en el que estás sólo hay 2 personas")
		seed(time.time())
		shuffle(members)
		embed = discord.Embed(title="A TRYHARDEAR", description="-",
					timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		
		team_one = []
		team_two = []
		for member in members:
			if(len(team_one) < len(members)/2):
				team_one.append(member)
			else:
				team_two.append(member)

		one_msg = ""
		for player in team_one:
			one_msg = one_msg + player.mention + "\n"
		embed.add_field(name=":blue_circle: Team 1:", value=one_msg, inline=True)
		two_msg = ""
		for player in team_two:
			two_msg = two_msg + player.mention + "\n"
		embed.add_field(name=":red_circle: Team 2:", value=two_msg, inline=False)
		embed.set_thumbnail(url="https://i.imgur.com/V6lhORZ.png")
		
		await ctx.send(embed=embed)

		
		#for member, i in zip(members, range(len(members))):
			
		#	await ctx.send('Player '+str(i)+': '+ member.mention)
		return
	else:
		await ctx.send(':x: Error. Tenés que estar en un canal de voz.', delete_after=1300)

@bot.event
async def on_ready():
	print('El bot está inicializado.')

bot.run('NzUyMzA5NDE5NjM0NzIwNzk4.X1Vwvg.tLCz4BVyWoW3BysSVwdkal6iCY8')