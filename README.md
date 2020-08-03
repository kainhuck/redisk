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