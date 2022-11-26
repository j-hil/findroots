# the order here does matter. In particular autoflake must be first.
autoflake src
pydocstringformatter src
isort src
black src
