from Raspberry_Pi.cli import parse_arguments
from Raspberry_Pi.eye_detection import start_detection
from Raspberry_Pi import events
import os


def main():
    def person_is_sleeping():
        events.on_sleep(wait_time_between_sounds=0.5, decibel_increase=10, repetition=1)

    def oh_no_youre_dying():
        events.on_crash()

    args = parse_arguments()

    if args.no_twilio:
        function_maps = {2: (person_is_sleeping, True)}
    else:
        function_maps = {2: (person_is_sleeping, True), 5: (oh_no_youre_dying, False)}

    start_detection(function_maps, False, False)
