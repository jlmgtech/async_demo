from EventLoop import *

def loadThing(result):
    global loop
    print("loading thing")
    prm = Promise()                                  # make a promise
    loop.setTimeout(lambda: prm.resolve(None), 2000) # it will resolve after 2 seconds
    return prm                                       # return it to the caller

def procThing(result):
    global loop
    print("thing loaded")
    prm = Promise()
    loop.setTimeout(lambda: prm.resolve(None), 2000)
    return prm
    
def finished(result):
    print("finished")

loop = EventLoop()

#creating promises
loadprm = loadThing(None)
procprm = loadprm.then(procThing)
procprm.then(finished)

# reordering execution is straightforward
# run procThing before loadThing
procThing(None) \
    .then(loadThing) \
    .then(finished)

loop.run()
print("done!")


#notes
# promises essentially just wrap a callback in a one-time observer.
# In other words, you give the promise a listener (with .then), and the listener is notified
# when the promise is resolved.

# In a traditional callback-style concurrency model, the execution of the callback 
# The key thing is this: any function that has the promise can add a listener to it.
# Because of this, the burden of managing the callback(s) is freed from 
# managing the callback to the promise object, which
# means that the callbacks don't specifically have to be defined in the same
# scope as the promise.
# In this way, promises allow you to "de-nest" your callbacks, defining the
# callbacks wherever you have access to the promise object.
