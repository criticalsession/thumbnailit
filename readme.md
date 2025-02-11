# THUMBNAILIT

ThumbnailIt is a command-line tool for extracting evenly spaced thumbnails from a video file and arranging them in a grid.

<img src="thumbnails_demo.png" alt="Demo" width="500" align="center" />

## Features
- Extracts a grid of thumbnails from a video file
- Customizable grid size (rows and columns)
- Optional timestamps on thumbnails
- Saves output as a single image

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Matplotlib
- tqdm

## Installation
Ensure you have Python installed, then install the required dependencies:

```sh
pip install opencv-python matplotlib tqdm
```

## Usage
Basic usage:
```sh
python thumbnailit.py <video_file>
```

### Optional Arguments
| Argument | Description |
|----------|-------------|
| `-o`, `--output` | Specify the output filename (default: `<input_filename>_thumbnails.png`) |
| `-r`, `--rows` | Number of rows in the thumbnail grid (default: 5) |
| `-c`, `--cols` | Number of columns in the thumbnail grid (default: 5) |
| `--show-time` | Display timestamps on thumbnails |

### Example
Extract thumbnails from `video.mp4`, create a 4x4 grid, and display timestamps:
```sh
python thumbnailit.py video.mp4 -r 4 -c 4 --show-time
```

## Output
The script will generate a single image file containing the extracted thumbnails and save it in the same directory as the input file (unless specified otherwise).
