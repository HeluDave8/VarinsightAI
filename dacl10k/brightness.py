import fiftyone as fo
import fiftyone.operators as foo

# Load the dataset (already downloaded)
dataset = fo.load_dataset("dacl10k")

# Get the compute_brightness operator
compute_brightness = foo.get_operator(
    "@jacobmarks/image_issues/compute_brightness"
)

# Run the operator on the full dataset
print("Computing brightness...")
compute_brightness(dataset)

print(f"Done! Brightness field added to {len(dataset)} samples.")
print(dataset.get_field_schema())

