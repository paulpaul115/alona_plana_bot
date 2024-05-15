import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os
import random

bot = commands.Bot(command_prefix='/', intents=discord.Intents.default(),activity=discord.Game("💎"))
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="alona")
async def _alona(ctx):
>>>>>>> 6fb874b (🍇🐔 Checkpoint)
    # Define the weights for the results
    weights_first_nine = [78.5, 18.5, 3]
    weights_tenth = [97, 3]
    results = ["🟦", "🟨", "🟪"]
    
    # Perform draws for the first 9 results
    gacha_results = random.choices(results, weights=weights_first_nine, k=9)
    
    # Perform draw for the 10th result
    gacha_results.append(random.choices(results[1:], weights=weights_tenth, k=1)[0])
    
    # Send the result to the channel
    embed=discord.Embed(title="アロナ！", color=0x50f6fd)
    embed.add_field(name="結果", value=' '.join(gacha_results), inline=False)
    embed.add_field(name="-1200💎",value="",inline=False)
    await ctx.send(embed=embed)

    
@slash.slash(name="plana")
async def _plana(ctx):
    # Define the weights for the results
    weights_first_nine = [51.5, 18.5, 30]
    weights_tenth = [70, 30]
    results = ["🟦", "🟨", "🟪"]
    
    # Perform draws for the first 9 results
    gacha_results = random.choices(results, weights=weights_first_nine, k=9)
    
    # Perform draw for the 10th result
    gacha_results.append(random.choices(results[1:], weights=weights_tenth, k=1)[0])
    
    # Send the result to the channel
    embed=discord.Embed(title="プラナ！", color=0xff6bad)
    embed.add_field(name="結果", value=' '.join(gacha_results), inline=False)
    embed.add_field(name="-1200💎",value="",inline=False)
    await ctx.send(embed=embed)
    
bot.run(os.getenv('TOKEN'))
