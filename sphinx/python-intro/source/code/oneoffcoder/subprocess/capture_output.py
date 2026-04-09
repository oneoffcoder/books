import subprocess

result = subprocess.run(
    ['python3', '-c', "print('captured output')"],
    capture_output=True,
    text=True,
    check=True,
)

print(result.stdout.strip())
