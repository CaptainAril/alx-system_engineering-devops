#!/usr/bin/env bash

SCRIPT_NAME=$( (basename "$0"))
echo "The name of this script is $SCRIPT_NAME"
ps -aef | grep $SCRIPT_NAME
# pgrep -l root $SCRIPT_NAME
echo $$
