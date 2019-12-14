def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

def loop_coro():
    i = 0
    while i < 10:
        yield i  
        a = yield
        print('received a:', a)
        i += a

if __name__ == '__main__':
    # my_coro = simple_coroutine()
    # next(my_coro)
    # my_coro.send(42)

    #my_coro = simple_coro2(1)
    #next(my_coro)
    #my_coro.send(28)
    #my_coro.send(99)
    coro = loop_coro()
    i = next(coro)
    while True:
        print('i:', i)
        next(coro)
        i = coro.send(1)
