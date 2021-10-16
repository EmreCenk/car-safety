from Raspberry_Pi.cli import parse_arguments
from Raspberry_Pi.eye_detection import start_detection
from Raspberry_Pi import events
import os


def main():
    def person_is_sleeping():
        events.on_sleep(wait_time_between_sounds=0.5, decibel_level=10, repetitions=1)

    def oh_no_youre_dying():
        events.on_crash()

    args = parse_arguments()
    function_maps = {2: (person_is_sleeping, True), 5: (oh_no_youre_dying, False)}
    start_detection(function_maps, True, True)
