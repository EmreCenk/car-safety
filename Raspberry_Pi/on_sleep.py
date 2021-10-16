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


def onSleep() -> None:
    for _ in range(10):
        playFile("alarm", 10)
        playFile("wake_up", 10)
        playFile("wake_up", 10)

        time.sleep(0.5)


if __name__ == "__main__":
    onSleep()
