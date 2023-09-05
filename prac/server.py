import wave
import asyncio
from websockets.server import serve

SRC_FILE = "test.wav"

current_pos = 0


async def send_wav(websocket):
    global current_pos

    wavefile = wave.open(SRC_FILE, "rb")
    wavefile.setpos(current_pos)
    # fs = wavefile.getframerate()
    # channels = wavefile.getnchannels()
    # sample_width = wavefile.getsampwidth()

    while wavefile.tell() < wavefile.getnframes():
        recv = await websocket.recv()
        required_frames = int(recv.decode())
        await websocket.send(wavefile.readframes(required_frames))
        print(".", end="", flush=True)
        current_pos = wavefile.tell()

    current_pos = 0
    wavefile.close()


async def main():
    async with serve(send_wav, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
