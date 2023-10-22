import asyncio
import logging
import requests
import random

import discord
from redbot.core.bot import Red

logger = logging.getLogger("red")

class mockup(Cog):
    """
    This is mockup cog used for testing..
    """

    def __init__(self, red: Red):
        super().__init__()
        if red.is_ready():  # todo: can we put while not here?
            asyncio.create_task(self.load())

    async def load(self):
        logger.info('== loaded mockup cog ==')
