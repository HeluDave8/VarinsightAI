import fiftyone.utils.huggingface as fouh
import fiftyone as fo

name = "dacl10k"

# 如果数据集已存在，跳过下载（避免覆盖已有的 tags 和 Saved Views）
if name not in fo.list_datasets():
    dataset = fouh.load_from_hub(
        "Voxel51/dacl10k",
        name=name,
        persistent=True,
    )
    print(f"📥 已从 Hugging Face Hub 下载数据集 '{name}'。")
else:
    print(f"✅ 数据集 '{name}' 已存在，跳过下载。")

dataset = fo.load_dataset(name)

print(dataset.get_field_schema())

session = fo.launch_app(dataset)
session.wait()
