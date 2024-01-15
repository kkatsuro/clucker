#!/bin/bash

ps aux | grep "something, this was start of one of redbot tokens i was using" | awk '{print $2}' | xargs kill -9
