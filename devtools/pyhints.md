# Cheat sheet / hints for working in python

Basically just stuff I forget and don't want to look up:

| Action                  | Command                                                          |
| ----------------------- | ---------------------------------------------------------------- |
| Create venv             | `python -m venv .venv`                                           |
| Activate venv           | `.\.venv\Scripts\Activate.ps1`                                   |
| Run tests with coverage | `coverage run -m pytest ./tests; coverage report; coverage html` |
| Build package           | `python -m build`                                                |
| Publish on PyPi         | `python -m twine upload dist/*`                                  |

