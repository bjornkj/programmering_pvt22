with open('system.log') as f:
    print(''.join(filter(lambda s: "BEAR" in s or "X-RAY" in s, f)))
