import os

filePath = os.path.dirname(os.path.realpath(__file__))


def playFile(fileName: str, volume: float = 1) -> None:
    os.system(f"mpg123 -f -{32768 * volume} {filePath}/media/{fileName}.mp3")


def onSleep():
    playFile("wake_up", 1)


if __name__ == "__main__":
    onSleep()
