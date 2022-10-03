from EventLoop import EventLoop

loop = EventLoop()
loop.setTimeout(lambda: print("hello after 5 seconds"), 5000)
loop.setTimeout(lambda: print("hello after 1 seconds"), 1000)
loop.run()

print("done!")
