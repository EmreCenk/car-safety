import os

filePath = os.path.dirname(os.path.realpath(__file__))


def playFile(fileName: str, volume: float = 1) -> None:
    """
    :param fileName: name of audio file in ./media
    :param volume: volume of sound, with 1 being 100%
    :return: void
    """
    os.system(f"mpg123 -f -{32768 * volume} {filePath}/media/{fileName}.mp3")


def onSleep() -> None:
    playFile("wake_up", 1)


if __name__ == "__main__":
    onSleep()
