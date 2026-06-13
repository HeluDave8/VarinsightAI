import fiftyone as fo

dataset = fo.load_dataset("dacl10k")

view = dataset.sort_by("id")

total = len(view)
split = total // 3  # 2974

person1 = view.take(split)

 #Launch the App
session = fo.launch_app(person1)   

# Keep the app running
session.wait()