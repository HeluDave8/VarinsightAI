import fiftyone as fo
import fiftyone.operators as foo

dataset = fo.load_dataset("dacl10k")


compute_contrast = foo.get_operator(
    "@jacobmarks/image_issues/compute_contrast"
)

print("Computing contrast...")
compute_contrast(dataset)

print("Done!")
print(dataset.get_field_schema())