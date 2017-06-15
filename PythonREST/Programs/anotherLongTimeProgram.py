def f():
    import time
    for i in range(0, 4):
        time.sleep(3)
    return "long time program finished after 12 seconds."

result = f()
