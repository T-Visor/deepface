# For reference: https://pypi.org/project/deepface/
from PIL import Image
from numpy import asarray
from deepface import DeepFace
from matplotlib import pyplot
import sys
import argparse




def main():
    # Optional arguments for DeepFace.
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

    arguments = parse_command_line_arguments()
    source_image = arguments.source_image[0]
    database_path = arguments.database_path[0]

    print(source_image)


    #df = DeepFace.find(img_path = "",
    #                   db_path = "",
    #                   detector_backend = backends[3])
    #print(df.to_string())




def parse_command_line_arguments():
    """ 
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        the parser with command-line arguments
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




if __name__ == '__main__':
    main()
