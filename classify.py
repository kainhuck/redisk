# classify

class String(object):
    def __init__(self, master):
        self._master = master

    def set(self, key: str, value: str, expire: int = -1) -> str:
        return self._master.set(key, value, expire)

    def get(self, key: str) -> str:
        return self._master.get(key)

    def incr(self, key: str) -> int:
        return self._master.incr(key)

    def incrby(self, key: str, increment: int) -> int:
        return self._master.incrby(key, increment)


class Hash(object):
    def __init__(self, master):
        self._master = master

    def hset(self, key: str, items: dict) -> int:
        return self._master.hset(key, items)

    def hget(self, key: str, field: str) -> object:
        return self._master.hget(key, field)

    def hmset(self, key: str, items: dict) -> str:
        return self._master.hmset(key, items)

    def hmget(self, key: str, *args) -> [str]:
        return self._master.hmget(key, *args)

    def hgetall(self, key: str) -> dict:
        return self._master.hgetall(key)


class List(object):
    def __init__(self, master):
        self._master = master

    def lpush(self, key: str, *args) -> int:
        return self._master.lpush(key, *args)

    def lrange(self, key: str, start: int, stop: int) -> [str]:
        return self._master.lrange(key, start, stop)

    def rpush(self, key: str, *args) -> int:
        return self._master.rpush(key, *args)

    def ltrim(self, key: str, start: int, stop: int) -> str:
        return self._master.ltrim(key, start, stop)

    def lpop(self, key: str) -> str:
        return self._master.lpop(key)

    def llen(self, key: str) -> int:
        return self._master.llen(key)


class Set(object):
    def __init__(self, master):
        self._master = master

    def sadd(self, key: str, *args) -> int:
        return self._master.sadd(key, *args)

    def smembers(self, key: str) -> {str}:
        return self._master.smembers(key)

    def sdiff(self, key: str, *args) -> {str}:
        return self._master.sdiff(key, *args)

    def sinter(self, key: str, *args) -> {str}:
        return self._master.sinter(key, *args)

    def sunion(self, key: str, *args) -> {str}:
        return self._master.sunion(key, *args)

    def scard(self, key: str) -> int:
        return self._master.scard(key)


class Zset(object):
    def __init__(self, master):
        self._master = master

    def zadd(self, key: str, items: dict) -> int:
        return self._master.zadd(key, items)

    def zrange(self, key: str, start: int, stop: int, withscores: bool = False) -> list:
        return self._master.zrange(key, start, stop, withscores)

    def zrevrange(self, key: str, start: int, stop: int, withscores: bool = False) -> list:
        return self._master.zrevrange(key, start, stop, withscores)

    def zcard(self, key: str) -> int:
        return self._master.zcard(key)


class Key(object):
    def __init__(self, master):
        self._master = master
    
    def keys(self, pattern: str) -> [str]:
        return self._master.keys(pattern)
    
    def getAllKeys(self) -> [str]:
        return self._master.getAllKeys()
    
    def rename(self, key:str, newkey:str):
        return self._master.rename(key, newkey)
    
    def renamenx(self, key:str, newkey:str) -> int:
        return self._master.renamenx(key, newkey)
    
    def dump(self, key:str) -> bytes:
        return self._master.dump(key)
    
    def delete(self, key:str, *args) -> int:
        return self._master.delete(key, *args)
    
    def exists(self, key:str, *args) -> int:
        return self._master.exists(key, *args)
    
    def expire(self, key:str, seconds:int) -> int:
        return self._master.expire(key, seconds)
    
    def pexpire(self, key:str, milliseconds:int) -> int:
        return self._master.pexpire(key, milliseconds)
    
    def persist(self, key:str) -> int:
        return self._master.persist(key)
    
    def ttl(self, key:str) -> int:
        return self._master.ttl(key)
    
    def pttl(self, key:str) -> int:
        return self._master.pttl(key)
    
    def randomKey(self) -> str:
        return self._master.randomKey()
    
    def typeOf(self, key:str) -> str:
        return self._master.typeOf(key)