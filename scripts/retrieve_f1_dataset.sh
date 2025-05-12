#!/bin/bash

# Create a temporary directory for downloading the dataset
mkdir -p ../src/resources/tmp || { echo "Failed to create temporary directory"; exit 1; }

# Download the dataset from Kaggle
curl -L -o ../src/resources/tmp/f1_dataset.zip https://www.kaggle.com/api/v1/datasets/download/rohanrao/formula-1-world-championship-1950-2020 || { echo "Failed to download dataset"; exit 1; }

# Unzip the dataset into the target directory
unzip ../src/resources/tmp/f1_dataset.zip -d ../src/resources/f1_dataset || { echo "Failed to unzip dataset"; exit 1; }

# Clean up temporary files
rm -r ../src/resources/tmp/f1_dataset.zip || { echo "Failed to remove zip file"; exit 1; }
rm -rf ../src/resources/tmp || { echo "Failed to remove temporary directory"; exit 1; }

echo "Dataset successfully retrieved and extracted."