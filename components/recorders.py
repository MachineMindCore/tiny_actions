import mouse
import keyboard

class Recorder:
    def __init__(self, key_stopper: str = "ctrl+e"):
        self.key_stopper:str = key_stopper
    
    def __call__(self):
        self.play()
    
    def record(self):
        print(f"To stop recording press {self.key_stopper}")
        mouse_events = []
        keyboard_events = []
        mouse.hook(mouse_events.append)
        keyboard.start_recording()
        keyboard.wait(self.key_stopper)
        mouse.unhook(mouse_events.append)
        keyboard_events = keyboard.stop_recording()
        return keyboard_events, mouse_events

    def set_stopper(self, new_key: str):
        self.key_stopper = new_key
    



