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


# notes:
# this works, but what if you need to change the order of the events?
# for example, if you want to procThing before you loadThing?
# then you have to rewrite each function to point to a different followup function
# promises alleviate this problem by providing an object back to the caller that wraps the callback.
# This way, the order of the callbacks can be changed in the caller without changing the callee.
