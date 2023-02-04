import os # default module
import logging
import pickle
import math
import random
import discord
import ffmpeg
from dotenv import load_dotenv
from bing_image_urls import bing_image_urls
from src.tiktok_module import downloader
import youtube_dl

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
load_dotenv() # load all the variables from the env file
bot = discord.Bot()

cwd = os.getcwd()

# Print the current working directory
print(f"Current working directory: {cwd}")

os.system(f"{os.getcwd()}\\src\\minesweepmodes.py")

pickle_jar = []
with (open(r"src\minesweeper.obj", "rb")) as openfile:
    while True:
        try:
            pickle_jar.append(pickle.load(openfile))
        except EOFError:
            break
minesweeper_options = []
logging.info(pickle_jar)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(
    name = "latency",
    description = "Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(
    name = "savetwtvid",
    description = "Saves a video on twitter as an mp4.")
async def savetwtvid(ctx,link: discord.Option(str)):
    if "twitter.com" in link:
        try:
            requestid = random.randint(0, 999999)
            await ctx.respond("Getting your twitter video...")
            await ctx.channel.trigger_typing()
            with youtube_dl.YoutubeDL({'outtmpl': f'{os.getcwd()}/tw{requestid}s{ctx.author.id}.mp4'}) as ydl:
                ydl.download([link])
            await ctx.send(file=discord.File(f"{os.getcwd()}\\tw{requestid}s{ctx.author.id}.mp4"))
            os.remove(f'{os.getcwd()}\\tw{requestid}s{ctx.author.id}.mp4')
        except Exception:
            await ctx.send("Something went wrong. It could be from any of the following: \
            \n> the video is too long \
            \n> the content is age-restricted, \
            \n> the tweet is from a private account, or \
            \n> the link is not a twitter link.")

@bot.slash_command(
    name = "savetiktok",
    description = "Saves a tiktok as an mp4.")
async def savetiktok(ctx, link: discord.Option(str)):
    try:
        requestid = random.randint(0, 999999)
        await ctx.respond("Getting your tiktok...")
        await ctx.channel.trigger_typing()
        dl = downloader.tiktok_downloader()
        dl.musicaldown(url=link,output_name=f"tt{requestid}s{ctx.author.id}.mp4")
        await ctx.send(file=discord.File(f"{os.getcwd()}\\tt{requestid}s{ctx.author.id}.mp4"))
        os.remove(f'{os.getcwd()}\\tt{requestid}s{ctx.author.id}.mp4')
    except Exception:
        await ctx.send("Something went wrong. It could be from any of the following: \
        \n> the video is too long,\n> the content is age-restricted, \
        \n> the tweet is from a private account, or\n> the link is not a twitter link.")

@bot.slash_command(
    name = "compress",
    description = "Poorly compresses a video.")
async def compress(ctx,
    attachment: discord.Option(discord.Attachment,
        "Video to be compressed.",
        required = False),
    link: discord.Option(str,
        "Link to video. Will be ignored if attachment is provided.",
        required = False)):
    if (link or attachment):
        if not attachment:
            attachment = link
        await ctx.respond("Compressing your video...")
        await ctx.channel.trigger_typing()
        try:
            requestid = random.randint(0, 999999)
            stream = ffmpeg.input(str(attachment))
            stream = stream.output(
                f"{requestid}c{ctx.author.id}.mp4", video_bitrate=8000, audio_bitrate=000
                )
            ffmpeg.run(stream)
            await ctx.send(file=discord.File(f"{requestid}c{ctx.author.id}.mp4"))
            os.remove(f'{os.getcwd()}\\{requestid}c{ctx.author.id}.mp4')
        except Exception:
            await ctx.respond("This is not a *direct* link to a video.")
    else:
        await ctx.respond("Link or attach a video.")

@bot.slash_command(
    name = "compresstwt",
    description = "Poorly compresses a video from a twitter link.")
async def compresstwt(ctx, link: discord.Option(str, "Link to video.")):
    if "twitter.com" in link:
        try:
            requestid = random.randint(0, 999999)
            await ctx.respond("Getting your twitter video...")
            await ctx.channel.trigger_typing()
            with youtube_dl.YoutubeDL({'outtmpl': f'{os.getcwd()}/tw{requestid}s{ctx.author.id}.mp4'}) as ydl:
                ydl.download([link])
        except Exception:
            await ctx.send("Something went wrong. It could be from any of the following:\n> the video is too long,\n> the content is age-restricted,\n> the tweet is from a private account, or\n> the link is not a twitter link.")
        stream = ffmpeg.input(f"{requestid}sc{ctx.author.id}unboiled.mp4")
        stream = stream.output(f"{requestid}sc{ctx.author.id}.mp4", video_bitrate=8000, audio_bitrate=000)
        ffmpeg.run(stream)
        os.remove(f'{os.getcwd()}\\{requestid}sc{ctx.author.id}unboiled.mp4')
        await ctx.send(file=discord.File(f"{requestid}sc{ctx.author.id}.mp4"))
        os.remove(f'{os.getcwd()}\\{requestid}sc{ctx.author.id}.mp4')

@bot.slash_command(name = "upyourass", description = "Would you put this up your ass?")
async def upyourass(ctx):
    nouns = open("src/nounlist.txt", "r", encoding="utf-8")
    nouns = nouns.readlines()
    item = random.choice(nouns)
    output = discord.Embed(colour=discord.Color.teal(), title="Would you put this up your ass?")
    output.description = item.title()
    output.set_image(url = bing_image_urls(item, limit=1)[0])
    await ctx.send_response(embed = output)

@bot.slash_command(name = "minesweeper", description = "Play minesweeper.")
async def minesweeper(ctx,
    gamemode: discord.Option(str,
        "The minesweeper variant you want to play.",
        choices=pickle_jar[1].keys()),
    height: discord.Option(int,
        "Height of the area. (Default 9.)",
        default=9,
        max_value = 10,
        min_value = 2),
    width: discord.Option(int,
        "Width of the area. (Default 10.)",
        default = 10,
        max_value = 14, min_value = 2),
    mines: discord.Option(int,
        "Percentage of squares that are mines. (Default 30)",
        default=30,
        min_value = 1,
        max_value = 99)):
    mines = math.floor((height*width-len(pickle_jar[1][gamemode]["data"]))*(mines/100))
    minesweep_board = [ [0]*height for i in range(width)]
    safe_tile = [math.ceil(width/2)-1,math.ceil(height/2)-1]
    zeros = [[safe_tile[0], safe_tile[1]]]
    for (dx, dy) in pickle_jar[1][gamemode]["data"]:
        if safe_tile[1]+dx >= 0 and safe_tile[1]+dx < height and safe_tile[0]+dy >= 0 and safe_tile[0]+dy < width:
            zeros.append([safe_tile[0]+dy, safe_tile[1]+dx])
    m = 0
    while m < mines:
        a = random.randint(0, width-1)
        b = random.randint(0, height-1)
        if minesweep_board[a][b] != "💥" and [a, b] not in zeros:
            minesweep_board[a][b] = "💥"
            m += 1
    for x in range(height):
        for y in range(width):
            if minesweep_board[y][x] != "💥":
                total = 0
                for (dx, dy) in pickle_jar[1][gamemode]["data"]:
                    if x+dx >= 0 and x+dx < height and y+dy >= 0 and y+dy < width:
                        if minesweep_board[y+dy][x+dx] == "💥":
                            total += 1
                minesweep_board[y][x] = pickle_jar[0][total]
    response = f"**{pickle_jar[1][gamemode]['name']}**: {pickle_jar[1][gamemode]['description']} {width}x{height} | ||{mines}|| mines"
    for x in range(height):
        response += "\n"
        for y in range(width):
            if x == safe_tile[1] and y == safe_tile[0]:
                response += f"{minesweep_board[y][x]}"
            else:
                response += f"||{minesweep_board[y][x]}||"
    await ctx.send_response(response)
bot.run(os.getenv('TOKEN')) # run the bot with the token
