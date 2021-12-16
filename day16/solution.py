import math

def parse_input(file_path):
    with open(file_path, "r") as f:
        hex = f.readline().strip()
        return ''.join(map(lambda v: format(int(v, 16), "04b"), hex))

def take(packet, i, n):
    return i + n, packet[i:i + n]

def parse_packet(packet, i):
    i, version = take(packet, i, 3)
    i, type_id = take(packet, i, 3)

    parsed_packet = {
        'version': int(version, 2),
        'type_id': int(type_id, 2),
    }

    if int(type_id, 2) == 4:
        i, packet_val = parse_literal(packet, i)
    else:
        i, packet_val = parse_operator(packet, i)

    parsed_packet["value"] = packet_val

    return i, parsed_packet

def parse_literal(packet, i):
    last = False
    value = ""
    while not last:
        i, segment = take(packet, i, 5)
        value += segment[1:]
        if segment[0] == '0':
            last = True
    return i, int(value, 2)

def parse_operator(packet, i):
    i, length_type_id = take(packet, i, 1)
    subpackets = []

    if int(length_type_id, 2) == 0:
        length_segment_size = 15
    else:
        length_segment_size = 11

    i, length = take(packet, i, length_segment_size)
    length = int(length, 2)
    
    if length_segment_size == 15:
        i_old = i
        while length > (i - i_old):
            i, sub_packet = parse_packet(packet, i)
            subpackets.append(sub_packet)
    else:
        for _ in range(length):
            i, sub_packet = parse_packet(packet, i)
            subpackets.append(sub_packet)
    
    return i, subpackets

def sum_of_versions(packet):
    sum_ = packet["version"]
    if isinstance(packet["value"], list):
        for subpacket in packet["value"]:
            sum_ += sum_of_versions(subpacket)
    return sum_

def evaluate_packet(packet):
    type_id = packet["type_id"]
    # literals
    if type_id == 4:
        return packet["value"]

    # operators
    subpacket_values = [evaluate_packet(sub_packet) for sub_packet in packet["value"]]

    if type_id == 0:
        return sum(subpacket_values)

    if type_id == 1:
        return math.prod(subpacket_values)

    if type_id == 2:
        return min(subpacket_values)

    if type_id == 3:
        return max(subpacket_values)
    
    if type_id == 5:
        return int(subpacket_values[0] > subpacket_values[1])

    if type_id == 6:
        return int(subpacket_values[0] < subpacket_values[1])

    if type_id == 7:
        return int(subpacket_values[0] == subpacket_values[1])

if __name__ == "__main__":
    packet_input = parse_input("full-input.txt")
    _, packet = parse_packet(packet_input, 0)
    print("Part I: ", sum_of_versions(packet))
    print("Part II: ", evaluate_packet(packet))
    