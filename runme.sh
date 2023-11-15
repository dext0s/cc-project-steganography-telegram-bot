#!/bin/bash

export TELEGRAM_BOT_TOKEN=$( cat token.txt )

python3 src/main.py