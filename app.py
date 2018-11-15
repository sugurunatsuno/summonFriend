import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")


@client.event
async def on_message(message):
    if message.content.startswith("/neko"):
        reply = "にゃーん"
        print(reply)
        await client.send_message(message.channel, reply)


@client.event
async def on_voice_state_update(before, after):

    # todo : ボイスチャットにインしている人がbotを除いて3人以上になった
    # todo : ギルガメがボイスチャットにいない

    # todo : Twitterでメンションを飛ばす

    avc = None
    if after.voice.voice_channel is not None:
        avc = after.voice.voice_channel

    if avc is not None:
        ch = [channel for channel in before.server.channels if channel.name == "general"][0]
        await client.send_message(ch, "ドーモ、{}サン".format(after.name))


token = os.environ["LOL"]

client.run(token)


# todo : ファイルを分けるdiscord, twitter, app, bot くらいに分けて拡張できるようにする
