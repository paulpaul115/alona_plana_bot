from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

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
