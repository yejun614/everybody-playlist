import wave
import miniaudio

from websockets.sync.client import connect

SRC_FILE = "test.wav"


def play_from_file():
    stream = miniaudio.stream_file(SRC_FILE)

    with miniaudio.PlaybackDevice() as device:
        device.start(stream)
        input("")


def play_from_wave():
    def stream_pcm(source):
        required_frames = yield b""
        while True:
            sample_data = source.readframes(required_frames)
            if not sample_data:
                break
            print(".", end="", flush=True)
            required_frames = yield sample_data

    wavefile = wave.open(SRC_FILE, "rb")
    # data = wavefile.readframes(wavefile.getnframes())
    fs = wavefile.getframerate()
    channels = wavefile.getnchannels()
    sample_width = wavefile.getsampwidth()

    print("fs", fs)
    print("channels", channels)
    print("sample_width", sample_width)

    with miniaudio.PlaybackDevice(
        output_format=miniaudio.SampleFormat.SIGNED16,
        nchannels=channels,
        sample_rate=fs,
    ) as device:
        stream = stream_pcm(wavefile)
        next(stream)
        device.start(stream)
        input()

    wavefile.close()


def play_from_websocket():
    buffering = 10
    buf = []

    with connect("ws://localhost:8765") as websocket:
        print("Server connected")

        def stream_pcm(websocket):
            required_frames = yield b""
            while True:
                websocket.send(str(required_frames).encode())
                sample_data = websocket.recv()
                if not sample_data:
                    break
                buf.append(sample_data)

                if len(buf) >= buffering:
                    print(".", end="", flush=True)
                    required_frames = yield buf.pop(0)
                else:
                    print("!", end="", flush=True)

        wavefile = wave.open(SRC_FILE, "rb")
        fs = wavefile.getframerate()
        channels = wavefile.getnchannels()
        sample_width = wavefile.getsampwidth()

        print("fs", fs)
        print("channels", channels)
        print("sample_width", sample_width)

        with miniaudio.PlaybackDevice(
            output_format=miniaudio.SampleFormat.SIGNED16,
            nchannels=channels,
            sample_rate=fs,
        ) as device:
            stream = stream_pcm(websocket)
            next(stream)
            device.start(stream)
            input()


if __name__ == "__main__":
    play_from_websocket()
