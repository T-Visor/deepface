# For reference: https://pypi.org/project/deepface/
from PIL import Image
from numpy import asarray
from deepface import DeepFace
from matplotlib import pyplot
import sys
import argparse
import os




def main():
    """
        Evaluate facial recognition performance
        using Top-1 accuracy.
    """
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

    arguments = parse_command_line_arguments()
    source_image = arguments.source_image[0]
    database_path = arguments.database_path[0]

    df = DeepFace.find(img_path = source_image,
                       db_path = database_path,
                       enforce_detection = False,
                       detector_backend = backends[3])

    # Get the first value under the 'identity' column.
    closest_identity_file = df['identity'].iloc[0]

    predicted_label = extract_label(str(closest_identity_file))
    true_label = extract_label(source_image)

    print('Top 1 Accuracy', end=', ')
    print('predicted:', predicted_label, end=', ')
    print('true label:', true_label)




def parse_command_line_arguments() -> argparse.ArgumentParser:
    """ 
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        (ArgumentParser): the parser with command-line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--source_image', nargs=1, required=True, 
                        help='Image of person to identify.')

    parser.add_argument('-d', '--database_path', nargs=1, required=True, 
                        help='Dataset of images containing faces.')

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




def extract_label(filename) -> str:
    """
    Args:
        filename (str): the filename to extract the label from

    Returns:
        (str): the label extracted from a given filename
    """
    # Extract the base file name.
    filename = os.path.basename(filename)

    # Remove the file extension.
    filename = os.path.splitext(filename)[0]

    # Remove the identifier
    filename = filename.rpartition('_')[0]

    return filename




if __name__ == '__main__':
    main()
