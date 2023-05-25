from collections import deque, namedtuple

class Packet(namedtuple(""Packet"", [""arrival"", ""duration""])):
    def __init__(self, arrival, duration):
        super(Packet, self).__init__()
        self.start = arrival
        self.dropped = 0

    def get_start(self):
        return -1 if self.dropped else self.start

    def update_start(self, prev_packet):
        if (prev_packet.start + prev_packet.duration) > self.start:
            self.start = prev_packet.start + prev_packet.duration

def clear_processed_packets(buffer, time):
    while len(buffer) > 0 and (buffer[0].start + buffer[0].duration) <= time:
        buffer.popleft()

def calc_start_times(packets, buffer_size):
    buffer = deque()

    for packet in packets:
        prev_packet = None
        if len(buffer) > 0:
            prev_packet = buffer[len(buffer) - 1]

        if prev_packet is not None:
            packet.update_start(prev_packet)

        if len(buffer) == buffer_size:
            clear_processed_packets(buffer, packet.arrival)

        if len(buffer) == buffer_size:
            packet.dropped = 1
        else:
            buffer.append(packet)

    return [packet.get_start() for packet in packets]

def main():
    buffer_size, n_packets = map(int, input().split())
    packets = list(Packet(*map(int, input().split())) for _ in range(n_packets))

    start_times = calc_start_times(packets, buffer_size)
    print(*start_times, sep='\n')

if __name__ == '__main__':
    main() 