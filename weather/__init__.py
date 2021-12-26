from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import get_weather_of_city
from jieba import posseg

#创建一个命令名字为weather，可用’天气‘’天气预报’’查天气‘使用
@on_command ('weather', aliases = ( '天气', '天气预报', '查天气' ))
async def weather(session: CommandSession):
    city=session.current_arg_text.strip()
    if not city:
        city=(await session.aget(prompt='你想查询哪个城市的天气捏~')).strip()
        if city == '火星':
            await session.send('就你这小逼崽子还想查火星的天气，火星大气稀薄，只有地球的百分之一，主要是由遗留下的二氧化碳（百分之95.3）加上氮气（百分之2.7）、氩气（百分之1.6）和微量的氧气（百分之0.15）和水汽（百分之0.03）组成的。去了不得把你憋死')
        while not city:
            city=(await session.aget(prompt='该城市的消息不能为空捏~')).strip()
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)

@on_natural_language(keywords = {'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()#去掉消息前后的空白字符
    #使用jieba库进行分词和词性标注
    words = posseg.lcut(stripped_msg)
    city = None
    for word in words:
        if word.flag == 'ns':
            #ns表示地名
            city = word.word
            break
    return IntentCommand(90.0,'weather', current_arg=city or '')
