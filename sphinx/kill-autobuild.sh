#!/bin/bash

ps aux | grep 'python -m' | grep -v 'grep' | awk '{print $2}' | xargs sudo kill -9
