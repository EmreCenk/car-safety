import os
import time
from pydub import AudioSegment
from pydub.playback import play

filePath = os.path.dirname(os.path.realpath(__file__))

files: dict[str, AudioSegment] = {}


def playFile(fileName: str, volume: float = 0) -> None:
    """
    :param fileName: name of audio file in ./media
    :param volume: increase in volume in dB
    :return: void
    """
    audio = files.setdefault(
        fileName, AudioSegment.from_mp3(f"{filePath}/media/{fileName}.mp3")
    )
    audio += volume

    play(audio)


def onSleep(sleep_time: float = 0.5, decibel_level: int = 10) -> None:
    for _ in range(10):
        playFile("alarm", decibel_level)
        playFile("wake_up", decibel_level)
        playFile("wake_up", decibel_level)
        time.sleep(sleep_time)


if __name__ == "__main__":
    onSleep()
