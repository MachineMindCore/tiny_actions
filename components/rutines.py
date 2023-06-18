import threading
import keyboard
import mouse
import pickle
from typing import List, Dict
from components.recorders import Recorder

class ActionRutine:
    def __init__(self, rutine_name: str, key_stopper: str = "ctrl+e"):
        self.recorder: Recorder = Recorder(key_stopper)
        self.rutine_name: str = rutine_name
        self.keyboard_events: List = []
        self.mouse_events: List = []

    def __add__(self, another):
        self.keyboard_events += another.keyboard_events
        self.mouse_events += another.mouse_events
        self.rutine_name = f"{self.rutine_name}_{another.rutine_name}"
        return self
        

    def record(self):
        self.keyboard_events, self.mouse_events = self.recorder.record()

    def play(self):
        k_thread = threading.Thread(target = lambda: keyboard.play(self.keyboard_events))
        m_thread = threading.Thread(target = lambda: mouse.play(self.mouse_events))
        k_thread.start()
        m_thread.start()
        k_thread.join()
        m_thread.join()
    
    def save(self):
        with open(f'actions/{self.rutine_name}.pkl', 'wb') as outp:
            pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)
        print(f"{self.rutine_name} saved")

    def load(self):
        with open(f'actions/{self.rutine_name}.pkl', 'rb') as inp:
            loaded_object = pickle.load(inp)
            self.__dict__.update(loaded_object.__dict__)     
        print(f"{self.rutine_name} loaded")