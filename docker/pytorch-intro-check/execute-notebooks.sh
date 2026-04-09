#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOCKER="${DOCKER:-docker}"
IMAGE="${IMAGE:-book-pytorch-intro-check:local}"
SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/sphinx/pytorch-intro/source}"
OUTPUT_DIR="${OUTPUT_DIR:-${REPO_ROOT}/sphinx/pytorch-intro/build/executed-notebooks}"
CACHE_DIR="${CACHE_DIR:-${REPO_ROOT}/sphinx/pytorch-intro/build/notebook-cache}"
KERNEL_NAME="${KERNEL_NAME:-python3}"
EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT:-1800}"
DOCKER_GPUS="${DOCKER_GPUS-all}"
PYTORCH_INTRO_REQUIRE_CUDA="${PYTORCH_INTRO_REQUIRE_CUDA:-1}"
PYTORCH_INTRO_RUN_REMOTE_DATASETS="${PYTORCH_INTRO_RUN_REMOTE_DATASETS:-0}"
PYTORCH_INTRO_CHECK_MODE="${PYTORCH_INTRO_CHECK_MODE:-1}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
    echo "Source directory not found: ${SOURCE_DIR}" >&2
    exit 1
fi

mkdir -p "${OUTPUT_DIR}" "${CACHE_DIR}"

NOTEBOOK_ARGS=("$@")

if [[ "${#NOTEBOOK_ARGS[@]}" -gt 0 ]]; then
    for notebook in "${NOTEBOOK_ARGS[@]}"; do
        if [[ ! -f "${SOURCE_DIR}/${notebook}" ]]; then
            echo "Notebook not found: ${SOURCE_DIR}/${notebook}" >&2
            exit 1
        fi
    done
fi

DOCKER_RUN_ARGS=(run --rm)

if [[ -n "${DOCKER_GPUS}" ]]; then
    DOCKER_RUN_ARGS+=(--gpus "${DOCKER_GPUS}")
fi

"${DOCKER}" "${DOCKER_RUN_ARGS[@]}" \
    -v "${SOURCE_DIR}:/workspace/source:ro" \
    -v "${OUTPUT_DIR}:/workspace/output" \
    -v "${CACHE_DIR}:/workspace/cache" \
    -e KERNEL_NAME="${KERNEL_NAME}" \
    -e EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT}" \
    -e NOTEBOOKS="${NOTEBOOK_ARGS[*]:-}" \
    -e PYTORCH_INTRO_DATA_DIR=/workspace/cache/data \
    -e TORCH_HOME=/workspace/cache/torch \
    -e PYTORCH_INTRO_REQUIRE_CUDA="${PYTORCH_INTRO_REQUIRE_CUDA}" \
    -e PYTORCH_INTRO_RUN_REMOTE_DATASETS="${PYTORCH_INTRO_RUN_REMOTE_DATASETS}" \
    -e PYTORCH_INTRO_CHECK_MODE="${PYTORCH_INTRO_CHECK_MODE}" \
    "${IMAGE}" \
    bash -lc '
set -euo pipefail

rm -rf /workspace/run
mkdir -p /workspace/run
cp -a /workspace/source/. /workspace/run/

cd /workspace/run
python - <<'"'"'PY'"'"'
import os
import subprocess
import sys

import torch

print(f"Python: {sys.version.split()[0]}")
print(f"PyTorch: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    current_device = torch.cuda.current_device()
    print(f"CUDA device {current_device}: {torch.cuda.get_device_name(current_device)}")

try:
    subprocess.run(["nvidia-smi"], check=True)
except FileNotFoundError:
    print("nvidia-smi is not available in this container.")
except subprocess.CalledProcessError as exc:
    raise SystemExit(exc.returncode) from exc

if os.environ.get("PYTORCH_INTRO_REQUIRE_CUDA") == "1" and not torch.cuda.is_available():
    raise SystemExit("CUDA is required for this check, but torch.cuda.is_available() is False.")
PY

notebooks=()

if [[ -n "${NOTEBOOKS}" ]]; then
    for notebook in ${NOTEBOOKS}; do
        notebooks+=("${notebook}")
    done
else
    mapfile -d "" notebooks < <(find . -maxdepth 1 -name "*.ipynb" ! -name "_*.ipynb" -print0 | sort -z)
    for i in "${!notebooks[@]}"; do
        notebooks[$i]="${notebooks[$i]#./}"
    done
fi

if [[ "${#notebooks[@]}" -eq 0 ]]; then
    echo "No notebooks selected for execution" >&2
    exit 1
fi

for notebook in "${notebooks[@]}"; do
    echo "==> Executing ${notebook}"
    jupyter nbconvert \
        --to notebook \
        --execute "${notebook}" \
        --output "${notebook}" \
        --output-dir /workspace/output \
        --ExecutePreprocessor.kernel_name="${KERNEL_NAME}" \
        --ExecutePreprocessor.timeout="${EXECUTION_TIMEOUT}" \
        --ExecutePreprocessor.iopub_timeout="${EXECUTION_TIMEOUT}"
done
'
