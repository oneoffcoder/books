#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOCKER="${DOCKER:-docker}"
IMAGE="${IMAGE:-book-scikit-intro-check:local}"
SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/sphinx/scikit-intro/source}"
OUTPUT_DIR="${OUTPUT_DIR:-${REPO_ROOT}/sphinx/scikit-intro/build/executed-notebooks}"
CACHE_DIR="${CACHE_DIR:-${REPO_ROOT}/sphinx/scikit-intro/build/notebook-cache}"
KERNEL_NAME="${KERNEL_NAME:-python3}"
EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT:-1800}"
SCIKIT_INTRO_CHECK_MODE="${SCIKIT_INTRO_CHECK_MODE:-1}"
SCIKIT_INTRO_RUN_REMOTE_DATASETS="${SCIKIT_INTRO_RUN_REMOTE_DATASETS:-0}"

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

"${DOCKER}" build -t "${IMAGE}" "${REPO_ROOT}" -f "${SCRIPT_DIR}/Dockerfile" >/dev/null

"${DOCKER}" run --rm \
    -v "${SOURCE_DIR}:/workspace/source:ro" \
    -v "${OUTPUT_DIR}:/workspace/output" \
    -v "${CACHE_DIR}:/workspace/cache" \
    -e KERNEL_NAME="${KERNEL_NAME}" \
    -e EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT}" \
    -e NOTEBOOKS="${NOTEBOOK_ARGS[*]:-}" \
    -e SCIKIT_INTRO_CHECK_MODE="${SCIKIT_INTRO_CHECK_MODE}" \
    -e SCIKIT_INTRO_RUN_REMOTE_DATASETS="${SCIKIT_INTRO_RUN_REMOTE_DATASETS}" \
    -e SCIKIT_INTRO_DATA_DIR=/workspace/cache/data \
    "${IMAGE}" \
    bash -lc '
set -euo pipefail

rm -rf /workspace/run
mkdir -p /workspace/run
cp -a /workspace/source/. /workspace/run/

cd /workspace/run

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
    /workspace/.venv/bin/jupyter nbconvert \
        --to notebook \
        --execute "${notebook}" \
        --output "${notebook}" \
        --output-dir /workspace/output \
        --ExecutePreprocessor.kernel_name="${KERNEL_NAME}" \
        --ExecutePreprocessor.timeout="${EXECUTION_TIMEOUT}" \
        --ExecutePreprocessor.iopub_timeout="${EXECUTION_TIMEOUT}"
done
'
