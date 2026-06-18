import fiftyone as fo

dataset = fo.load_dataset("dacl10k")

view = dataset.load_saved_view("my_tagged_subset")

session = fo.launch_app(view)
session.wait()
