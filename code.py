"""First assignment.
"""
import argparse
import logging
import time
import string
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.WARNING)

def process(file_path, bool):
    """read text file and compile statistics
    """
    start_time = time.time()
    logging.info("Reading input file %s...", file_path)
    #with keyword and context manager
    with open(file_path) as input_file:
        text = input_file.read()
    num_chars = len(text)
    logging.info("Done. Number of characters is %d", num_chars)

    char_dict = {ch: 0 for ch in string.ascii_lowercase}

    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1

    num_letters = sum(char_dict.values())
    char_rdict = {ch: (num/num_letters)*100 for ch, num in char_dict.items()}
    for ch, num in char_rdict.items():
        print(f"{ch} -> {num:.3f}")

    if bool == False:
        elapsed_time = time.time() - start_time
        print(f"Done in {elapsed_time:.3f} seconds")

    else:
        fig = plt.figure()
        ax = plt.axes()
        plt.bar(char_rdict.keys(), char_rdict.values())
        plt.title('Relative frequencies of letters in text')
        plt.ylabel('Relative frequencies')
        ax.minorticks_on()
        ax.tick_params(axis='x', which='minor', bottom=False)

        elapsed_time = time.time() - start_time
        print(f"Done in {elapsed_time:.3f} seconds")
        plt.show()



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
