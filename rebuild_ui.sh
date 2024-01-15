#!/bin/bash

compile() {
    file="$1"
    new_file="src/"$(basename "$file" .ui)".py"
    echo "$file" \> "$new_file"
    pyside6-uic "$file" > "$new_file"
}

# this looks so terribly..  what do I even use bash for?
# https://stackoverflow.com/questions/4321456/find-exec-a-shell-function-in-linux
export -f compile
find ui-files/ -name '*.ui' -exec bash -c 'compile "$0"' {} \;
