import cli
import os

args = cli.parse_arguments()

if args.sound:
    print(args.sound)
    if os.path.isfile(args.sound):
        print("Good path")
    else:
        print("Bad path")
