from Raspberry_Pi.cli import parse_arguments
from Raspberry_Pi.events import on_sleep
import os


def main():
    args = parse_arguments()

    if args.sound:
        print(args.sound)
        if os.path.isfile(args.sound):
            on_sleep()
        else:
            print("Bad path")
