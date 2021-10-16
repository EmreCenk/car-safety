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
    try:
        audio = files.setdefault(
            fileName, AudioSegment.from_mp3(f"{filePath}/media/{fileName}.mp3")
        )
        audio += volume

        play(audio)
    except Exception as E:
        #This case here is written to test the system on windows.
        #
        # print("Linux version didn't work. ig this isn't linux. Here's the error:", E)
        # print("Trying test version for windows")
        os.startfile(f"{filePath}/media/{fileName}.mp3")


def onSleep(wait_time_between_sounds: float = 0.5,
            decibel_level: int = 10,
            repetitions: int = 10) -> None:
    for _ in range(repetitions):
        playFile("alarm", decibel_level)
        playFile("wake_up", decibel_level)
        playFile("wake_up", decibel_level)
        time.sleep(wait_time_between_sounds)


if __name__ == "__main__":
    onSleep(wait_time_between_sounds=0.5,
            decibel_level=10,
            repetitions=10)
