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

    # Note(Callum): I changed this because I don't believe that this function
    # should handle the path stuff
    audio = files.setdefault(
        file_name,
        AudioSegment.from_mp3(file_name),
    )
    audio += volume

    play(audio)


def on_sleep() -> None:
    for _ in range(10):
        play_file(f"{file_path}/media/alarm.mp3", 10)
        play_file(f"{file_path}/media/wake_up.mp3", 10)
        play_file(f"{file_path}/media/wake_up.mp3", 10)

        time.sleep(0.5)


if __name__ == "__main__":
    on_sleep()
