#!/usr/bin/env python3
"""
Web Cache and Tracker Module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cache_with_expiry(expiration_time: int = 10) -> Callable:
    """
    Decorator to cache the result with expiration time
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            redis_client = redis.Redis()
            count_key = f"count:{url}"
            content_key = f"cached:{url}"

            # Increment the access count
            redis_client.incr(count_key)

            # Try to get cached content
            cached_content = redis_client.get(content_key)
            if cached_content:
                return cached_content.decode('utf-8')

            # If not cached, fetch and cache the content
            content = func(url)
            redis_client.setex(content_key, expiration_time, content)

            return content
        return wrapper
    return decorator


@cache_with_expiry()
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL and track access frequency
    """
    response = requests.get(url)
    return response.text
