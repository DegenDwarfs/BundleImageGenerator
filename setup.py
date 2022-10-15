from pathlib import Path
import config

directory = config.bundles_dir
print("Directory Created:" + directory)
Path(directory).mkdir(parents=True, exist_ok=True)
