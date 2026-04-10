#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOCKER="${DOCKER:-docker}"
IMAGE="${IMAGE:-book-spark-intro-check:local}"
SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/sphinx/spark-intro/source}"
OUTPUT_DIR="${OUTPUT_DIR:-${REPO_ROOT}/sphinx/spark-intro/build/executed-notebooks}"
KERNEL_NAME="${KERNEL_NAME:-python3}"
EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT:-2400}"
NBCONVERT_BIN="${NBCONVERT_BIN:-/opt/venv/bin/jupyter-nbconvert}"
HOST_UID="${HOST_UID:-$(id -u)}"
HOST_GID="${HOST_GID:-$(id -g)}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
    echo "Source directory not found: ${SOURCE_DIR}" >&2
    exit 1
fi

mkdir -p "${OUTPUT_DIR}"

NOTEBOOK_ARGS=("$@")

if [[ "${#NOTEBOOK_ARGS[@]}" -gt 0 ]]; then
    for notebook in "${NOTEBOOK_ARGS[@]}"; do
        if [[ ! -f "${SOURCE_DIR}/${notebook}" ]]; then
            echo "Notebook not found: ${SOURCE_DIR}/${notebook}" >&2
            exit 1
        fi
    done
fi

"${DOCKER}" run --rm \
    -v "${SOURCE_DIR}:/workspace/source:ro" \
    -v "${OUTPUT_DIR}:/workspace/output" \
    -e KERNEL_NAME="${KERNEL_NAME}" \
    -e EXECUTION_TIMEOUT="${EXECUTION_TIMEOUT}" \
    -e NBCONVERT_BIN="${NBCONVERT_BIN}" \
    -e HOST_UID="${HOST_UID}" \
    -e HOST_GID="${HOST_GID}" \
    -e NOTEBOOKS="${NOTEBOOK_ARGS[*]:-}" \
    "${IMAGE}" \
    bash -c '
set -euo pipefail

fix_output_owner() {
    chown -R "${HOST_UID}:${HOST_GID}" /workspace/output
}

trap fix_output_owner EXIT

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
    mapfile -d "" notebooks < <(find . -maxdepth 1 -name "*.ipynb" -print0 | sort -z)
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
    rm -rf /workspace/run/_spark_output /workspace/run/metastore_db /workspace/run/spark-warehouse /workspace/run/derby.log
    "${NBCONVERT_BIN}" \
        --to notebook \
        --execute "${notebook}" \
        --output "${notebook}" \
        --output-dir /workspace/output \
        --ExecutePreprocessor.kernel_name="${KERNEL_NAME}" \
        --ExecutePreprocessor.timeout="${EXECUTION_TIMEOUT}" \
        --ExecutePreprocessor.iopub_timeout="${EXECUTION_TIMEOUT}"
done
'
