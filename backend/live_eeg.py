from pylsl import resolve_byprop, StreamInlet
import numpy as np

print("Looking for Muse EEG stream...")

streams = resolve_byprop('type', 'EEG', timeout=10)

if not streams:
    raise RuntimeError("No EEG stream found. Start 'python -m muselsl stream' first.")

inlet = StreamInlet(streams[0])

print("Connected to Muse!")

def get_live_sample():
    sample, timestamp = inlet.pull_sample()
    return np.array(sample)

# Test: continuously print samples
while True:
    sample = get_live_sample()
    print(sample)