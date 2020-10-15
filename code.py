"""First assignment.
"""
import argparse
import logging
import time
import string
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.WARNING)

def process(file_path, hist_bool, stats_bool):
    """read text file and compile statistics
    """
    start_time = time.time()
    logging.info("Reading input file %s...", file_path)
    #open file with keyword and context manager
    with open(file_path, 'r') as input_file:
        try:
            #reset counter to beginning of file
            input_file.seek(0)
            text = input_file.read()
            #work on statistics if required
            if stats_bool is True:
                input_file.seek(0)
                num_lines = sum(1 for line in input_file)
                num_chars = len(text)
                num_words = len(text.split())
                logging.info(num_words)
                logging.info(num_lines)
        except OSError as e:
            print('Cannot read file!!!\n{}'.format(e))
            return


    logging.info("Done.")

    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    #store counters as dictonary values
    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1

    num_letters = sum(char_dict.values())
    #create dictonary with relative values
    char_rdict = {ch: (num/num_letters)*100 for ch, num in char_dict.items()}
    for ch, num in char_rdict.items():
        print(f"{ch} -> {num:.3f}%")

    if stats_bool is True:
        print(f"""The numer of characters is {num_chars}, the number of words is
        {num_words}, while the number of lines is {num_lines}.""")

    if hist_bool is False:
        elapsed_time = time.time() - start_time
        print(f"Done in {elapsed_time:.3f} seconds")

    else:
        fig = plt.figure()
        ax = plt.axes()
        plt.bar(char_rdict.keys(), char_rdict.values())
        plt.title('Relative frequencies of letters in text')
        plt.ylabel('Relative frequencies (%)')
        ax.minorticks_on()
        #remove minorticks from x-axis
        ax.tick_params(axis='x', which='minor', bottom=False)

        elapsed_time = time.time() - start_time
        print(f"Done in {elapsed_time:.3f} seconds")
        plt.show()



#if the file is executed alone, __name__ == "__main__", otherwise it's not
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #add file path as positional argument,
    #with help message summarizing the usage
    help_message = """Insert path to text file: this program
                        is going to print  the relative frequence of each letter
                        of the alphabet in the book, without distinguishing
                        between lower and upper case."""
    parser.add_argument('infile', type=str, help=help_message)
    #add optional argument for printing histogram
    parser.add_argument('-histogram', action='store_true',
                    help='Print histogram of the frequencies')
    #add optional argument for printing stats
    parser.add_argument('-stats', action='store_true',
                    help='Print the basic book stats')
    args = parser.parse_args()
    process(args.infile, args.histogram, args.stats)
