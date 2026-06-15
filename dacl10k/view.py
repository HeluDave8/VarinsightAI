import os
import fiftyone as fo
import pandas as pd

dataset = fo.load_dataset("dacl10k")

df = pd.read_csv(r"C:\Users\Besitzer\Desktop\varinsightAI\dacl10k\shared_subset.csv")

# extract only filenames from CSV
csv_names = set(os.path.basename(p) for p in df["filepath"])

# match by filename only
subset = dataset.match(
    lambda sample: os.path.basename(sample.filepath) in csv_names
)

print("Subset size:", len(subset))

session = fo.launch_app(subset)
session.wait()