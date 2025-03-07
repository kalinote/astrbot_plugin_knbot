from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("KNBot Base", "Kalinote", "KNBot 基础功能插件", "1.0.0", "https://github.com/kalinote/astrbot_plugin_knbot")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

