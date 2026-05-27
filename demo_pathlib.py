from pathlib import Path

# Create a path of current dire
p = Path('.')

# List of Sub directories in current dir
dirs = [x for x in p.iterdir() if x.is_dir()]


# List of Python files in current directory
py_files = list(p.glob('**/*.py'))
