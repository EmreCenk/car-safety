import cli
import on_sleep
import os

args = cli.parse_arguments()

if args.sound:
    print(args.sound)
    if os.path.isfile(args.sound):
        on_sleep.on_sleep()
    else:
        print("Bad path")
