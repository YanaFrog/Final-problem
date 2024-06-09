import re
import cv2
from pathlib2 import Path
from glob import glob

data_path = Path('E:/Python/Task_Astrocytes')
def GetEvents(folder):
    file_mask = data_path / folder / 'events' / '*.png'
    file_names = glob(str(file_mask))
    file_names.sort(key=lambda x: int(re.search('event_t(\d+)\.png', x).group(1)))
    images = []
    for i in file_names:
        I = cv2.imread(str(i), 0)
        images.append(I)
    return images
def GetImages(folder):
    file_mask = data_path / folder / 'images' / '*.png'
    file_names = glob(str(file_mask))
    file_names.sort(key=lambda x: int(re.search('smoothed_t(\d+)\.png', x).group(1)))
    images = []
    for i in file_names:
        I = cv2.imread(str(i), 0)
        images.append(I)
    return images