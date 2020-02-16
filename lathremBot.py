# lathremBot.py
#
# This is the main module for lathremBot. It contains all the methods used to
# accept and reply to messages from discord.
#
# The discord.py module is used to handle communications to and from the
# Discord API. More information about discord.py and the Discord API can be
# found here:
#     https://github.com/Rapptz/discord.py
#     https://github.com/discordapp/discord-api-docs
#
# Please note that this bot uses lower level features of discord.py and it
# might be better/easier to explore the higher level discord.ext options as
# they provide more functionality "out-of-the-box".


from os import path
from random import choice
from time import gmtime, strftime


import discord


from config import getConfig
from config import getServerConfig, setServerConfig


client = discord.Client()
version = strftime("%Y.%j.%H%M", gmtime(path.getmtime(__file__)))
print(f"Starting client v{version}...")


commands = {}  # This dict tracks registered bot commands.


def registerCommand():
    """
    This decorator registers methods for the bot.  Put this before each
    method that should be exposed as a bot command.
    """

    def registerCommand(func):
        commands[func.__name__] = func
        return func
    return registerCommand


@client.event
async def on_ready():
    """
    This is called when the client has finished connecting.
    """

    print(f"""{client.user} connected and listening on: """)
    [print(f"""  {guild.name}""") for guild in client.guilds]
    print(f"""Registered Commands:""")
    [print(f"""  [{key}]""") for key in commands]
    for user in client.users:
        if not user.bot:
            print(user.id, user.name)


@client.event
async def on_message(message):
    """
    This is called for every message that LathremBot can see.
    """

    # don't respond to messages from this bot
    if message.author == client.user:
        return

    # don't respond to messages from other bots
    if message.author.bot is True:
        return

    # get the command prefix for the source guild
    guild_id = getattr(message.guild, 'id', None)
    prefix = getServerConfig(guild_id , "prefix")

    # process commands
    cmd = message.content
    if cmd.startswith(prefix):

        # get the requested command and its arguments by removing
        # the bot_prefix and splitting the words into a list
        cmd = cmd[len(prefix):].split()

        # make sure a command was given
        if len(cmd) > 0:

            # lower case only please
            cmd[0] = cmd[0].casefold()

            # execute the command
            if cmd[0] in commands:
                await commands[cmd[0]](message, cmd[1:], prefix)
                return


helloReplies = ["Ahoy ", "Aloha ", "Bonjour ", "Ciao ", "Hello ",
                "Hiya ", "Hola ", "Howdy ", "Konnichiwa "]


@registerCommand()
async def hello(message, args, prefix):
    """
    A friendly greeting.

    Say hello to LathremBot and it says hello back to you!

    Usage:
        {prefix}hello
    """

    id = message.author.id
    reply = f"""{choice(helloReplies)}<@{id}>!"""
    await message.channel.send(reply)


m8bReplies = ["It is certain.", "It is decidedly so.",
              "Without a doubt.", "Yes - definitely.",
              "You may rely on it.", "As I see it, yes.",
              "Most likely.", "Outlook good.",
              "Yes.", "Signs point to yes.",
              "Reply hazy, try again.", "Ask again later.",
              "Better not tell you now.", "Cannot predict now.",
              "Concentrate and ask again.", "Don't count on it.",
              "My reply is no.", "My sources say no.",
              "Outlook not so good.", "Very doubtful."]


@registerCommand()
async def m8b(message, args, prefix):
    """
    Ask the Magic 8-Ball.

    The Magic 8-Ball makes all your hard decisions easy!

    Usage:
        {prefix}m8b [your yes/no question]
    """

    id = message.author.id
    reply = f"""<@{id}>, the magic 8-ball says:\n> {choice(m8bReplies)}"""
    await message.channel.send(reply)


@registerCommand()
async def help(message, args, prefix):
    """
    Displays help messages.

    Call with no arguments to get a list of available
    commands, or call with a command as an argument to
    get additional information about that command.

    Each help command should contain a "Usage" section:
        Optional arguments are enclosed in [square brackets]
        Required arguments are enclosed in <angle brackets>

    Usage:
        {prefix}help [command]
    """

    if len(args) == 1:
        if args[0] in commands:
            desc = commands[args[0]].__doc__.format(prefix=prefix)
            reply = f"""{args[0]}\n{desc}"""
            await message.author.send(f"""```\n{reply}```""")
    else:
        reply = f"""LathremBot v{version}\n\nCommands:\n"""
        padding = max(map(len, commands))
        for (key, func) in commands.items():
            desc = func.__doc__.split("""\n""", 2)[1].strip()
            reply += f"""  {key.ljust(padding)}  {desc}\n"""
        reply += f"""\nType {prefix}help <command> for more info."""
        await message.author.send(f"""```\n{reply}```""")


@registerCommand()
async def prefix(message, args, prefix):
    """
    Change LathremBot's prefix.

    If you are the owner of this server, you can change
    the prefix used by LathremBot. The prefix must be
    at least 2 characters long and shouldn't start with
    any of Discord's markdown or escape characters.

    This command is only supported in server channels,
    it is ignored in direct messages.

    Usage:
        {prefix}prefix <new prefix>
    """

    if message.guild is not None:
        if message.author.id == message.guild.owner_id:
            if len(args) == 1:
                if len(args[0]) >= 2:
                    setServerConfig(message.guild.id, "prefix", args[0])
                    reply = f"""My prefix has been changed to {args[0]}."""
                    await message.channel.send(reply)


@registerCommand()
async def shutdown(message, args, prefix):
    """
    Shut down LathremBot.

    The owner of LathremBot can use this command to
    perform a clean shutdown.

    Usage:
        {prefix}shutdown
    """

    if message.author.id == int(getConfig('admin')):
        await client.logout()


# start the client
client.run(getConfig("token"))
