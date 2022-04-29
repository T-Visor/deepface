# For reference: https://pypi.org/project/deepface/
from PIL import Image
from numpy import asarray
from deepface import DeepFace
from matplotlib import pyplot
import sys
import argparse
import os

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
models = ['VGG-Face', 'Facenet', 'Facenet512', 'OpenFace', 'DeepFace', 'DeepID', 'ArcFace', 'Dlib']




def main():
    """
        Evaluate facial recognition performance
        using Top-1 accuracy.

        NOTE: This has only been tested on using the FaceScrub dataset.
    """
    arguments = parse_command_line_arguments()
    source_image = arguments.source_image[0]
    database_path = arguments.database_path[0]

    identities = []
    predicted_fileIDs = []
    predicted_labels = []

    results_dataframe = DeepFace.find(img_path = source_image,
                        db_path = database_path,
                        enforce_detection = False,
                        detector_backend = backends[3])

    # Get the first 'K' results from the facial recognition system.
    for i, row in results_dataframe.iloc[:4].iterrows():
        identities.append(row['identity'])

    # Extract labels and file IDs.
    #for identity in identities:
    #    predicted_fileIDs.append(extract_unique_fileID(str(identity)))
    #    predicted_labels.append(extract_label(str(identity)))

    predicted_labels, predicted_fileIDs = get_labels_and_fileIDs(identities)

    # Extract label and file ID from source image.
    true_label = extract_label(source_image)
    source_fileID = extract_unique_fileID(source_image)

    print(source_image, "\n")

    for identity in identities:
        print(identity)

    # TODO: remove entry from all predicted lists if a duplicate is found
    if source_fileID in predicted_fileIDs:
        print('source file in dataset')

        # Find the list element to remove
        for i in range(len(predicted_fileIDs)):
            if predicted_fileIDs[i] == source_fileID:
                identities.pop(i)

        predicted_labels, predicted_fileIDs = get_labels_and_fileIDs(identities)
    else:
        print('good to go')

    for label in predicted_labels:
        print(label)

    if true_label in predicted_labels:
        print('Made correct prediction!')
    else:
        print('Model mispredicted.')



    #predicted_label = extract_unique_fileID(str(closest_identity_file))
    #true_label = extract_unique_fileID(source_image)

    #print(predicted_label)
    #print(true_label)

    # Write results to a text file.
    #out_file = open('sample.txt', 'a')
    #out_file.write('=============================================\n')
    #out_file.write('source image: ' + os.path.basename(source_image) + '\n')
    #out_file.write('predicted: ' + predicted_label + ' \n')
    #out_file.write('true label: ' + true_label + '\n')
    #out_file.write('=============================================\n')
    #out_file.close()

    #if predicted_label == true_label:
    #    sys.exit(1)
    #else:
    #    sys.exit(0)




def parse_command_line_arguments() -> argparse.ArgumentParser:
    """ 
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        (argparse.ArgumentParser): the parser with command-line arguments
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



def get_labels_and_fileIDs(identities) -> tuple[list, list]:
    predicted_fileIDs = []
    predicted_labels = []

    # Extract labels and file IDs.
    for identity in identities:
        predicted_fileIDs.append(extract_unique_fileID(str(identity)))
        predicted_labels.append(extract_label(str(identity)))

    return predicted_labels, predicted_fileIDs




def extract_label(filename) -> str:
    """
    Args:
        filename (str): the filename to extract the label from

    Returns:
        (str): the label extracted from the given filename
    """
    directory_name = os.path.dirname(filename)
    label = os.path.basename(directory_name)
    return label




def extract_unique_fileID(filename):
    """
    Args:
        filename (str): the filename to extract the label from
    """
    # Extract the base file name.
    filename = os.path.basename(filename)

    # Remove the file extension.
    filename = os.path.splitext(filename)[0]

    # Handles Fawkes perturbated images.
    if ('_cloaked' in filename):
        filename = filename.rpartition('_')[0]

    # Handles Lowkey perturbated images.
    if ('_attacked' in filename):
        filename = filename.rpartition('.')[0]

    return filename




if __name__ == '__main__':
    main()
