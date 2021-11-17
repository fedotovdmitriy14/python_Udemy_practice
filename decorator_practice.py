def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        finish = time.time()
        print(finish-start)
        return return_value
    return wrapper

@benchmark
def pr(url):
    import requests
    webpage = requests.get(url)

pr("https://www.codewars.com/kata/55905b7597175ffc1a00005a/train/python")