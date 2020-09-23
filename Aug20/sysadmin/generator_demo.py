def generate_traffic_signals():
    signal = 1
    print(f"returning red with signal value {signal}")
    yield signal

    signal += 1
    print(f"returning green with signal value {signal}")
    yield signal

    signal += 1
    print(f"returning orange with signal value {signal}")
    yield signal


if __name__ == "__main__":
    for signal in generate_traffic_signals():
        print(signal)
