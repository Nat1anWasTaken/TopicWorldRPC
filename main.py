import asyncio

from pypresence import Presence

event_loop = asyncio.new_event_loop()

client = Presence(client_id=994508721327718410, loop=event_loop)

client.connect()

client.update(
    state="傳送指令｜領地飛行｜自由建造",
    details="完全自由的紅石伺服器！",

    large_image="icon",
    large_text="Topic World",
    small_image="minecraft",
    small_text="Java 1.19 & Bedrock 1.19.0",

    buttons=[
        {
            "label": "加入 Discord 伺服器",
            "url": "https://discord.gg/38GrT4AeaB"
        },
        {
            "label": "複製 IP 地址",
            "url": "https://l.nat1an.xyz/copy?content=bWMubmF0MWFuLnh5eg=="
        }
    ]
)

event_loop.run_forever()
