import aioredis
from simple_settings import settings

class Cache:


    def __init__(self) -> None:
        self._redis = None

    async def setup(self) -> None:
        if not self._redis:
            self.redis = await aioredis.create_redis_pool(settings.REDIS_URL)