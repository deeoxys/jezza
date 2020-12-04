import discord
import time
import random
import datetime

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity
    (type = discord.ActivityType.watching, name = "for /j"))

    global start_time
    start_time = time.time()

    print(str(datetime.datetime.now().strftime("%X")) + ": " + "logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prefix = "/j "
    rec = False

    if message.content.startswith(prefix + "rec"):
        rec = True
        user = message.author
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "user " + str(message.author) + " requested recording")

        filepath = "messages\\" + str(user) + ".txt"
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "creating filepath: " + filepath)

        f = open(str(filepath), "w")
        f.close()

    if rec:
        f = open(str(filepath), "w")
        """if message.content.startswith("/"):
            return"""

        f.write(str(message.content) + ",")
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + " writing to file (" + filepath + ")")

    if message.content.startswith(prefix + "quote"):
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "user " + str(message.author) + " requested quote")

        f = open("messages\\" + message.author + "")


    if message.content.startswith(prefix + "uptime"):
        uptime = ("%s seconds" % (round(time.time() - start_time)))

        await message.channel.send(uptime)
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "user " + str(message.author) + " requested uptime (" + uptime + ")")

    if message.content.startswith(prefix + "ping"):
        ping = ("%s ms" % round(client.latency))

        await message.channel.send(ping)
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "user " + str(
            message.author) + " requested ping (" + str(ping) + ")")

    if message.content.startswith(prefix + "ping"):
        ping = ("%s ms" % round(client.latency))

        await message.channel.send(ping)
        print("\n" + str(datetime.datetime.now().strftime("%X")) + ": " + "user " + str(
            message.author) + " requested ping (" + str(ping) + ")")

# so folk cant scoop the bot.
def readKey():
    f = open("assets/.gitignore jezza.txt", "r")
    key = f.read()
    print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Opened file " + f.name + " got key (" + key + ").")
    f.close()

    return key

# start bot up.
client.run(readKey())