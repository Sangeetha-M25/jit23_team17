from pylsl import resolve_streams

print("Searching for streams...")

streams = resolve_streams()

print("Found", len(streams), "stream(s)")

for s in streams:
    print("----------------")
    print("Name :", s.name())
    print("Type :", s.type())
    print("Source ID :", s.source_id())