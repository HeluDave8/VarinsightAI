import fiftyone.utils.huggingface as fouh
import fiftyone as fo

name = "dacl10k"

# If the dataset already exists, skip download (to avoid overwriting existing tags and Saved Views)
if name not in fo.list_datasets():
    dataset = fouh.load_from_hub(
        "Voxel51/dacl10k",
        name=name,
        persistent=True,
    )
    print(f"📥 Dataset '{name}' downloaded from Hugging Face Hub.")
else:
    print(f"✅ Dataset '{name}' already exists, skipping download.")

dataset = fo.load_dataset(name)

print(dataset.get_field_schema())

session = fo.launch_app(dataset)
session.wait()
