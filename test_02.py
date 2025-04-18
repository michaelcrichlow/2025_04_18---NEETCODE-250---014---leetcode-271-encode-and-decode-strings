# NOTE:
# Core Insight:
# 1.) You can use "{:4}".format(len(val)) to get how long each string is.
# 2.) I ended up using `str(len(val)).zfill(4)` because it made more sense to me.


def encode(l: list[str]) -> str:
    local_array = []
    for val in l:
        # length = "{:4}".format(len(val))
        length = str(len(val)).zfill(4)
        local_array.append(length + val)

    return "".join(local_array)

def decode(s: str) -> list[str]:
    local_array = []
    i = 0
    N = len(s)

    while i < N:
        length_of_word = int(s[i: i + 4])
        i += 4
        word = s[i: i + length_of_word]
        local_array.append(word)
        i += length_of_word

    return local_array

def main() -> None:
    test_strings = ["apple", "banana", "cherry", "dates"]
    encoded_string = encode(test_strings)
    final_strings = decode(encoded_string)
    assert(test_strings == final_strings)
    print("All asserts passed!")



if __name__ == '__main__':
    main()
