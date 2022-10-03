from EventLoop import *

def loadThing():
    global loop
    print("loading thing")
    prm = Promise()                                  # make a promise
    loop.setTimeout(lambda: prm.resolve(None), 2000) # it will resolve after 2 seconds
    prm.then(procThing)                              # when it resolves, call procThing

def procThing(result):
    global loop
    print("thing loaded")
    prm = Promise()
    loop.setTimeout(lambda: prm.resolve(None), 2000)
    prm.then(finished)
    
def finished(result):
    print("finished")

loop = EventLoop()
loadThing()
loop.run()
print("done!")


#notes
# this example doesn't really show off the power of promises.
# Instead, it simply shows a direct translation of the 1st callback example.
# In the next example, we'll see a prominent reason promises are useful.
