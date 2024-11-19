cache = {}

def initialize_cache():
    """Initialize the cache with default values."""
    global cache
    cache = {
        'user_data': {},
        'session_data': {},
    }
    print("Cache initialized.")

def get_from_cache(key):
    """Retrieve an item from the cache."""
    return cache.get(key, None)

def set_in_cache(key, value):
    """Set an item in the cache."""
    cache[key] = value

def clear_cache():
    """Clear the entire cache."""
    global cache
    cache.clear()
    print("Cache cleared.") 