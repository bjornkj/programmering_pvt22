# “BEAR” eller “X-RAY”.

def filter_func(s: str) -> bool:
    return "BEAR" in s or "X-RAY" in s


with open('system.log') as f:
    print(''.join(filter(filter_func, f)))

