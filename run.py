#!/usr/bin/env python3

import argparse
import random
import sys
import subprocess
import os
from tqdm import tqdm
from pathlib import Path


def main():
    """
        Perform batch facial recognition using the Top-K accuracy metric, saving
        results to a text file.
    """
    arguments = parse_command_line_arguments()

    # Assign values from command-line arguments.
    source_directory = arguments.source_directory[0]
    database_path = arguments.database_path[0]
    k_value = arguments.k_value[0]
    model = arguments.model[0]
    output_file = arguments.output_file[0]

    # Select a random face photo from each identity (class), since
    # each identity can have multiple photos of themselves.
    results = get_an_image_from_each_class(source_directory)

    source_images_count = len(results)
    correct_predictions = 0

    # Display the source files.
    print('------------------------SOURCE FILES------------------------')
    for image in results:
        print(image)
    print('----------------------------------------------------------\n')

    # Create a new file with the accuracy metric displayed.
    out_file = open(output_file, mode='w')
    out_file.write('-------------------------------\n')
    out_file.write('TOP ' + str(k_value) + ' ACCURACY\n')
    out_file.write('-------------------------------\n')
    out_file.close()

    # Repeatedly perform face recognition for each source image.
    count = 1
    with tqdm(total=source_images_count) as progress_bar:
        for item in results:
            out_file = open(output_file, mode='a')
            out_file.write('\n' + str(count) + '.\n')
            out_file.close()

            correct_predictions += subprocess.call([sys.executable, 'identify-face.py', '-s', item, '-d', database_path, '-k', str(k_value), '-m', model, '-o', output_file])

            count += 1
            progress_bar.update(1)

    # Calculate the face recognition accuracy and write the percentage to the
    # end of the output file.
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

    parser.add_argument('-m', '--model', choices=['VGG-Face', 'Facenet512', 'ArcFace', 'SFace', 'Ensemble'], nargs=1, required=True,
                        help='Face recognition model to use.')

    parser.add_argument('-o', '--output_file', nargs=1, required=True,
                        help='Output file to write accuracy results to (Ex. "output.txt")')

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def get_an_image_from_each_class(source_directory: str) -> list:
    """
    Args:
        source_directory (str): the path to a face dataset

    Returns:
        (list): a list containing one face image from every class of the dataset
    """
    selected_images = []

    for root, directories, files in os.walk(source_directory):
        if not files: continue

        random_file = random.choice(files)
        if not random_file.endswith('.pkl'): # ignore serialized file containing face representations
            selected_images.append(str(root) + '/' + random_file)

    return selected_images


if __name__ == '__main__':
    main()
