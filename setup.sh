#!/bin/bash

mkdir -p mediaeval-project/{data/{images,captions,annotations},src/{retrieval,generation,evaluation},notebooks,results/{retrieval,generation,evaluation}}

touch mediaeval-project/README.md
touch mediaeval-project/requirements.txt
touch mediaeval-project/setup.sh

touch mediaeval-project/src/__init__.py
touch mediaeval-project/src/retrieval/__init__.py
touch mediaeval-project/src/retrieval/retrieval.py
touch mediaeval-project/src/retrieval/index.py
touch mediaeval-project/src/retrieval/utils.py

touch mediaeval-project/src/generation/__init__.py
touch mediaeval-project/src/generation/generation.py
touch mediaeval-project/src/generation/utils.py

touch mediaeval-project/src/evaluation/__init__.py
touch mediaeval-project/src/evaluation/evaluation.py
touch mediaeval-project/src/evaluation/metrics.py

touch mediaeval-project/src/config.py

touch mediaeval-project/notebooks/retrieval_demo.ipynb
touch mediaeval-project/notebooks/generation_demo.ipynb
touch mediaeval-project/notebooks/evaluation_demo.ipynb
