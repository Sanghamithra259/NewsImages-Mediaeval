import os
from PIL import Image
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

# -----------------------
# Configuration
# -----------------------
GROUP_NAME = "SyntaxError404"   # Your registered group name
APPROACH_NAME = "Retrieval"     # Your approach name

# Small & Large tasks
TASKS = {
    "SMALL": "data/subset.csv",        # CSV of small task article IDs
    "LARGE": "data/newsarticles.csv"   # CSV of all article IDs
}

RETRIEVAL_DIR = "output/retrieved_images"  # where your retrieval txts are
IMAGE_DATASET_DIR = "data/newsimages"     # original images folder
OUTPUT_BASE_DIR = "submission"            # final submission folder

# Target image size
TARGET_SIZE = (460, 260)

# Number of threads for parallel processing
NUM_THREADS = 8

# -----------------------
# Function to read article IDs from CSV
# -----------------------
def get_article_ids(csv_path):
    df = pd.read_csv(csv_path, header=None)
    # Assuming article_id is the first column
    return df.iloc[:, 0].astype(str).tolist()

# -----------------------
# Function to process a single article
# -----------------------
def process_article(article_id, task_dir):
    txt_filename = f"{article_id}_*.txt"
    matched_txt = [f for f in os.listdir(RETRIEVAL_DIR) if f.startswith(f"{article_id}_") and f.endswith(".txt")]
    if not matched_txt:
        print(f"Warning: No retrieval result for article {article_id}")
        return

    with open(os.path.join(RETRIEVAL_DIR, matched_txt[0]), "r") as f:
        retrieved_image_id = f.read().strip() + ".jpg"

    src_image_path = os.path.join(IMAGE_DATASET_DIR, retrieved_image_id)
    if not os.path.exists(src_image_path):
        print(f"Warning: Image {retrieved_image_id} not found for article {article_id}")
        return

    dest_image_name = f"{article_id}_{GROUP_NAME}_{APPROACH_NAME}.png"
    dest_image_path = os.path.join(task_dir, dest_image_name)

    # Open, resize, save as PNG
    try:
        img = Image.open(src_image_path).convert("RGB")
        img = img.resize(TARGET_SIZE)
        img.save(dest_image_path, format="PNG")
    except Exception as e:
        print(f"Error processing {article_id}: {e}")

# -----------------------
# Process each task in parallel
# -----------------------
for task_suffix, csv_path in TASKS.items():
    article_ids = get_article_ids(csv_path)
    task_folder = f"RET_{APPROACH_NAME}_{task_suffix}"
    final_dir = os.path.join(OUTPUT_BASE_DIR, task_folder)
    os.makedirs(final_dir, exist_ok=True)

    print(f"Processing {task_folder} with {len(article_ids)} articles...")

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(process_article, aid, final_dir) for aid in article_ids]
        for _ in as_completed(futures):
            pass  # just wait for all to complete

print(" Submission folders ready!")
