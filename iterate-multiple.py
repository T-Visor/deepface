#!/usr/bin/env python3

import sys
import subprocess
import os
from tqdm import tqdm
from pathlib import Path



def main():
    arguments = parse_command_line_arguments()

    source_directory = arguments.source_directory[0]
    database_path = arguments.database_path[0]
    k_value = arguments.k_value[0]
    output_file = arguments.output_file[0]

    results = [os.path.join(dp, f) for dp, dn, fn in os.walk(source_directory) for f in fn]
    source_images_count = len(results)
    correct_predictions = 0

    # Create a blank file
    open(output_file, mode='w').close()

    with tqdm(total=source_images_count) as progress_bar:
        for item in results:
            returned = subprocess.call([sys.executable, 'run.py', '-s', item, '-d', database_path, '-k', k_value, '-o', output_file])
            progress_bar.update(1)

    out_file = open(output_file, mode='a')
    percentage = round(100 * float(correct_predictions) / float(source_images_count))
    percentage = str(percentage) + '%'
    out_file.write('\nAccuracy: ' + str(correct_predictions) + '/' + str(source_images_count) + ' (' + percentage + ')')




def parse_command_line_arguments() -> argparse.ArgumentParser:
    """
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        (argparse.ArgumentParser): the parser with command-line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--source_directory', nargs=1, required=True,
                        help='Directory with images of people to identify.')

    parser.add_argument('-d', '--database_path', nargs=1, required=True,
                        help='Dataset of images containing known faces.')

    parser.add_argument('-k', '--k_value', type=int, nargs=1, required=True,
                        help='Determines the value used for Top-K Accuracy.')

    parser.add_argument('-o', '--output_file', nargs=1, required=True,
                        help='Output file to write accuracy results to (Ex. "output.txt")')

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




if __name__ == '__main__':
    main()
