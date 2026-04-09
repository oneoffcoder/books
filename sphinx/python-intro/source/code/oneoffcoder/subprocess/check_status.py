import subprocess

try:
    subprocess.run(
        ['python3', '-c', 'import sys; sys.exit(1)'],
        check=True,
    )
except subprocess.CalledProcessError as exc:
    print(f'command failed with status {exc.returncode}')
