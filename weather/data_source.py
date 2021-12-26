from config import NICKNAME
import ujson as json
import nonebot
import requests
async def get_weather_of_city(city:str) -> str:
    data_json = json.loads(requests.get(
                    f"http://wthrcdn.etouch.cn/weather_mini?city={city}"
                ).text)
        
    if "desc" in data_json:
        if data_json["desc"] == "invilad-citykey":
                return f"{NICKNAME}没查到!!试试查火星的天气？"
        elif data_json["desc"] == "OK":
            w_type = data_json["data"]["forecast"][0]["type"]
            w_max = data_json["data"]["forecast"][0]["high"][3:]
            w_min = data_json["data"]["forecast"][0]["low"][3:]
            fengli = data_json["data"]["forecast"][0]["fengli"][9:-3]
            ganmao = data_json["data"]["ganmao"]
            fengxiang = data_json["data"]["forecast"][0]["fengxiang"]
            repass = f"{city}的天气是 {w_type}\n最高温度: {w_max}\n最低温度: {w_min}\n风力: {fengli} {fengxiang}\n{ganmao}"
            return repass
        else:
            return "好像出错了？再试试？"    
