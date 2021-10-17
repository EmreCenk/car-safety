import os
import time
from pydub import AudioSegment
from pydub.playback import play

file_path = os.path.dirname(os.path.realpath(__file__))

files: dict[str, AudioSegment] = {}


def play_file(file_name: str, volume: float = 0) -> None:
    """
    :param fileName: name of audio file in ./media
    :param volume: increase in volume in dB
    :return: void
    """

    try:
        # Note(Callum): I changed this because I don't believe that this function
        # should handle the path stuff
        audio = files.setdefault(
            file_name,
            AudioSegment.from_mp3(file_name),
        )
        audio += volume

        play(audio)
    except Exception as E:
        # This case here is written to test the system on windows.
        #
        # print("Linux version didn't work. ig this isn't linux. Here's the error:", E)
        # print("Trying test version for windows")
        # file_name = file_name.replace("\\", "/").replace("/events","")
        os.startfile(file_name)
        print("started file")


def on_sleep(
    wait_time_between_sounds1: float = 0.5,
    wait_time_between_sounds2: float = 0.5,
    decibel_increase: int = 10,
    repetition: int = 1,
) -> None:
    for _ in range(repetition):
        play_file(f"{file_path}/../media/alarm.mp3", decibel_increase)
        play_file(f"{file_path}/../media/wake_up.mp3", decibel_increase)
        play_file(f"{file_path}/../media/wake_up.mp3", decibel_increase)

        time.sleep(wait_time_between_sounds1)

    for _ in range(repetition):
        play_file(f"{file_path}/../media/pull_over.mp3", decibel_increase)

        time.sleep(wait_time_between_sounds2)


if __name__ == "__main__":
    on_sleep(0.5, 10, 5)
