import fiftyone as fo

dataset = fo.load_dataset("dacl10k")

subset = dataset.take(500, seed=42)

session = fo.launch_app(subset)
session.wait()