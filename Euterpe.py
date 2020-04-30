"""
End goal functionality:
Input: The number of chords you want, the key, optional starting chord.
Output: Chord progressions in symbols and actual chord names (IV vs Cmaj).

Option to print out progression in every key?
"""
import random

major_input_alpha = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]

# rules = {
#     "I": ["ii", "iii", "IV", "V", "vi", "vii°"],
#     "ii": ["I", "V", "vii°"],
#     "iii": ["I", "IV", "vi"],
#     "IV": ["I", "ii", "V", "vii°"],
#     "V": ["I", "vi"],
#     "vi": ["I", "ii", "iii", "IV", "V", "vi", "vii°"],
#     "vii°": ["I"]
# }

rules = {
    1: [2, 3, 4, 5, 6, 7],
    2: [1, 5, 7],
    3: [1, 4, 6],
    4: [1, 2, 5, 7],
    5: [1, 6],
    6: [1, 2, 3, 4, 5, 7],
    7: [1]
}

keys = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "B"],
    "C#": ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#"],
    "D♭": ["D♭", "E♭m", "Fm", "G♭", "A♭", "B♭m", "C"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#"],
    "E♭": ["E♭", "Fm", "Gm", "A♭", "B♭", "Cm", "D"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#"],
    "F": ["F", "Gm", "Am", "B♭", "C", "Dm", "E"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#"],
    "G♭": ["G♭", "A♭m", "B♭m", "C♭", "D♭", "Em♭", "F"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#"],
    "A♭": ["A♭", "B♭m", "Cm", "D♭", "E♭", "Fm", "G"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#"],
    "B♭": ["B♭", "Cm", "Dm", "E♭", "F", "Gm", "A"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#"]
}


def step(start: int, count: int) -> [int]:
    prog = []
    next_chords = rules[start]
    prog.append(start)
    for index in range(count - 1):
        next_index = random.randrange(len(next_chords))
        the_chord = next_chords[next_index]
        prog.append(the_chord)
        next_chords = rules[the_chord]
    return prog


def get_key(prog: [int], key: str) -> str:
    sym_string = ""
    prog_string = ""
    if key in keys:
        key_list = keys[key]
        for chord in prog:
            sym_string = f"{sym_string} {major_input_alpha[chord - 1]}"
            prog_string = f"{prog_string} {key_list[chord - 1]}"
        str_rtn = f"{sym_string}\n{prog_string}"
    else:
        for chord in prog:
            sym_string = f"{sym_string} {major_input_alpha[chord - 1]}"
        str_rtn = f"{sym_string}"
    return str_rtn


def get_progression():
    chord_count = input("Enter length of progression: ")
    key = input("Enter the desired key: ")
    starting_chord = input("Enter starting chord: ")

    if starting_chord in major_input_alpha:
        progression = step(major_input_alpha.index(starting_chord)+1, int(chord_count))
    else:
        rand_start = random.randrange(7)
        progression = step(rand_start, int(chord_count))

    print("--------------------------------\n")
    print(get_key(progression, key))


get_progression()
