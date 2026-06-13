import fiftyone as fo
import fiftyone.operators as foo
import os

# Increase operator timeout 
fo.config.operator_timeout = 3600  # 1 hour

dataset = fo.load_dataset("dacl10k")


compute_blurriness = foo.get_operator(
    "@jacobmarks/image_issues/compute_blurriness"
)



print("Computing blurriness...")
compute_blurriness(dataset)

print("Done!")
print(dataset.get_field_schema())