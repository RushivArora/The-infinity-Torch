import argparse
import base64
import picamera
import json
"""
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.cloud import pubsub_v1
from google.cloud import storage
from google.cloud import translate
"""
from google.cloud import vision

path  = "/home/pi/desktop/image.jpg"

def detect_text_Bin_to_Hex(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
   
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    """
    
    print(hex(int(text,2)))
   
    print('Saving result to {} in bucket {}.'hex(int(text,2)),
                                                     bucket_name))
                                                     """

def main():
    detect_handwritten_ocr(path)
    detect_text(path)
    
    """Create a bucket with the following comand before running this code 'gsutil mb gs:'"""
