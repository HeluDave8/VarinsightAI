import fiftyone as fo

dataset = fo.load_dataset("dacl10k")

view = dataset.take(1000, seed=42)

dataset.save_view("my_tagged_subset", view)
