class tracer:
    def __init__(self, func): # On @ decoration: save original func
        self.calls = 0
        self.func = func
    def __call__(self, *args): # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a,b,c):
    print(a+b+c)

spam(1,2,3)
