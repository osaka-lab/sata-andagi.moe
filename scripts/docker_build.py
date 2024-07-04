import sys
sys.path.insert(0, ".")

import os
from app import __version__

build_name = "r3tr0ananas/sata_andagi_moe"

os.system(
    f"docker build -t {build_name}:{__version__} --build-arg ARCH=amd64 ."
)

os.system(
    f"docker build -t {build_name}:latest --build-arg ARCH=amd64 ."
)