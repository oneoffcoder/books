#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOCKER="${DOCKER:-docker}"
IMAGE="${IMAGE:-book-pytorch-intro-check:local}"
CACHE_DIR="${CACHE_DIR:-${REPO_ROOT}/sphinx/pytorch-intro/build/notebook-cache}"

mkdir -p "${CACHE_DIR}"

DATASETS=("$@")
if [[ "${#DATASETS[@]}" -eq 0 ]]; then
    DATASETS=(mnist fashionmnist kmnist qmnist cifar10 stl10 svhn usps)
fi

"${DOCKER}" run --rm \
    -v "${CACHE_DIR}:/workspace/cache" \
    -e PYTORCH_INTRO_DATA_DIR=/workspace/cache/data \
    -e TORCH_HOME=/workspace/cache/torch \
    -e PYTORCH_INTRO_PRELOAD_DATASETS="${DATASETS[*]}" \
    "${IMAGE}" \
    python - <<'PY'
import os
from pathlib import Path
from torchvision import datasets

base_dir = Path(os.environ["PYTORCH_INTRO_DATA_DIR"])
selected = os.environ["PYTORCH_INTRO_PRELOAD_DATASETS"].split()

def root(name):
    path = base_dir / name
    path.mkdir(parents=True, exist_ok=True)
    return str(path)

downloaders = {
    "mnist": lambda: datasets.MNIST(root=root("mnist"), download=True),
    "fashionmnist": lambda: datasets.FashionMNIST(root=root("fashionmnist"), download=True),
    "kmnist": lambda: datasets.KMNIST(root=root("kmnist"), download=True),
    "qmnist": lambda: datasets.QMNIST(root=root("qmnist"), download=True),
    "cifar10": lambda: datasets.CIFAR10(root=root("cifar10"), download=True),
    "stl10": lambda: datasets.STL10(root=root("stl10"), split="train", download=True),
    "svhn": lambda: datasets.SVHN(root=root("svhn"), split="train", download=True),
    "usps": lambda: datasets.USPS(root=root("usps"), download=True),
}

unknown = sorted(set(selected) - set(downloaders))
if unknown:
    names = ", ".join(unknown)
    supported = ", ".join(sorted(downloaders))
    raise SystemExit(f"Unsupported dataset(s): {names}. Supported: {supported}")

for name in selected:
    print(f"==> Downloading {name} into {base_dir}", flush=True)
    dataset = downloaders[name]()
    print(f"    {name}: {len(dataset)} examples", flush=True)
PY
