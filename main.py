import os
import sys

import cv2
import matplotlib.pyplot as plt
import math

from tqdm import tqdm

thumbnail_rows = 5
thumbnail_cols = 5
total_thumbnails = thumbnail_rows * thumbnail_cols

if len(sys.argv) < 2 or sys.argv[1] == '':
    print('Please provide a file to extract thumbnails from (python main.py <file>)')
    print()
    sys.exit()

input_file = sys.argv[1]
output_name = os.path.splitext(input_file)[0] + '_thumbnails.png'
print(f'Reading file: {input_file}')

cap = cv2.VideoCapture(input_file)

# get metadata
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'Total frames: {total_frames}')
frame_gap = math.floor(total_frames / total_thumbnails)

fps = cap.get(cv2.CAP_PROP_FPS)
print(f'Frames per second: {fps:0.2f}')

# pull thumbnails
print()
print(f'Extracting thumbnails every {frame_gap} frames')
fig, axs = plt.subplots(thumbnail_rows, thumbnail_cols, figsize=(30,20))
axs = axs.flatten()

# Adjust the spacing between subplots
plt.subplots_adjust(
    wspace=0.1,    # horizontal space between subplots
    hspace=0.2,    # vertical space between subplots
    left=0.02,     # left margin
    right=0.98,    # right margin
    top=0.95,      # top margin
    bottom=0.05    # bottom margin
)
img_idx = 0
for frame in tqdm(range(total_frames), desc='Processing frames', unit='frames'):
    ret, img = cap.read()
    if not ret:
        break

    if frame % frame_gap == 0 and img_idx < total_thumbnails:
        # Calculate timestamp
        seconds = frame / fps
        minutes = int(seconds // 60)
        seconds = seconds % 60
        timestamp = f'{minutes:02d}:{seconds:05.2f}'

        axs[img_idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[img_idx].set_title(f'Time: {timestamp}')
        axs[img_idx].axis('off')
        img_idx += 1

# Clear any unused subplot spaces
for i in range(img_idx, len(axs)):
    axs[i].axis('off')

plt.savefig(output_name, dpi=300)
print(f'Saved thumbnails to: {output_name}')
plt.close()
cap.release()