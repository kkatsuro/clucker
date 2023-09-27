#!/usr/bin/env bash

project_path='/home/meta/projects/clucker'

# @todo: this should work on every computer - relative path?
if [[ "$VIRTUAL_ENV" != "$project_path/venv" ]]; then
    . "$project_path/venv/bin/activate"
fi

main_window="$project_path/new-src/main_window.py"

pyside6-uic "$project_path/untitled.ui" > "$main_window"

# make QComboBoxChangeIndex possible
line_number="$(grep -m 1 --line-number "class" "$main_window" | sed 's/:.*$//g') "
sed -i "$line_number"'i\from QComboBoxChangeIndex import QComboBoxChangeIndex\n' "$main_window"
sed -i 's#QComboBox(#QComboBoxChangeIndex(#g' "$main_window"
