# C#

This directory currently contains C# sample code under `IntroCode/`.

Unlike the active Sphinx books in this repository, `sphinx/csharp` is not yet wired into the standard per-book Sphinx build workflow. There is no local `Makefile`, `pyproject.toml`, or `source/` docs tree here yet.

## Contents

- `IntroCode/`: C# solution and related sample projects
- `README.md`: notes for working with the directory

## Tooling

Install a current .NET SDK for normal development:

- [.NET](https://dotnet.microsoft.com/download)

Some older project layouts may also benefit from Mono on Linux:

- [Mono](https://www.mono-project.com/download/stable/)

## Working With The Solution

Build the solution from this directory:

```bash
dotnet build IntroCode/IntroCode.sln
```

If this directory is later promoted into a full Sphinx book, it should gain the same `Makefile`-driven workflow used by the other books under `sphinx/`.
