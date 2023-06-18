import time

class Timer:
    def __init__(self):
        self.init_time = time.time()
    
    def reset(self):
        self.init_time = time.time()
    
    def time(self):
        return self.init_time - time-time()