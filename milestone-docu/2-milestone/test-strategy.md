# Test setup and considerations:

## Task manager and est runner
For the runner and manager I'm using [Poetry](https://python-poetry.org/) as it properly manages [PEP-518](https://peps.python.org/pep-0518) for Python dependencies.

## Assertions 

As an assertion library I'm using the standard assertion library from python.

## App linting 

Pylint to check linting follows [PEP-8](https://peps.python.org/pep-0008/), [PEP-518]https://peps.python.org/pep-0518 and [PEP-257](https://peps.python.org/pep-0257/). (In Progress).

## Telegram bot testing

The [Telegram Bot](https://docs.python-telegram-bot.org/en/v20.6/testing.html) library already ran a great amount of of tests that can be [found here](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/tests). So as we aren't doing any manipulation of the default clases or code, just adding functionallity we will asume there is no need to further test that code. We will, of course, test the rest of functionalities.