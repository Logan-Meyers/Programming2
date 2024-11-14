# How to make a PyVenv, install packages, and make an alias

This will guide you through it all, for macOS and Ubuntu.

## Table of Contents:

- [macOS Venv Tutorial](#how-to-make-a-python-virtual-environment-venv-macos)
- [Ubuntu Venv Tutorial](#how-to-make-a-python-virtual-environment-venv-ubuntu)
- [Installing packages in the Python Venv](#installing-packages-in-the-python-venv)


## How to make a Python Virtual Environment (Venv) (macOS)

1. Make sure brew is installed, look here for how: [brew.sh](https://brew.sh/)
2. Update brew with `brew update && brew upgrade`
3. Install python via brew with `brew install python` or a specific verison with `brew install python@3.12`
4. cd into the folder to put the venv into, for example: `cd ~/Desktop/Programming2/PyVenv/`
5. Create the venv with `python3.12 -m venv venv`
6. Activate the venv for that terminal session with `source venv/bin/activate`
7. Add an alias to zshrc:
    1. Locate and open the .zshrc file, in the home directory. For example, at: `~/.zshrc`
    2. Add the following line in the file somewhere: `alias pyvenv="source ~/Desktop/Programming2/PyVenv/venv/bin/activate"`
8. You can deativate the venv with `deactivate`, obviously..

## How to make a Python Virtual Environment (Venv) (Ubuntu)

1. Update system packages with `sudo apt update %% sudo apt upgrade`
2. Install Python via the various methods:
    1. First, see if you can run python with `python`. If you enter the python environment, take note of the version and use `exit()`.
    2. If you are okay with the version installed, continue to step 3
    3. If not (or you can't enter the environment in the first place), add the python deadsnakes repository with `sudo add-apt-repository ppa:deadsnakes/ppa`, then install a specific version of python with, for example: `sudo apt install python3.12`
    4. Then make sure it can run with the corresponding command: `python3.12`
4. Make sure the corresponding venv package is installed for your python version, such as: `sudo apt install python3.12-venv`
3. cd into the folder to put the venv into, for example: `cd ~/Desktop/Programming2/PyVenv/`
5. Create the venv with `python3.12 -m venv venv`
6. Activate the venv for that terminal session with `source venv/bin/activate`
7. Add an alias to bashrc:
    1. Locate and open the .bashrc file, in the home directory. For example, at: `~/.bashrc`
    2. Add the following line in the file somewhere: `alias pyvenv="source ~/Desktop/Programming2/PyVenv/venv/bin/activate"`
    3. Restart terminal session for it to take effect
8. You can deativate the venv with `deactivate`, obviously..

## Installing packages in the Python Venv

1. First, obviously, enter the python venv with `pyvenv`
2. Install some packages with `pip install [package]`!
3. Some packages to consider adding:
    - pygame