# redis core

from conn import connect
from base import handle
from five import *


class Redis(object):
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance


    def __init__(self, host: str = "127.0.0.1", port: int = 6379, encode: str = "utf-8", debug: bool=False):
        self.host = host
        self.port = port
        self.encode = encode
        self.debug = debug
        self.conn = connect(host=host, port=port)

        self.String = String(self)
        self.Hash = Hash(self)
        self.List = List(self)
        self.Set = Set(self)
        self.Zset = Zset(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print("An Exception: %s." % exc_val)

        self.close()
        return True

    def close(self):
        self.conn.close()

    def raw(self, cmd: str) -> object:
        if self.debug:
            print(f"{self.host}:{self.port}> {cmd}")
        cmd = cmd + "\r\n"
        self.conn.send(cmd.encode(self.encode))
        result = self.conn.recv(1024)
        return handle(result.decode(self.encode))

    def multi(self) -> str:
        return self.raw("multi")

    def exec(self) -> object:
        return self.raw("exec")

    def ping(self) -> str:
        return self.raw("ping")

    def keys(self, pattern: str) -> [str]:
        cmd = f"keys {pattern}"
        return self.raw(cmd)

    def set(self, key: str, value: str, expire: int = -1) -> str:
        if expire < 0:
            cmd = f"set {key} {value}"
        else:
            cmd = f"set {key} {value} ex {expire}"
        return self.raw(cmd)

    def get(self, key: str) -> str:
        cmd = f"get {key}"
        return self.raw(cmd)

    def incr(self, key: str) -> int:
        cmd = f"incr {key}"
        return self.raw(cmd)

    def incrby(self, key: str, increment: int) -> int:
        cmd = f"incrby {key} {increment}"
        return self.raw(cmd)

    def hset(self, key: str, items:dict) -> int:
        cmd = f"hset {key}"
        for k, v in items.items():
            cmd += f" {k} {v}"
        return self.raw(cmd)

    def hget(self, key: str, field: str) -> object:
        cmd = f"hget {key} {field}"
        return self.raw(cmd)

    def hmset(self, key: str, items:dict) -> str:
        cmd = f"hmset {key}"
        for k, v in items.items():
            cmd += f" {k} {v}"
        return self.raw(cmd)

    def hmget(self, key: str, *args) -> [str]:
        cmd = f"hmget {key}"
        for field in args:
            cmd += f" {field}"
        return self.raw(cmd)

    def hgetall(self, key: str) -> dict:
        cmd = f"hgetall {key}"
        keyValueList = self.raw(cmd)
        keyValueDict = {}
        for i in range(0, len(keyValueList), 2):
            keyValueDict[keyValueList[i]] = keyValueList[i+1]
        return keyValueDict

    def lpush(self, key: str, *args) -> int:
        cmd = f"lpush {key}"
        for element in args:
            cmd += f" {element}"
        return self.raw(cmd)

    def lrange(self, key: str, start: int, stop: int) -> [str]:
        cmd = f"lrange {key} {start} {stop}"
        return self.raw(cmd)

    def rpush(self, key: str, *args) -> int:
        cmd = f"rpush {key}"
        for element in args:
            cmd += f" {element}"
        return self.raw(cmd)

    def ltrim(self, key: str, start: int, stop: int) -> str:
        cmd = f"ltrim {key} {start} {stop}"
        return self.raw(cmd)

    def lpop(self, key: str) -> str:
        cmd = f"lpop {key}"
        return self.raw(cmd)

    def llen(self, key: str) -> int:
        cmd = f"llen {key}"
        return self.raw(cmd)

    def sadd(self, key: str, *args) -> int:
        cmd = f"sadd {key}"
        for member in args:
            cmd += f" {member}"
        return self.raw(cmd)

    def smembers(self, key: str) -> {str}:
        cmd = f"smembers {key}"
        return set(self.raw(cmd))

    def sdiff(self, key: str, *args) -> {str}:
        cmd = f"sdiff {key}"
        for key in args:
            cmd += f" {key}"
        return set(self.raw(cmd))

    def sinter(self, key: str, *args) -> {str}:
        cmd = f"sinter {key}"
        for key in args:
            cmd += f" {key}"
        return set(self.raw(cmd))

    def sunion(self, key: str, *args) -> {str}:
        cmd = f"sunion {key}"
        for key in args:
            cmd += f" {key}"
        return set(self.raw(cmd))

    def scard(self, key: str) -> int:
        cmd = f"scard {key}"
        return self.raw(cmd)

    def zadd(self, key: str, items:dict) -> int:
        cmd = f"zadd {key}"
        for member, score in items.items():
            cmd += f" {score} {member}"
        return self.raw(cmd)

    def zrange(self, key: str, start: int, stop: int, withscores: bool = False) -> list:
        cmd = f"zrange {key} {start} {stop}"
        if withscores:
            cmd += f" WITHSCORES"
            memberScoreList = self.raw(cmd)
            memberScoreTupleSet = set()
            for i in range(0, len(memberScoreList), 2):
                memberScoreTupleSet.add(
                    (memberScoreList[i], int(memberScoreList[i+1])))
            return memberScoreTupleSet
        return self.raw(cmd)

    def zrevrange(self, key: str, start: int, stop: int, withscores: bool = False) -> list:
        cmd = f"zrevrange {key} {start} {stop}"
        if withscores:
            cmd += f" WITHSCORES"
            memberScoreList = self.raw(cmd)
            memberScoreTupleList = []
            for i in range(0, len(memberScoreList), 2):
                memberScoreTupleList.append(
                    (memberScoreList[i], int(memberScoreList[i+1])))
            return memberScoreTupleList
        return self.raw(cmd)

    def zcard(self, key: str) -> int:
        cmd = f"zcard {key}"
        return self.raw(cmd)


if __name__ == "__main__":
    r = Redis(debug=True)
    print(r.multi())
    print(r.set("name", "horika"))
    print(r.List.lpush("people", "kangkang"))
    print(r.List.lrange("people", 0, 1))
    print(r.get("name"))
    print(r.set("asd", "sdas sdsa"))
    print(r.set("s", "sss"))
    print(r.exec())
    r.close()