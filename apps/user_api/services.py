from common.redis import Cache

class UserService:
    cache = Cache()

    async def delete_cache(self, cpf:str) -> None:
        if await self.cache.get_cache(cpf):
            await self.cache.delete_cache(cpf)
