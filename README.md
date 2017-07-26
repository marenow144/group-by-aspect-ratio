# Group by aspect ratio

Groups photos by aspect ratio. Creates subfolder with grouped photos. Groups for 2x4, 3x2, 16x9, 1x1 and "others" if photo has another ratio. 

## Prerequisites
- Python 3.x
- Pillow (`pip install pillow`)

## Usage
```
python group.py --path=<source path> --target=<destination path>
```

- `--path=<source path>` is required. It should point to direcotry with photos
- `--target=<destination path>` is optional. If not given subfolders will be created in source path 