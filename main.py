import discord
import os

client = discord.Client()

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

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")

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
>>>>>>> fffadf9 (🐂🏉 Checkpoint)
