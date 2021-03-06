# Setup Buttler

The setup buttler helps you manage your CI setup from the command line.

## Install and Run

```
# install the package
poetry install

# run to list all commands
poetry run python cli.py
```

## Jenkins Commands

Add a job and assign it to a view (the view is created if it doesn't exist):

```
poetry run python cli.py create-job <job-name> <view-name>
```

Add new view:

```
poetry run python cli.py create-view <view-name>
```

Show Jenkins version:

```
poetry run python cli.py show-version
```
