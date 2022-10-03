from EventLoop import EventLoop

def loadThing(callback):
    global loop
    print("loading thing")
    loop.setTimeout(callback, 2000)

def procThing(callback):
    global loop
    print("thing loaded")
    loop.setTimeout(callback, 2000)
    
def finished():
    print("finished")

loop = EventLoop()
# 
loadThing(lambda: procThing(finished))
# in reverse order
procThing(lambda: loadThing(finished))
loop.run()
print("done!")


# notes:
# In the previous example, the callbacks were hard-coded. Here, they are passed in dynamically.
# This allows us to reorder the callbacks trivially.
# But, it also requires nesting the callbacks. For short chains, this is fine. For long chains, the nesting can be quite deep:
# loadThing(lambda: procThing(lambda: analyzeThing(lambda: uploadThing(finished))))
#
# There is another problem: C doesn't have lambdas, so this method basically won't work in C (at least not conveniently).
#
# However, with promises, you don't need lambdas or nesting:
# loadThing()
# .then(procThing)
# .then(analyzeThing)
# .then(uploadThing)
# .then(finished)

