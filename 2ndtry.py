import fiftyone as fo

dataset = fo.load_dataset("dacl10k")

subset = dataset.take(1000, seed=42)

session = fo.launch_app(subset)
session.wait()