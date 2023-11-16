# Test setup and considerations:

## Task manager

## Test runner

## Assertions 

## App build

In a future stage of the app the objective is to set up Poetry
To keep the requisites for the app we are following [PEP-518]https://peps.python.org/pep-0518.
This means the code will have a **pyproject.toml** which details the dependences.

## App linting 

Checking linting follows [PEP-8](https://peps.python.org/pep-0008/), [PEP-518]https://peps.python.org/pep-0518 and [PEP-257](https://peps.python.org/pep-0257/).

## Telegram bot testing

The Telegram Bot library already ran a great amount of of tests that can be [found here](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/tests). So as we aren't doing any manipulation of the default clases or code, just adding functionallity we will asume there is no need to further test that code. We will, of course, test the rest of functionalities.