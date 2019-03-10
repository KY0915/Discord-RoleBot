from discord import Game
from discord.ext.commands import Bot
import random
from discord.ext import commands
from discord.utils import get
import asyncio
BOT_PREFIX = ("?", "!")
TOKEN="Your own Token"

client= Bot(command_prefix=BOT_PREFIX)

#name allows difference names
#alias allows multiple name for the command for same function.
#brief= brief description
#description = descriptions when prompted using help !help command
#context pass allows user mention
@client.command(name="8",
                aliases=['eight','8ight'],
                brief="brief explanation",
                description="detailed explanation",
                pass_context=True)
async def eight_ball(context):
    possible_responses=["hello",
                       "who are you",
                       "nice to meet you",
                       "bye"]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="I am on"))
    print("Logged in as " + client.user.name)

@client.command(pass_context=True,
                brief="shows the current server's ID. Command is !info",
                description="shows the current server's ID example: !info")

async def info(ctx):
    if ctx.message.author == ctx.message.server.owner:
        await client.say("ID: {}".format(ctx.message.server.id))
    else:
        await client.say("Only server owner can use this command")

@client.command(pass_context=True)
async def new_roles(ctx):
    author= ctx.message.author
    await client.create_role(author.server,name="new role")
    

@client.command(pass_context=True,
                brief="Copy the roles of a server to another server",
                description="Copy the roles of a server to another server. Example: !copy_roles src_server_ID dest_server_ID"
                )
async def copy_roles(ctx):
    rolenamelistsrc=[]
    rolenamelistdest=[]
    await client.wait_until_ready()
    message=ctx.message.content
    message=message[12:]
    message=message.split(" ")
    author= ctx.message.author
    src=ctx.message.server
    
    for server in client.servers:
        if server.id==message[0]:
            print("found")
            for role in server.roles:
                rolenamelistsrc.append(role.name)
            #print(ctx.message.author.roles)

    

    for server in client.servers:
        if server.id==message[1]:
            print("migrating roles")
            for role in server.roles:
                rolenamelistdest.append(role.name)
            for role in rolenamelistsrc:
                if role not in rolenamelistdest:
                    await client.create_role(server,name=role)

    
        


    
    """
    print(author.server)
    print(src)
    print(src.id)
    print(src.roles)
    """
"""
#will add user to default role. 
@client.event
asyc def on_member_join(member):
    role= discord.utils.get(member.server.roles,name='new role')
    await client.add_roles(member,role)
"""


client.run(TOKEN)
