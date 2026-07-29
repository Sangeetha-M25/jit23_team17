from pylsl import resolve_streams, StreamInlet

print("Searching for streams...")

streams = resolve_streams()

print(f"Found {len(streams)} stream(s)\n")

for stream in streams:
    print("Name :", stream.name())
    print("Type :", stream.type())
    print("Source :", stream.source_id())
    print("----------------------")

    if stream.type() == "EEG":
        print("\nConnecting to EEG stream...\n")

        inlet = StreamInlet(stream)

        info = inlet.info()

        ch = info.desc().child("channels").child("channel")

        print("Channels:\n")

        while ch.name():
            print(ch.child_value("label"))
            ch = ch.next_sibling()

        break