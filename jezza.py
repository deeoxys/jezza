import discord
import time
import random
import datetime

client = discord.Client(intents = discord.Intents.all())
badwords = []
prefix = "J"

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity
    (type = discord.ActivityType.watching, name = "for " + prefix))

    global start_time
    start_time = time.time()

    log("logged in as {0.user}".format(client) + ".")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return

    filepath = "messages\\" + str(message.author.id) + ".txt"
    text = str(message.content)
    file_name = ""
    quotes = []


    if not message.content.startswith("/") and not message.content.startswith("!") and not message.content.startswith("-") and not message.content.startswith("j"):
        f = open(str(filepath), "a")
        f.write(str(message.content)+ "$$DELIMITER$$" + str(datetime.datetime.now().strftime("%x %X")) + "\n")
        f.close()

    if text.upper().startswith(prefix + "QUOTE"):
        quoteMsg = ""
        quoteIndex = 0
        userToQuote = ""
        seed = 0

        try:
            userToQuote = client.get_user(message.mentions[0].id)
        except IndexError:
            log("Error: " + str(IndexError))
            pass
            return

        if userToQuote == "":
            return

        url = "messages/" + str(userToQuote) + ".txt"
        log("User " + str(message.author) + " requested quote from " + str(userToQuote) + ".")

        try:
            seed = random.randint(0, file_len("messages/" + str(userToQuote) + ".txt") - 1)
        except FileNotFoundError:
            log("Error: " + str(FileNotFoundError))
            await message.channel.send(str(userToQuote) + " has not sent a message yet.")
            return

        f = open("messages/" + str(userToQuote) + ".txt", "r")
        quotes = f.readlines()
        f.close()

        quoteMsg = "On " + quotes[seed].split("$$DELIMITER$$")[1].strip("\n") + ", " + str(userToQuote) + " said: " + quotes[seed].split("$$DELIMITER$$")[0]
        log("Got quote: " + quoteMsg + ".")
        await message.channel.send(quoteMsg)

    if text.upper().startswith(prefix + "GIVE ALL"):

        role_names = [role.name for role in message.author.roles]
        if not "Bojo" in role_names:
            log("Non-admin user " + str(message.author) + " tried to use admin command (GIVE ALL)!")
            return

        roleName = text.split()[2]
        count = 0

        for member in message.guild.members:
            count = count + 1
            try:
                await member.add_roles(discord.utils.get(message.guild.roles, name=roleName))
                log("Successfully gave " + str(member) + roleName + " role. (" + str(count) + " users!).")
            except Exception:
                log("Error: " + str(Exception))
                return

        await message.channel.send("Successfully gave " + str(count) + " users DJ!")
        log("user " + str(message.author) + " gave all ("+ str(count) + ") users DJ role. (" + str(message.guild.name) + ").")

    if text.upper() == (prefix + "UPTIME"):
        uptime = ("%s seconds" % (round(time.time() - start_time)))

        await message.channel.send(uptime)
        log("user " + str(message.author) + " requested uptime (" + uptime + ")")

    if text.upper() == (prefix + "PING"):
        ping = ("%s ms" % round(client.latency))

        await message.channel.send(ping)
        log("user " + str(
            message.author) + " requested ping (" + str(ping) + ")")

    if text.upper() in badwords:
        await message.delete()
        await message.channel.send("deleted illegal message posted by " + str(message.author))
        log("deleted illegal message posted by " + str(message.author))

    try:
        file_name = message.attachments[0].url
    except IndexError:
        pass

    if file_name in badwords or text.__contains__("sausages"):
        await message.delete()
        await message.channel.send("deleted illegal image posted by " + str(message.author))
        log("deleted illegal image posted by " + str(message.author))

# so folk cant scoop the bot.
def readKey():
    f = open("assets/.gitignore jezza.txt", "r")
    key = f.read()
    log("Opened file " + f.name + ", got key (" + key + ").")
    f.close()

    return key

def readBadwords():
    f = open("assets/.gitignore badwords.txt", "r")
    for line in f:
        stripped_line = line.strip("\n")
        badwords.append(stripped_line)

    log("Opened file " + f.name + ", got bad words (" + str(badwords) + ").")
    f.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def log(msg):
    print(str(datetime.datetime.now().strftime("%x %X")) + ": " + str(msg))

# start bot up.
readBadwords()
client.run(readKey())