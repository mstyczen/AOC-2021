import numpy as np
from numpy.core.defchararray import chararray

def parse_input(file_path):
    with open(file_path, "r") as f:
        signals, outputs = [], []
        for line in f.readlines():
            signal, output = tuple(map(lambda x: x.strip(), line.split('|')))
            signal = signal.split(' ')
            output = output.split(' ')
            signals.append(signal)
            outputs.append(output)
        return signals, outputs

def part1(outputs):
    all_outputs = [digit for output in outputs for digit in output]
    return len(list(filter(lambda x: x in [2,3,4,7], map(len, all_outputs))))

def part2(signals, outputs):
    sum = 0
    for singal, output in zip(signals, outputs):
        segment_mapping = remap(singal, output)
        sum += decode_number(output, segment_mapping)
    return sum

def count_occurrences(character, string_array):
    # count in how many strings in a string list a character occurs 
    return len([character for string in string_array if character in string])

def remove_all_characters(str1, str2):
    # remove all characters that appear in str2 from str1
    return "".join([c for c in str1 if c not in str2])

def strlist_chars(string_array):
    # get all characters that appear in a stringlist
    return [c for c in "".join(string_array)]

def remap(signal, output):
    # get all unique sequences
    all_tokens = set(["".join(sorted(x)) for x in signal + output])

    digits_by_length = {}
    for i in range(2,8):
        digits_by_length[i] = list(filter(lambda x: len(x) == i, all_tokens))
    
    # the "a" segment is one that appears in a 7, but does not appear in a 1
    up = remove_all_characters(digits_by_length[3][0], digits_by_length[2][0])

    # find the remaining two segments of 1 based on number of occurrences in the 6 segment digits
    right_up = [c for c in digits_by_length[2][0] if count_occurrences(c, digits_by_length[6]) == 2][0]
    right_down = [c for c in digits_by_length[2][0] if count_occurrences(c, digits_by_length[6]) == 3][0]
    
    # find the left up, left down and middle segments based on occurrences in 4, 1 and the count of occurrences in five digit numbers
    candidates = set(strlist_chars(digits_by_length[4])).difference(strlist_chars(digits_by_length[2]))
    left_up = [c for c in candidates if count_occurrences(c, digits_by_length[5]) == 1][0]
    middle = [c for c in candidates if c != left_up][0]
    left_down = [c for c in strlist_chars(digits_by_length[5]) if count_occurrences(c, digits_by_length[5]) == 1 and c != left_up][0]
    # mark the last unmapped segment as down
    down = remove_all_characters("abcdefg", "".join([up,right_up,right_down,left_down,left_up,middle]))
    
    segment_mapping = {up: "a", left_up: "b", right_up: "c", middle: "d", left_down: "e", right_down: "f", down: "g"}
    return segment_mapping

def decode_number(output, segment_mapping):
    # decode the output strings into an actual number
    number_mapping = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf":"7", "abcdefg": "8", "abcdfg": "9"}
    
    numbers = []
    for digit in output:
        mapped_output = "".join(sorted([segment_mapping[c] for c in digit]))
        numbers.append(number_mapping[mapped_output])
    
    return int("".join(numbers))

if __name__ == "__main__":
    signals, outputs = parse_input("full-input.txt")
    print("Part I: ", part1(outputs))
    print("Part II: ", part2(signals, outputs))
