import fiftyone as fo
dataset = fo.load_dataset("dacl10k")

# Example how to export

#example of tag name from fiftyone
tag = "high quality image"

# tagged samples (kept)
tagged_view = dataset.match_tags(tag)

# untagged samples (correct way)
untagged_view = dataset.exclude_by("tags", tag)

export_directory_tagged = r"C:\Users\Besitzer\Desktop\datasets overiew\dacl10k\tagged" # write your pc path here where you want to save each tagged folder
export_directory_untagged = r"C:\Users\Besitzer\Desktop\datasets overiew\dacl10k\untagged"#

tagged_view.export(
    export_dir=export_directory_tagged,
    dataset_type=fo.types.FiftyOneDataset,
    export_media=True,
)

untagged_view.export(
    export_dir=export_directory_untagged,
    dataset_type=fo.types.FiftyOneDataset,
    export_media=True,
)

print(f"✅ Tagged exported: {len(tagged_view)} samples")
print(f"🚫 Untagged exported: {len(untagged_view)} samples")
