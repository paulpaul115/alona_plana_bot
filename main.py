import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os
import random

bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("こんにちは！"):
        await message.channel.send("こんにちは！")
    if message.content.startswith("よし"):
        await message.channel.send("どうでしたか？")
    if message.content.startswith("ふぅ"):
        await message.channel.send("おつかれさん")
    if message.content.startswith("ああ"):
        await message.channel.send("どうした？")
    if message.content.startswith("こんばんは！"):
        await message.channel.send("こんばんは！")

client.run("")
=======
if __name__ == "__main__":
  app.run()
>>>>>>> 3f58a27 (🙈🍈 Checkpoint)
=======

bot = commands.Bot(command_prefix='g-')
bot.remove_command("help")
@bot.event
=======
@client.event
>>>>>>> f75f183 (🐟🚞 Checkpoint)
async def on_ready():
  print("ログイン完了")
=======
@slash.slash(name="gacha")
async def _gacha(ctx):
    # Define the weights for the results
    weights_first_nine = [78.5, 18.5, 3]
    weights_tenth = [97, 3]
    results = ["🟪", "🟨", "🟦"]
    
    # Perform draws for the first 9 results
    gacha_results = random.choices(results, weights=weights_first_nine, k=9)
    
    # Perform draw for the 10th result
    gacha_results.append(random.choices(results[1:], weights=weights_tenth, k=1)[0])
    
    # Send the result to the channel
    await ctx.send(','.join(gacha_results))
>>>>>>> 7f7088c (🎣😘 Checkpoint)


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
bot.run(os.getenv('TOKEN'))
>>>>>>> 7333e66 (🚜👨‍❤️‍💋‍👨 Checkpoint)
=======
client.run(.env('TOKEN'))
>>>>>>> f75f183 (🐟🚞 Checkpoint)
=======
>>>>>>> 43b7f21 (👵🐆 Checkpoint)
=======
=======
client.run(os.getenv('TOKEN'))
>>>>>>> dad48ff (🐂🏉 Checkpoint)
<<<<<<< HEAD
>>>>>>> fffadf9 (🐂🏉 Checkpoint)
=======
=======
client.run(os.getenv('TOKEN'))
>>>>>>> 3cd7792 (⛲️😼 Checkpoint)
<<<<<<< HEAD
>>>>>>> 3558a36 (⛲️😼 Checkpoint)
=======
=======
bot.run(os.getenv('TOKEN'))
>>>>>>> ab50f74 (🎣😘 Checkpoint)
>>>>>>> 7f7088c (🎣😘 Checkpoint)
