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

if __name__ == '__main__':
    # my_coro = simple_coroutine()
    # next(my_coro)
    # my_coro.send(42)

    my_coro = simple_coro2(1)
    next(my_coro)
    my_coro.send(28)
    my_coro.send(99)
