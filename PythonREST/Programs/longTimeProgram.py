def f():
    import time
    for i in range(0, 5):
        time.sleep(3)
    return "long time program finished after 15 seconds."

result = f()
