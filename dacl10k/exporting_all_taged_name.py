import fiftyone as fo
import os

# Load the existing dataset
dataset = fo.load_dataset("dacl10k")

base_export_dir = r"C:\Users\Besitzer\Desktop\datasets_overview\dacl10k"   # put your local computer's path here,where you want those to be saved

all_tags = dataset.distinct("tags")

for tag in all_tags:
    print(f"Exporting: {tag}")

    tagged_view = dataset.match_tags(tag)

    folder_name = tag.replace(" ", "_").replace("/", "_")

    export_dir = os.path.join(base_export_dir, folder_name)

    tagged_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.FiftyOneDataset,
        export_media=True,
    )

    print(f"✅ Exported {len(tagged_view)} samples to {export_dir}")
