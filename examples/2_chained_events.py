from EventLoop import EventLoop

def loadThing():
    global loop
    print("loading thing")
    loop.setTimeout(procThing, 2000)

def procThing():
    global loop
    print("thing loaded")
    loop.setTimeout(finished, 2000)
    
def finished():
    print("finished")

loop = EventLoop()
loop.setTimeout(loadThing, 0)
loop.run()

print("done!")
