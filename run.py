#!/usr/bin/env python3

import argparse
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

    # Create a new file with the accuracy metric displayed.
    out_file = open(output_file, mode='w')
    out_file.write('-------------------------------\n')
    out_file.write('TOP ' + str(k_value) + ' ACCURACY\n')
    out_file.write('-------------------------------\n')
    out_file.close()

    count = 1
    with tqdm(total=source_images_count) as progress_bar:
        for item in results:
            out_file = open(output_file, mode='a')
            out_file.write('\n' + str(count) + '.\n')
            out_file.close()

            correct_predictions += subprocess.call([sys.executable, 'detect-face.py', '-s', item, '-d', database_path, '-k', str(k_value), '-o', output_file])

            count += 1
            progress_bar.update(1)

    out_file = open(output_file, mode='a')
    percentage = round(100 * float(correct_predictions) / float(source_images_count))
    percentage = str(percentage) + '%'
    out_file.write('\nAccuracy: ' + str(correct_predictions) + '/' + str(source_images_count) + ' (' + percentage + ')')
    out_file.close()




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
