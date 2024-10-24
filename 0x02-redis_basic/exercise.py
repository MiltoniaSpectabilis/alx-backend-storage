#!/usr/bin/env python3
"""
Redis basic - Exercise module
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times methods of Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper function that increments the count for the given method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper function that stores input and output lists in Redis
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(input_key, str(args))

        # Execute method and store output
        output = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(fn: Callable) -> None:
    """
    Display the history of calls of a particular function
    """
    redis_store = redis.Redis()
    fn_name = fn.__qualname__
    calls_count = redis_store.get(fn_name)

    try:
        calls_count = int(calls_count.decode('utf-8'))
    except (AttributeError, ValueError):
        calls_count = 0

    print(f"{fn_name} was called {calls_count} times:")

    inputs = redis_store.lrange(f"{fn_name}:inputs", 0, -1)
    outputs = redis_store.lrange(f"{fn_name}:outputs", 0, -1)

    for inp, out in zip(inputs, outputs):
        try:
            inp = inp.decode('utf-8')
            out = out.decode('utf-8')
        except (AttributeError, ValueError):
            continue
        print(f"{fn_name}(*{inp}) -> {out}")


class Cache:
    """
    Cache class for handling Redis operations
    """

    def __init__(self):
        """
        Initialize the Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store input data in Redis using a random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get value from Redis by key and convert it using optional function
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get a string value from Redis
        """
        value = self.get(key, lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """
        Get an integer value from Redis
        """
        value = self.get(key, lambda x: int(x))
        return value
