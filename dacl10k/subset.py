import fiftyone as fo

# load persisted dataset
dataset = fo.load_dataset("dacl10k")

# try to restore saved workspace
SAVED_VIEW_NAME = "workspace"

if dataset.has_saved_view(SAVED_VIEW_NAME):
    # restores the subset with all tags and progress intact
    subset = dataset.load_saved_view(SAVED_VIEW_NAME)
    print(f"✅ Restored Saved View '{SAVED_VIEW_NAME}' with all tags and progress intact ({len(subset)})。")
else:
    # first time running: create subset and persist it as a Saved View
    subset = dataset.take(1000, seed=42)
    # save the subset's sample IDs as a Saved View
    dataset.save_view(SAVED_VIEW_NAME, subset)
    print(f"📌 First time running, Saved View '{SAVED_VIEW_NAME}' created ({len(subset)} samples).")

# launch App
session = fo.launch_app(subset)

# block and wait for user interaction
session.wait()

# save the dataset to persist any changes (like tags or Saved Views) made in the App
dataset.save()
print("💾 Dataset saved.")

# If you click 'Save View' in the App to save a new view (e.g., filtered by labeled/unlabeled),
# you can list all saved views using the following method:
print(f"📋 All Current Saved Views: {dataset.list_saved_views()}")