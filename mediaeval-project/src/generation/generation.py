import pandas as pd
import torch
from diffusers import StableDiffusionPipeline
import os
from utils import build_prompt

def generate_images(csv_path, output_dir):
    
    columns = [
        "article_id",
        "article_url",
        "article_title",
        "article_tags",
        "article_hash",
        "image_url"
    ]
    df = pd.read_csv(csv_path,names=columns)
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    os.makedirs(output_dir, exist_ok=True)

    for idx, row in df.iterrows():
        article_id = str(row['article_id'])
        headline = row['article_title']
        tags = row['article_tags']
        prompt = build_prompt(headline, tags)

        image = pipe(prompt).images[0]
        image = image.resize((460, 260))
        filepath = os.path.join(output_dir, f"{article_id}.png")
        image.save(filepath)
        print(f"Saved {filepath}")

if __name__ == "__main__":
    csv_path = "C:\\Users\\SAMYUKTHA\\mediaeval\\NewsImages-Mediaeval\\mediaeval-project\\data\\captions\\subset.csv"
    output_dir = "C:\\Users\\SAMYUKTHA\\mediaeval\\NewsImages-Mediaeval\\mediaeval-project\\results\\generation"
    generate_images(csv_path, output_dir)
