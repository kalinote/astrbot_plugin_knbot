from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("KNBot Base", "Kalinote", "KNBot 基础功能插件", "0.1", "https://github.com/kalinote/astrbot_plugin_knbot")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

        # 首先禁用自带的沙箱python解释器工具
        plugins = self.context.get_all_stars()
        for plugin in plugins:
            if plugin.name == "astrbot-python-interpreter":
                plugin.activated = False
