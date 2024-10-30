# How to make a Python Virtual Environment (Venv) (macOS)

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

# Installing packages in the Python

1. First, obviously, enter the python venv with `pyvenv`
2. Install some packages with `pip install [package]`!
3. Some packages to consider:
    - pygame