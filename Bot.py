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

    help_embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/rNrDLUvN5eu_VKOqg2YfS-sO2Edb3IFZAoX2aAKrPRkK_VGVW9H6CVM3Z4T3f0YYbeGop6G-LVhhMgRYBLbJ-d5hppUXjxxqrZcG7tokvMSBz4xpG3jz1Lda5QLVfRX_elC4JEW_N0cOnB6v5nUwhkH-")
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
    elif type == 'Expo' or 'expo':
        calculation_sulfur_expo = int(sulfur) // 25
        calculation_charcoal_expo = calculation_sulfur_expo * 20
        calculation_fragments_expo = calculation_sulfur_expo * 5
        expo_menu = discord.Embed(
            title="Craftables",
            description="Amount: " + str(calculation_sulfur_expo) + "\n" + "\nMaterials: " + "\nCharcoal: " + str(
                calculation_charcoal_expo) + "\nFragments: " + str(calculation_fragments_expo),
            color=discord.Color.dark_orange()
        )
        expo_menu.set_thumbnail(
            url="https://static.wikia.nocookie.net/play-rust/images/3/31/Explosive_5.56_Rifle_Ammo_icon.png/revision/latest/scale-to-width-down/256?cb=20151106061449")
        await ctx.send(embed=expo_menu)

import json
@bot.command()
async def serverstatus(ctx, id : str):
    """
    Takes a string value (Paranoid or UKN) and will then display a embed menu with the servers information in the discord chat the command was called in.
    """
    response = requests.get('https://api.battlemetrics.com/servers' + "/" + id)
    print(response.status_code)
    json_data= response.json()
    print(json)
    name = str(json_data["data"]["attributes"]["name"])
    status = str(json_data["data"]["attributes"]["status"])
    players = str(json_data["data"]["attributes"]["players"])
    player_queue = str(json_data["data"]["attributes"]["details"]["rust_queued_players"])
    seed = str(json_data["data"]["attributes"]["details"]["rust_maps"]["url"])

    serverstatus_menu = discord.Embed(
        title=name,
        description="Server Status: " + status + "\nPlayers Online: " + players + "/250" + "\nQueue Length: " + player_queue +
        "\nMap Seed: " + seed,
        color=discord.Color.dark_orange()
    )
    await ctx.send(embed=serverstatus_menu)

@bot.command()
async def raidchart(ctx, type):
    if type == 'C4' or type == "c4":
        c4_chart = discord.Embed(
            title="C4 Chart",
            description="\nWood Wall: 1" + "\nStone Wall: 2" + "\nSheet Wall: 4" + "\nArmoured Wall: 8" + "\nWood Door: 1" + "\nSheet Door: 1" + "\nGarage Door: 2" + "\nArmoured Door: 2" + "\nLadder Hatch: 1" +
            "\nWood High Ex: 2" + "\nStone High Ex: 2",
            color=discord.Color.dark_orange()
        )

        c4_chart.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/6/6c/Timed_Explosive_Charge_icon.png/revision/latest?cb=20151106061610")
        await ctx.send(embed=c4_chart)
    elif type == 'Rocket' or type == "Rockets" or type == "rocket" or type == "rockets":
        rocket_chart = discord.Embed(
            title="Rocket Chart",
            description="\nWood Wall: 2" + "\nStone Wall: 4" + "\nSheet Wall: 8" + "\nArmoured Wall: 15" + "\nWood Door: 1" + "\nSheet Door: 2" + "\nGarage Door: 3" + "\nArmoured Door: 4" + "\nLadder Hatch: 2" +
            "\nWood High Ex: 3" + "\nStone High Ex: 4",
            color=discord.Color.dark_orange()
        )

        rocket_chart.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/9/95/Rocket_icon.png/revision/latest/top-crop/width/360/height/360?cb=20151106061039")
        await ctx.send(embed=rocket_chart)
    elif type == 'Satchel' or type == "Satchels" or type == "satchel" or type == "satchels":
        satchel_chart = discord.Embed(
            title="Satchel Chart",
            description="\nWood Wall: 3" + "\nStone Wall: 10" + "\nSheet Wall: 23" + "\nArmoured Wall: 46" + "\nWood Door: 2" + "\nSheet Door: 4" + "\nGarage Door: 9" + "\nArmoured Door: 12" + "\nLadder Hatch: 4" +
            "\nWood High Ex: 6" + "\nStone High Ex: 10",
            color=discord.Color.dark_orange()
        )

        satchel_chart.set_thumbnail(url="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835Fc5WLCfDY0jhyo8DEiv5ddOKA9pbAzRP66Mz-oL1M/360fx360f")
        await ctx.send(embed=satchel_chart)
    elif type == 'Expo' or 'expo':
        expo_chart = discord.Embed(
            title="Expo Chart",
            description="\nWood Wall: 49" + "\nStone Wall: 209" + "\nSheet Wall: 417" + "\nArmoured Wall: 834" + "\nWood Door: 18" + "\nSheet Door: 63" + "\nGarage Door: 152" + "\nArmoured Door: 200" + "\nLadder Hatch: 63" +
            "\nWood High Ex: 6" + "\nStone High Ex: 10",
            color=discord.Color.dark_orange()
        )

        expo_chart.set_thumbnail(url="https://static.wikia.nocookie.net/play-rust/images/3/31/Explosive_5.56_Rifle_Ammo_icon.png/revision/latest/scale-to-width-down/256?cb=20151106061449")
        await ctx.send(embed=expo_chart)

bot.run("your token here")