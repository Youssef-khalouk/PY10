from functools import lru_cache


@lru_cache
def slow_add(a, b):
    print("Computing...")
    return a + b


print(slow_add(2, 3))  # Computes
print(slow_add(2, 3))  # Uses cache (no "Computing...")
print(slow_add(2, 3))  # Uses cache (no "Computing...")
print(slow_add(2, 3))  # Uses cache (no "Computing...")
print(slow_add(2, 3))  # Uses cache (no "Computing...")