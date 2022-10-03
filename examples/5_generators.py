from EventLoop import *

def loadThing(result):
    global loop
    print("loading thing")
    prm = Promise()
    loop.setTimeout(lambda: prm.resolve(None), 2000)
    return prm

def procThing(result):
    global loop
    print("thing loaded")
    prm = Promise()
    loop.setTimeout(lambda: prm.resolve(None), 2000)
    return prm
    
def finished(result):
    print("finished")

def doStuff():
    loaded = yield loadThing(None)
    proccd = yield procThing(loaded)
    finished(proccd)

def procGen(prev=None):
    global gen
    if gen is None: return
    try:
        # if iterator is still going, get next value
        result = gen.send(prev)
        if isinstance(result, Promise):
            result.then(lambda res: procGen(res))
        else:
            gen.send(None)
    except StopIteration:
        # iterator is finished
        gen = None

loop = EventLoop()
gen = doStuff()
procGen(None)

loop.run()
print("done!")
