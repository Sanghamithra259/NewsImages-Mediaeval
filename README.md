NewsImages-MediaEval 2025 Submission

Group Name: SyntaxError404
Approach Name: Retrieval

Overview

This repository contains our submission for the NewsImages Challenge at MediaEval 2025. The goal of the challenge is to provide relevant image recommendations for a given news article. We implemented an image retrieval pipeline using CLIP-style embeddings and a learned projection.

The submission includes:

Retrieval results for the small subtask (30 articles)

Retrieval results for the large subtask (all 8,501 articles)

Scripts used to generate embeddings, train the projection, and create the final submission images

mediaeval-project/
│
├─ data/                       # Dataset (CSV files and original images)
│   ├─ newsarticles.csv
│   ├─ subset.csv
│   └─ newsimages/             # Original JPG images
│
├─ features/                   # Generated embeddings and trained projection
│   ├─ text_embeds.npy
│   ├─ text_ids.npy
│   ├─ image_embeds.npy
│   ├─ image_ids.npy
│   └─ projection_ckpt.pt
│
├─ output/                     # (Optional) intermediate outputs
│   └─ retrieved_images/
│
├─ submission/                 # Final images for submission (PNG)
│   ├─ RET_Retrieval_SMALL/
│   └─ RET_Retrieval_LARGE/
│
├─ generate_submission.py      # Script to convert retrieved images to PNGs
├─ run_retrieval.py            # Script to perform retrieval
├─ dataset.py                  # Dataset loading & embedding generation
├─ requirements.txt            # Python dependencies
└─ utils/
    ├─ config.py
    └─ other utility files

Submission Format

File naming convention: [articleID]_[GroupName]_[ApproachName].png
Example: 117_SyntaxError404_Retrieval.png

Image size: 460x260 pixels (landscape)

Approach naming: RET_Retrieval_SMALL and RET_Retrieval_LARGE

Notes

Only one image per article ID is provided.

The code is modular: you can replace the retrieval pipeline with a generative approach (GEN) if needed.

Original images are included in data/newsimages/ but are not part of the submission.
