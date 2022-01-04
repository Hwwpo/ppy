from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment
import ujson as json
import requests


@on_command('sesetu', aliases='色色图')
async def setu(session: CommandSession):
    data_json = json.loads(requests.get(
        f"https://iw233.cn/API/GHS/1422322819.php?type=json"
    ).text)

    url = data_json["pic"]
    url1 = url.replace("\\", "/")

    seg = MessageSegment.image(url1)
    print(seg)
    await session.send(seg)
