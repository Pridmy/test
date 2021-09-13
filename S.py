import asyncio

import pytgcalls
import pyrogram
import os

CHAT_ID = int(os.environ.get("CHAT_ID", "")) 
INPUT_SOURCE = os.environ.get("INPUT", "")



async def main(client):
    group_call = pytgcalls.GroupCallFactory(client).get_group_call()
    await group_call.join(CHAT_ID)
    await group_call.start_video(INPUT_SOURCE)

    await pyrogram.idle()


if __name__ == '__main__':
    pyro_client = pyrogram.Client(os.environ.get("SESSION_STRING", ""), int(os.environ.get("API_ID", "")), os.environ.get("API_HASH", ""))
    pyro_client.start()

    asyncio.get_event_loop().run_until_complete(main(pyro_client))
