from khl import Bot,Message
from mcdreforged.api.all import PluginServerInterface,Info,CommandSource,RText
message_3 = "¿"

chat_bot = Bot("1/MTIwMDU=/K5GUvkc8dcGoXwxDmb4lUA==")

channel_id = "7116632627546621"

channel = chat_bot.fetch_public_channel(channel_id)

# register command
# invoke this via saying `/hello` in channel
@chat_bot.command("hello")
async def world(msg: Message):  # when `name` is not set, the function name will be used
    await chat_bot.send(await channel, message_3)


# everything done, go ahead now!
chat_bot.run()