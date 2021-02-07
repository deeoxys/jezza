"""
JEZZA BOT

TODO be a bit more efficient and use functions and procedures for stuff
TODO loop through ENTIRE server history and get quotes (this may be possible or may NOT idk)
TODO fix @everone exploit
"""

# imports
import discord
import time
import random
import datetime

# construct client with intents (a bit like permissions from what i understand)
client = discord.Client(intents = discord.Intents.all())
# some important variables
badwords = []
prefix = "J"
NAME = "jezza"

@client.event
async def on_ready():
    # set our status to waiting for prefix
    await client.change_presence(activity = discord.Activity
    (type = discord.ActivityType.watching, name = "for " + prefix))

    # varibles for logging
    global start_time
    start_time = time.time()

    # log that we have logged in successfully
    log("logged in as {0.user}".format(client) + ".")

@client.event
async def on_message(message):
    # ignore ourselves and other bots
    if message.author == client.user:
        return
    if message.author.bot:
        return

    # set up variables required for quoting
    filepath = "messages/" + str(message.author) + ".txt"
    text = str(message.content)
    file_name = ""
    quotes = []

    # ignore commands, these are the main ones i have thought of
    if not message.content.startswith("/") and not message.content.startswith("!") and not message.content.startswith("-") and not message.content.startswith("j"):
        # open file with append mode
        f = open(str(filepath), "a")
        # append message with the DELIMITER that hopefully no one ever sends! and the datetime
        f.write(str(message.content) + "$$DELIMITER$$" + str(datetime.datetime.now().strftime("%c")) + "\n")
        f.close()

    """ QUOTE COMMAND"""
    if text.upper().startswith(prefix + "QUOTE"):
        # some variables we need
        quoteMsg = ""
        quoteIndex = 0
        userToQuote = ""
        seed = 0

        # one of many try catches that hopefully stop the main exceptions that could occur
        try:
            userToQuote = client.get_user(message.mentions[0].id)
        except IndexError:
            log("Error: " + str(IndexError))
            pass
            return

        # if the ping was not read properly just give up :/
        if userToQuote == "":
            return

        # set up read path
        url = "messages/" + str(userToQuote) + ".txt"
        log("User " + str(message.author) + " requested quote from " + str(userToQuote) + ".")

        try:
            # calculate RANDOM SEED with GROUNDBREAKING technology
            seed = random.randint(0, file_len("messages/" + str(userToQuote) + ".txt") - 1)
        except FileNotFoundError:
            log("Error: " + str(FileNotFoundError))
            await message.channel.send(str(userToQuote) + " has not sent a message yet.")
            return

        # get all the users possible quotes
        f = open("messages/" + str(userToQuote) + ".txt", "r")
        quotes = f.readlines()
        f.close()

        # build the quote message up
        quoteMsg = "On " + quotes[seed].split("$$DELIMITER$$")[1].strip("\n") + ", " + str(userToQuote) + " said: " + quotes[seed].split("$$DELIMITER$$")[0]
        log("Got quote: " + quoteMsg + ".")
        await message.channel.send(quoteMsg)

    # """LASTWORDS COMMAND"""
    # if text.upper().startswith(prefix + "LASTWORDS"):
    #     # some variables we need
    #     quoteMsg = ""
    #     userToQuote = ""
    #
    #
    #     # one of many try catches that hopefully stop the main exceptions that could occur
    #     try:
    #         userToQuote = client.get_user(message.mentions[0].id)
    #     except IndexError:
    #         log("Error: " + str(IndexError))
    #         pass
    #         return
    #
    #     # if the ping was not read properly just give up :/
    #     if userToQuote == "":
    #         return
    #
    #     # set up read path
    #     url = "messages/" + str(userToQuote) + ".txt"
    #     log("User " + str(message.author) + " requested last words from " + str(userToQuote) + ".")
    #
    #     # get all the users quotes
    #     f = open("messages/" + str(userToQuote) + ".txt", "r")
    #     quotes = f.readlines()
    #     f.close()
    #
    #     # build the quote message up
    #     quoteMsg = str(userToQuote) + "s last words were on " + quotes[file_len(url)].split("$$DELIMITER$$")[1].strip("\n") + ", " + str(userToQuote) + " said: " + quotes[file_len(url)].split("$$DELIMITER$$")[0]
    #     log("Got last words: " + quoteMsg + ".")
    #     await message.channel.send(quoteMsg)

    """GIVE ALL COMMAND"""
    if text.upper().startswith(prefix + "GIVE ALL"):
        # get the users role
        role_names = [role.name for role in message.author.roles]
        # check if they have god role
        if not "God" in role_names:
            log("Non-admin user " + str(message.author) + " tried to use admin command (GIVE ALL)!")
            return

        # get the roleName parameter
        roleName = text.split()[2]
        count = 0

        # loop through server members
        for member in message.guild.members:
            count = count + 1
            try:
                # give role
                await member.add_roles(discord.utils.get(message.guild.roles, name=roleName))
                log("Successfully gave " + str(member) + roleName + " role. (" + str(count) + " users!).")
            except Exception:
                log("Error: " + str(Exception))
                return

        await message.channel.send("Successfully gave " + str(count) + " users DJ!")
        log("user " + str(message.author) + " gave all ("+ str(count) + ") users DJ role. (" + str(message.guild.name) + ").")

    """UPTIME COMMAND"""
    if text.upper() == (prefix + "UPTIME"):
        uptime = ("%s seconds" % (round(time.time() - start_time)))

        await message.channel.send(uptime)
        log("user " + str(message.author) + " requested uptime (" + uptime + ")")

    """PING COMMAND"""
    if text.upper() == (prefix + "PING"):
        # get latency/ping/RTT
        ping = ("%s ms" % round(client.latency))

        await message.channel.send(ping)
        log("user " + str(message.author) + " requested ping (" + str(ping) + ")")

    """HELP COMMAND"""
    if text.upper() == (prefix + "HELP"):
        await message.channel.send("You can find my GitHub page at https://github.com/r333mo/jezza, the README has my commands and features.")

    """BAD WORDS FILTER"""
    # check if it is in the message
    if text.upper() in badwords:
        # delet
        await message.delete()
        # mock them
        await message.channel.send("deleted illegal message posted by " + str(message.author))
        log("deleted illegal message posted by " + str(message.author))
    try:
        # in case there was no file attachments
        file_name = message.attachments[0].url
    except IndexError:
        pass

    # for files
    if file_name in badwords:
        # delet
        await message.delete()
        # mock them
        await message.channel.send("deleted illegal image posted by " + str(message.author))
        log("deleted illegal image posted by " + str(message.author))

# so folk cant scoop the bot.
def readKey():
    f = open("assets/.gitignore " + NAME + ".txt", "r")
    key = f.read()
    log("Opened file " + f.name + ", got key (" + key + ").")
    f.close()

    return key

# https://www.youtube.com/watch?v=qQMsLAIqtmU
def readBadwords():
    f = open("assets/.gitignore badwords.txt", "r")
    for line in f:
        stripped_line = line.strip("\n")
        badwords.append(stripped_line)

    log("Opened file " + f.name + ", got bad words (" + str(badwords) + ").")
    f.close()

# get the amount of lines in a file, this is p bad as it is NOT async. As users eventually send many thousands of messages i WILL rewrite this.
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def log(msg):
    print(str(datetime.datetime.now().strftime("%c")) + ": " + str(msg))

# start bot up.
readBadwords()
client.run(readKey())