from parsing.parser import init_parser
from components.rutines import ActionRutine

class ActionsApp:
    def __init__(self):
        self.parser = init_parser()
        self.args = self.parser.parse_args()

    def run(self):
        for instruction in self.args._get_kwargs():
            if instruction[-1] != None:
                getattr(self, instruction[0])()
    
    def record(self):
        rutine = ActionRutine(rutine_name=self.args.record[0])
        rutine.record()
        rutine.save()
    
    def play(self):
        rutine = ActionRutine(rutine_name=self.args.play[0])
        rutine.load()
        rutine.play()
    
    def combine(self):
        new_rutine = ActionRutine(rutine_name="")
        for name in self.args.combine:
            partial_rutine = ActionRutine(rutine_name=name).load()
            new_rutine += partial_rutine
        new_rutine.save()
        