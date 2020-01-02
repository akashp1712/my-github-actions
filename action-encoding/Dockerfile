FROM python:3.8.1-alpine3.10

LABEL "com.github.actions.name"="Declare encoding"
LABEL "com.github.actions.description"="Automatically defined encoding at the top of your Python file and raise a pull reuqest"
LABEL "com.github.actions.icon"="corner-up-left"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/akashp1712/my-github-actions"
LABEL "homepage"=""
LABEL "maintainer"="Akash <akashp1712@gmail.com>"

ADD add_encoding.py /add_encoding.py
ENTRYPOINT ["python", "/add_encoding.py"]
