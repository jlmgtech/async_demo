import time

# create constants for different terminal colors:
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0;0m"
GREY = "\033[1;30m"

class TimeoutCallback:
    def __init__(self, callback, timeoutid, delay):
        self.callback = callback
        self.timeoutid = timeoutid
        self.delay = delay
        self.active = True

class EventLoop():
    def __init__(self):
        self.events = []
        self.timeouts = []
        self.listeners = {}
        self.running = True
        self.lastid = 0
        self.seconds = 0

    def setTimeout(self, callback, delay):
        timeout = TimeoutCallback(callback, self.lastid, delay)
        self.timeouts.append(timeout)
        self.lastid += 1
        return self.lastid-1

    def run(self):
        while self.running:
            for timeout in self.timeouts:
                if timeout.delay <= 0:
                    timeout.callback()
                    timeout.active = False
                else:
                    timeout.delay -= 500

            self.timeouts = [t for t in self.timeouts if t.active]
            if len(self.timeouts) == 0:
                self.running = False
            time.sleep(0.5)
            self.seconds += 0.5
            print(f"{CYAN}tick: {BLUE}{self.seconds}s{RESET}")


