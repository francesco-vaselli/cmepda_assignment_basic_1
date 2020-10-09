"""First assignment.
"""
import argparse
import logging
import time
import string


logging.basicConfig(level=logging.DEBUG)

def process(file_path, bool):
    """read text file and compile statistics
    """
    start_time = time.time()
    logging.info("Reading input file %s...", file_path)
    #with keyword and context manager
    with open(file_path) as input_file:
        text = input_file.read()
        print(type(text))
    num_chars = len(text)
    logging.info("Done. Number of characters is %d", num_chars)

    char_dict = {ch: 0 for ch in string.ascii_lowercase}

    elapsed_time = time.time() - start_time
    logging.info("Done in %.3f seconds", elapsed_time)
    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1

    num_letters = sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch} -> {num/num_letters:.3%}")

    if bool == True:
        print('yhea')


#if the file is executed alone, __name__ == "__main__", otherwise it's not
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #add file path as positional argument
    parser.add_argument('infile', type=str, help='Path to current file')
    #add optional argument for printing histogram
    parser.add_argument('-histogram', action='store_true',
                    help='Print histogram of the frequencies')
    args = parser.parse_args()
    process(args.infile, args.histogram)
