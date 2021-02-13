import discord
from discord.ext import commands
import requests
import time
import json

bot = commands.Bot(command_prefix='!')

@bot.command()
async def bothelp(ctx):
    """
     >> Displays a help menu of all the commands and how to call them
    """
    help_embed = discord.Embed(
    title="Command Help",
    description="Raid Calculator Command: " + "Call using !raidcalc (type of explosive) (amount of sulfur)" + "\n" + "\nServer Status Command: " + "Call using !serverstatus (server name)" + "\n" +
    "\nRaid Chart Command: " + "Calling using !raidchart (explosive type)" + "\n" + "\nWipe Reminder Command: " + "Call using !wipereminder (type in seconds till the server wipes) (server name)",
    color = discord.Color.dark_orange()
    )

    help_embed.set_thumbnail(url="https://o.remove.bg/downloads/5963675a-bbc1-49cf-b325-5ab1d03b3481/png-transparent-question-mark-logo-question-mark-cartoon-text-monochrome-black-removebg-preview.png")
    await ctx.send(embed=help_embed)
@bot.command()
async def raidcalc(ctx,type,sulfur):
    """
     >> Takes two variables (type and sulfur) the program then takes the type you have entered Ie rocket,c4 or satchel
     and returns the amount of the entered item you are able to craft with the entered amount of sulfur as well as the other needed materials
    """
    if type == 'Rocket' or type == "Rockets" or type == "rocket" or type == "rockets":
        calculation_sulfur_rockets = int(sulfur) // 1400
        calculation_charcoal_rockets = calculation_sulfur_rockets * 1950
        calculation_fragments_rockets = calculation_sulfur_rockets * 100
        calculation_lg_rockets = calculation_sulfur_rockets * 30
        calculation_pipes_rockets = calculation_sulfur_rockets * 2
        rocket_menu = discord.Embed(
            title="Craftables",
            description="Amount: " + str(calculation_sulfur_rockets) + "\n" + "\nMaterials: " + "\nCharcoal: " + str(calculation_charcoal_rockets) + "\nFragments: " + str(calculation_fragments_rockets) + "\nLowgrade: " + str(calculation_lg_rockets) +
            "\nPipes: " + str(calculation_pipes_rockets),
            color=discord.Color.dark_orange()
        )
        rocket_menu.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/9/95/Rocket_icon.png/revision/latest/top-crop/width/360/height/360?cb=20151106061039")
        await ctx.send(embed=rocket_menu)
    elif type == 'C4':
        calculation_sulfur_c4 = int(sulfur) // 2200
        calculation_charcoal_c4 = calculation_sulfur_c4 * 3000
        calculation_fragments_c4 = calculation_sulfur_c4 * 200
        calculation_lg_c4 = calculation_sulfur_c4 * 60
        calculation_tech_c4 = calculation_sulfur_c4 * 2
        calculation_cloth_c4 = calculation_sulfur_c4 * 5
        c4_menu = discord.Embed(
            title="Craftables",
            description="Amount: " + str(calculation_sulfur_c4) + "\n" + "\nMaterials: " + "\nCharcoal: " + str(calculation_charcoal_c4) + "\nFragments: " + str(calculation_fragments_c4) + "\nLowgrade: " + str(calculation_lg_c4) +
            "\nTech Trash: " + str(calculation_tech_c4) + "\nCloth: " + str(calculation_cloth_c4),
            color=discord.Color.dark_orange()
        )
        c4_menu.set_thumbnail(
            url="https://static.wikia.nocookie.net/play-rust/images/6/6c/Timed_Explosive_Charge_icon.png/revision/latest?cb=20151106061610")
        await ctx.send(embed=c4_menu)
    elif type == 'Satchel' or type == "Satchels" or type == "satchel" or type == "satchels":
        calculation_sulfur_satchel = int(sulfur) // 480
        calculation_charcoal_satchel = calculation_sulfur_satchel * 720
        calculation_fragments_satchel = calculation_sulfur_satchel * 80
        calculation_rope_satchel = calculation_sulfur_satchel * 1
        satchel_menu = discord.Embed(
            title="Craftables",
            description="Amount: " + str(calculation_sulfur_satchel) + "\n" + "\nMaterials: " + "\nCharcoal: " + str(calculation_charcoal_satchel) + "\nFragments: " + str(calculation_fragments_satchel) +
            "\nRope: " + str(calculation_rope_satchel),
            color=discord.Color.dark_orange()
        )
        satchel_menu.set_thumbnail(
            url="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835Fc5WLCfDY0jhyo8DEiv5ddOKA9pbAzRP66Mz-oL1M/360fx360f")
        await ctx.send(embed=satchel_menu)


import json
@bot.command()
async def serverstatus(ctx, server):
    """
    Takes a string value (Paranoid or UKN) and will then display a embed menu with the servers information in the discord chat the command was called in.
    """
    if server == 'Paranoid':
        response = requests.get('https://api.battlemetrics.com/servers/8846084')
        print(response.status_code)
        json_data_paranoid = response.json()
        print(json_data_paranoid)
        name = str(json_data_paranoid["data"]["attributes"]["name"])
        server_status = str(json_data_paranoid["data"]["attributes"]["status"])
        player_count = str(json_data_paranoid["data"]["attributes"]["players"])
        players_queued = str(json_data_paranoid["data"]["attributes"]["details"]["rust_queued_players"])

        menu = discord.Embed(
         title=name,
         description="\nServer: Status " + server_status + "\nPlayers: " + player_count + "/250" + "\nQueue: " + players_queued,
         color=discord.Color.dark_orange()
        )

        menu.set_thumbnail(url="https://paranoid.gg/img/favicon.png")
        await ctx.send(embed=menu)
    elif server == 'UKN':
        response = requests.get('https://api.battlemetrics.com/servers/6792417')
        json_data_ukn = response.json()
        print(json_data_ukn)
        name = str(json_data_ukn["data"]["attributes"]["name"])
        server_status = str(json_data_ukn["data"]["attributes"]["status"])
        player_count = str(json_data_ukn["data"]["attributes"]["players"])
        players_queued = str(json_data_ukn["data"]["attributes"]["details"]["rust_queued_players"])

        men = discord.Embed(
         title=name,
         description="\nServer: Status " + server_status + "\nPlayers: " + player_count + "/425" + "\nQueue: " + players_queued,
         color=discord.Color.dark_orange()
        )

        men.set_thumbnail(url="https://ukn.gg/img/logo.png")
        await ctx.send(embed=men)
    elif server == 'Rusty2x':
        response = requests.get('https://api.battlemetrics.com/servers/433778')
        json_data_rusty2x = response.json()
        print(json_data_rusty2x)
        name = str(json_data_rusty2x["data"]["attributes"]["name"])
        server_status = str(json_data_rusty2x["data"]["attributes"]["status"])
        player_count = str(json_data_rusty2x["data"]["attributes"]["players"])
        players_queued = str(json_data_rusty2x["data"]["attributes"]["details"]["rust_queued_players"])

        men = discord.Embed(
         title=name,
         description="\nServer: Status " + server_status + "\nPlayers: " + player_count + "/200" + "\nQueue: " + players_queued,
         color=discord.Color.dark_orange()
        )

        men.set_thumbnail(url="https://i.redd.it/4r2d03zzicm31.png")
        await ctx.send(embed=men)


@bot.command()
async def raidchart(ctx, type):
    if type == 'C4':
        c4_chart = discord.Embed(
            title="C4 Chart",
            description="\nWood Wall: 1" + "\nStone Wall: 2" + "\nSheet Wall: 4" + "\n Armoured Wall: 8" + "\nWood Door: 1" + "\nSheet Door: 1" + "\nGarage Door: 2" + "\nArmoured Door: 2" + "\nLadder Hatch: 1" +
            "\nWood High Ex: 2" + "\nStone High Ex: 2",
            color=discord.Color.dark_orange()
        )

        c4_chart.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/6/6c/Timed_Explosive_Charge_icon.png/revision/latest?cb=20151106061610")
        await ctx.send(embed=c4_chart)
    elif type == 'Rocket':
        rocket_chart = discord.Embed(
            title="Rocket Chart",
            description="\nWood Wall: 2" + "\nStone Wall: 4" + "\nSheet Wall: 8" + "\n Armoured Wall: 15" + "\nWood Door: 1" + "\nSheet Door: 2" + "\nGarage Door: 3" + "\nArmoured Door: 4" + "\nLadder Hatch: 2" +
            "\nWood High Ex: 3" + "\nStone High Ex: 4",
            color=discord.Color.dark_orange()
        )

        rocket_chart.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/9/95/Rocket_icon.png/revision/latest/top-crop/width/360/height/360?cb=20151106061039")
        await ctx.send(embed=rocket_chart)
    elif type == 'Satchel':
        satchel_chart = discord.Embed(
            title="Satchel Chart",
            description="\nWood Wall: 3" + "\nStone Wall: 10" + "\nSheet Wall: 23" + "\n Armoured Wall: 46" + "\nWood Door: 2" + "\nSheet Door: 4" + "\nGarage Door: 9" + "\nArmoured Door: 12" + "\nLadder Hatch: 4" +
            "\nWood High Ex: 6" + "\nStone High Ex: 10",
            color=discord.Color.dark_orange()
        )

        satchel_chart.set_thumbnail(url="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835Fc5WLCfDY0jhyo8DEiv5ddOKA9pbAzRP66Mz-oL1M/360fx360f")
        await ctx.send(embed=satchel_chart)
    elif type == 'Stone Pickaxe':
        stonepick_chart = discord.Embed(
            title="Satchel Chart",
            description="\nWood Wall: 3" + "\nStone Wall: 10" + "\nSheet Wall: 23" + "\n Armoured Wall: 46" + "\nWood Door: 2" + "\nSheet Door: 4" + "\nGarage Door: 9" + "\nArmoured Door: 12" + "\nLadder Hatch: 4" +
                        "\nWood High Ex: 6" + "\nStone High Ex: 10",
            color=discord.Color.dark_orange()
        )

        stonepick_chart.set_thumbnail(url="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835Fc5WLCfDY0jhyo8DEiv5ddOKA9pbAzRP66Mz-oL1M/360fx360f")
        await ctx.send(embed=stonepick_chart)


@bot.command()
async def wipereminder(ctx, t:int, servername: str):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    if t == 0:
        wipe_embed = discord.Embed(
            title="Wipe Alert",
            description="@everyone " + servername + " has just wiped" ,
            color=discord.Color.dark_orange()
        )
        wipe_embed.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/46b63d3c-ae67-464c-9a37-670829b2a157/da3m1p2-984b8628-aef9-46ec-9a2f-67c63c174031.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNDZiNjNkM2MtYWU2Ny00NjRjLTlhMzctNjcwODI5YjJhMTU3XC9kYTNtMXAyLTk4NGI4NjI4LWFlZjktNDZlYy05YTJmLTY3YzYzYzE3NDAzMS5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.CoXXDV-5gqNkHM-IO5_sMNgz_l4lhK2dohdUFTl5rZI")
        await ctx.send(embed=wipe_embed)


bot.run("your token here")