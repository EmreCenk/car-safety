import os
import time
import sys
filePath = os.path.dirname(os.path.realpath(__file__))


def playFile(fileName: str, volume: float = 1) -> None:
    """
    :param fileName: name of audio file in ./media
    :param volume: volume of sound, with 1 being 100%
    :return: void
    """
    if "linux" in sys.platform:
        # works on linux
        os.system(f"mpg123 -q --scale {32768 * volume} {filePath}/media/{fileName}.mp3")

    else:
        # works in windows
        os.startfile(f"{filePath}/media/{fileName}.mp3")

def onSleep() -> None:
    for i in range(10):
        playFile("wake_up", i)

        time.sleep(0.5)


if __name__ == "__main__":
    onSleep()
