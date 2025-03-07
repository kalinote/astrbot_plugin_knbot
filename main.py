from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("KNBot Base", "Kalinote", "KNBot 基础功能插件", "0.1", "https://github.com/kalinote/astrbot_plugin_knbot")
class KNBotBase(Star):    
    def __init__(self, context: Context):
        super().__init__(context)
        
        self.scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")

    @filter.on_astrbot_loaded()
    async def on_astrbot_loaded(self):
        for plugin in self.context.get_all_stars():
            if plugin.name == "astrbot-reminder" and plugin.activated:
                logger.info("禁用原生提醒插件")
                await self.context._star_manager.turn_off_plugin("astrbot-reminder")
            if plugin.name == "astrbot-python-interpreter" and plugin.activated:
                logger.info("禁用原生代码执行器插件")
                await self.context._star_manager.turn_off_plugin("astrbot-python-interpreter")
    
    
    