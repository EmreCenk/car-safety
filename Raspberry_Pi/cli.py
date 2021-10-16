import argparse
import pathlib


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect sleeping while driving and wake up user."
    )
    parser.add_argument(
        "--sound",
        type=pathlib.Path,
        help="sound to play when sleeping is detected (UNIMPLEMENTED)",
        metavar="FILE",
    )
    parser.add_argument(
        "--no-twilio", action="store_true", help="disable Twilio integration"
    )
    args = parser.parse_args()
    return args
