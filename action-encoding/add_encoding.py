# -*- coding: utf-8 -*-

import glob

path = 'the\\exact\\path'

# if given empty path, it starts from the current directory
files = [f for f in glob.glob("" + "**/*.py", recursive=True)]

encoding_line = "# -*- coding: utf-8 -*-"
for file in files:
    # add encoding in the python files
    with open(file, 'r+') as f:
        first_line = f.readline().strip()

        if first_line != encoding_line:
            content = f.read()
            f.seek(0, 0)
            f.write(encoding_line + '\n' + content)
