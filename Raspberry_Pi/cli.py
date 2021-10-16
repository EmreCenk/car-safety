import argparse
import pathlib


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect sleeping while driving and wake up user."
    )
    parser.add_argument(
        "--sound",
        type=pathlib.Path,
        help="sound to play when sleeping is detected",
        metavar="FILE",
    )
    args = parser.parse_args()
    return args
