# redisk
redisk is a redis client made by python
star it if you like it

this simple & easy to use

## Quick start
- way1
```python
from redisk import Redis

r = Redis(debug=True) # debug = True to use debug mod
key = r.get("key")
...
r.close()
```

- way2
```python
with Redis() as r:
    key = r.get("key")
    ...
```

- string
```python
r.get()
r.set()
r.incr()
r.incrby()
# or
r.String.get()
r.String.set()
r.String.incr()
r.String.incrby()
```

- hash
```python
r.hset()
r.hget()
r.hmset()
r.hmget()
r.getall()
# or
r.Hash.hset()
r.Hash.hget()
r.Hash.hmset()
r.Hash.hmget()
r.Hash.hgetall()
```

- List
```python
...
```

- Set
```python
...
```

- Zset
```python
...
```

- transaction
```python
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
```
the out put just like this
```python
127.0.0.1:6379> multi
OK
127.0.0.1:6379> set name horika
QUEUED
127.0.0.1:6379> lpush people kangkang
QUEUED
127.0.0.1:6379> lrange people 0 1
QUEUED
127.0.0.1:6379> get name
QUEUED
127.0.0.1:6379> set asd sdas sdsa
QUEUED
127.0.0.1:6379> set s sss
QUEUED
127.0.0.1:6379> exec
['OK', 20, ['kangkang', 'kangkang'], 'horika', RediskException('ERR syntax error'), 'OK']
```