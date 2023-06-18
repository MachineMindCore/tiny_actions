from argparse import ArgumentParser

def init_parser():
    action_parser = ArgumentParser(
        prog = "tiny-actions",
        usage = "Small cli command to record and play mouse and keyboard events.",
        description = "Record, play, store and load actions rutines. For stop rutine record press stopper key (default=ctrl+e)"
    )

    action_parser.add_argument("--record", nargs=1, type=str, required=False)
    action_parser.add_argument("--play", nargs=1, type=str, required=False)
    action_parser.add_argument("--combine", nargs='+', type=str, required=False)
    action_parser.add_argument("--list", nargs='?', required=False)
    return action_parser
    