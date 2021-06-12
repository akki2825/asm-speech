"""
Script to chunk audio file from syncmap file.

Usage:
    audio_chunk.py --syncmap-file=<s> --audio-file=<a> --output-dir=<o>

Options:
    --syncmap-file=<s>      Syncmap file path
    --audio-file=<a>        Audio file path
    --output-dir=<o>        Output directory for chunked audio files
"""
from docopt import docopt
import json
from pydub import AudioSegment


if __name__ == "__main__":
    args = docopt(__doc__)

    audio_file = args["--audio-file"]
    syncmap_file = args["--syncmap-file"]
    output_dir = args["--output-dir"]

    new_audio = AudioSegment.from_mp3(audio_file)

    with open(syncmap_file, 'r') as f:
        data = json.load(f)

    count = 0
    for item in data["fragments"]:
        t1 = float(item['begin']) * 1000
        t2 = float(item['end']) * 1000
        chunk = new_audio[t1:t2]
        chunk.export(output_dir + "demo" + str(count) + '.mp3', format="mp3")
        count+=1
