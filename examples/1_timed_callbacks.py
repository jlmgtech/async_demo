#first implement a basic event loop, with setTimeout and addEventListener
from EventLoop import EventLoop

def loadThing():
    global loop
    print("loading thing")
    loop.setTimeout(procThing, 1000)

def procThing():
    global loop
    print("thing loaded")
    loop.setTimeout(lambda: print("thing processed"), 1000)
    

loop = EventLoop()
loop.setTimeout(lambda: print("hello after 5 seconds"), 5000)
loop.setTimeout(lambda: print("hello after 1 seconds"), 1000)
loop.setTimeout(procThing, 0)
loop.run()

print("done!")
