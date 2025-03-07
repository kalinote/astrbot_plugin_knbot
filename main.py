from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("KNBot Base", "Kalinote", "KNBot 基础功能插件", "0.1", "https://github.com/kalinote/astrbot_plugin_knbot")
class KNBotBase(Star):
    def __init__(self, context: Context):
        super().__init__(context)

        # 禁用原生提醒插件
        self.context._star_manager.turn_off_plugin("astrbot-reminder")
        

