# R

## Install R

```bash
sudo apt update
sudo apt dist-upgrade
sudo apt install r-base
```

### Install Juypter kernel

```bash
R --version
R
install.packages('IRkernel')
IRkernel::installspec(name = 'ir36', displayname = 'R')
```