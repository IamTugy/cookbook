#!/bin/sh
echo "Running Linter";
poetry run flake8 .
if [ $? -eq 0 ]; then
    echo "Linter Passed Successfully"
else
    echo "Linter Has Failed"
    exit 1
fi
