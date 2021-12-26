from .prv_city import list
from ._city import City
import ujson as json
import nonebot
import requests


async def yiqingchaxun(area: str):
    epidemic_data = json.loads(requests.get(
        "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    ).json()["data"])
    province = None
    city = None
    if area == "中国":
        province = area
    elif area[-1] == '省' or (area in list.keys()):
        province = area
    else:
        province = City[area]
        city = area
    if area == "中国":
        data_ = epidemic_data["areaTree"][0]
    else:
        for i in range(0, 99):
            if epidemic_data["areaTree"][0]["children"][i]["name"] == province:
                data_ = epidemic_data["areaTree"][0]["children"][i]
                break
    if city:
        for j in range(0, 999):
            if epidemic_data["areaTree"][0]["children"][i]["children"][j]["name"] == city:
                data_ = data_["children"][j]
                break
    if data_ == None:
        return "没有查询到..."
    confirm = data_["total"]["confirm"]  # 累计确诊
    heal = data_["total"]["heal"]  # 累计治愈
    dead = data_["total"]["dead"]  # 累计死亡
    dead_rate = data_["total"]["deadRate"]  # 死亡率
    heal_rate = data_["total"]["healRate"]  # 治愈率
    now_confirm = data_["total"]["nowConfirm"]  # 目前确诊
    suspect = data_["total"]["suspect"]  # 疑似
    add_confirm = data_["today"]["confirm"]  # 新增确诊
    last_update_time = epidemic_data["lastUpdateTime"]
    x = f"{area}"
    return (
        f"{x} 疫情数据：\n"
        f"\t目前确诊：\n"
        f"\t\t确诊人数：{now_confirm}(+{add_confirm})\n"
        f"\t\t疑似人数：{suspect}\n"
        f"==================\n"
        f"\t累计数据：\n"
        f"\t\t确诊人数：{confirm}\n"
        f"\t\t治愈人数：{heal}\n"
        f"\t\t死亡人数：{dead}\n"
        f"\t治愈率：{heal_rate}%\n"
        f"\t死亡率：{dead_rate}%\n"
        f"更新日期：{last_update_time}"
    )
