import redis, random, math
import asyncio, pkg_resources

cache = redis.Redis(host='redis', port=6379)
book = pkg_resources.resource_filename('pd_app', 'data/pride-prejudice.txt')

'''class Model:
    def __init__(self, redis = cache):
        self.cache = redis
        self._init()

    def _init(self):
        pass


    async def reset_model(self):
        await self.train_stop()
        pipe = self.cache.pipeline()
        for k in self.cache.keys('*'):
            self.cache.delete(k)
        pipe.execute()
        self._init()


    def predict(self, query):
        return ''

    def train_start(self):
        return 0
    async def train_stop(self):
        return 0
    def train_status(self):
        return 0
'''
