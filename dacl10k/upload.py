import fiftyone.utils.huggingface as fouh
import fiftyone as fo

name = "dacl10k"

dataset = fouh.load_from_hub(
    "Voxel51/dacl10k",
    name=name,
    persistent=True,
    overwrite=True
)



dataset = fo.load_dataset("dacl10k")

print(dataset.get_field_schema())

session = fo.launch_app(dataset)
session.wait()