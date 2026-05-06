import os
import shutil

STAGING_DIR = 'staging_area'
PUBLISHED_DIR = 'published_code'

# Ensure the published directory exists
os.makedirs(PUBLISHED_DIR, exist_ok=True)

# Get a list of all files currently in the staging area
files = [f for f in os.listdir(STAGING_DIR) if os.path.isfile(os.path.join(STAGING_DIR, f))]

if not files:
    print("All files have been published! The staging area is empty.")
    exit(0)

# Pick the first file in the list
file_to_move = files[0]
src = os.path.join(STAGING_DIR, file_to_move)
dest = os.path.join(PUBLISHED_DIR, file_to_move)

# Move the file
shutil.move(src, dest)
print(f"Successfully moved {file_to_move} to {PUBLISHED_DIR}")