from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import yiqingchaxun
from jieba import posseg

@on_command ('yiqing',aliases = ('疫情', '查疫情' ))
async def yiqing(session: CommandSession):
    area=session.current_arg_text.strip()
    if not area:
        area=(await session.aget(prompt='你想查询哪个地区的疫情捏~')).strip()
        while not area:
            area=(await session.aget(prompt='该地区的内容不能为空噢~')).strip()
    yiqing_msg = await yiqingchaxun(area)
    await session.send(yiqing_msg)

@on_natural_language(keywords = {'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()#去掉消息前后的空白字符
    #使用jieba库进行分词和词性标注
    words = posseg.lcut(stripped_msg)
    area = None
    for word in words:
        if word.flag == 'ns':
            #ns表示地名
            area = word.word
            break
    return IntentCommand(90.0,'yiqing', current_arg=area or '')
