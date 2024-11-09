#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store inputs and outputs in Redis."""
        # Generate keys for input and output lists
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        # Store input arguments as strings
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the result
        result = method(self, *args, **kwargs)

        # Store the output result
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    """Cache class for storing data in Redis with random keys."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable]): Optional function to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved
            data in the desired format.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a UTF-8 string from Redis by key."""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis by key."""
        return self.get(key, fn=int)

    def replay(self, method: Callable) -> None:
        """Display the history of calls for a particular function."""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        # Retrieve inputs and outputs from Redis
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        # Display the number of times the method was called
        print(f"{method.__qualname__} was called {len(inputs)} times:")

        # Loop over inputs and outputs and print them
        for input_data, output_data in zip(inputs, outputs):
            print(f"{method.__qualname__}(*
                  {input_data.decode()}) -> {output_data.decode()}")
