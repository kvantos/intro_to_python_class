import time


# decorator
def perf_meter(func):
    def inner(*args):
        start = time.clock()
        func(*args)
        print("elapsed time: %s" % str(time.clock() - start))
    return inner


# this is also decorator
def cache_it(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner


for x in range(1,10,2):
    print(x)

class frange:

    class frange_iterator:
        def __init__(self, start, stop, step):
            self.start = start
            self.current = None
            self.stop = stop
            self.step = step

        def __next__(self):
            if self.current is None:
                self.current = self.start
                return self.start
            elif self.current + self.step <= self.stop - 1:
                self.current += self.step
                return self.current
            else:
                raise StopIteration

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return frange.frange_iterator(self.start, self.stop, self.step)


for z in frange(1,10,0.5):
    print(z)

rr = frange(1,10,0.5)

print(list(rr))

if 3.5 in rr:
    print("Ho")

@perf_meter
def is_sorted(iterable):
    return iterable == sorted(iterable)

print("simple1")
is_sorted([1,2,3,4,5])
print("simple2")
is_sorted([2,3,45,6])


def is_smaller(t):
    return t[0] < t[1]

@perf_meter
def is_sorted_better(iterable):
    it = iter(iterable)
    it2 = iter(iterable)
    next(it2)
    return all(map(is_smaller, (zip(it, it2))))

print("better1")
is_sorted(list(range(10000000)))
# is_sorted_better([1,2,3,4,5])
print("better2")
is_sorted_better([2,3,45,6])

@perf_meter
def is_sorted_my(iterable):
    srt = True
    for i, item in enumerate(iterable):
        try:
            next_item = iterable[i+1]
        except IndexError:
            break

        if item >= next_item:
            srt = False
            break
    return srt

print("my1")
is_sorted(list(range(10000000)))
# is_sorted_my([1,2,3,4,5])
print("my2")
is_sorted_my([2,3,45,6])

@cache_it
@perf_meter
def foo(n):
    time.sleep(n)
    return n*42


print("\n\n\n")
h = foo(5)
print("res 1 %s" % str(h))
e = foo(5)
print("res2 %s" % str(e))
