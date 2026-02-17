#!/bin/bash

# Get OS name for future use

OS_NAME=$(uname -s)

# Build the qanotz application using pyinstaller
# You can alternatively use 'pyinstaller QANotz.spec'
pyinstaller --noconsole -n QANotz qanotz/__main__.py --paths . --icon=QANotz.icns --clean

# Move the genereated file to the root directory

case "$OS_NAME" in
    "Darwin"*|"Mac"*|"Apple"*|"macOS"*)
        mv dist/QANotz.app ./
        ;;
    "CYGWIN"*|"MSYS"*|"MINGW"*|*"WindowsNT"*)
        mv dist/QANotz ./
        ;;
    *)
        echo "Unsupported OS: $OS_NAME"
        exit 1
        ;;
esac

# Clean up build artifacts

rm -rf build dist