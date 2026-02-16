#!/bin/bash

# Build the qanotz application using pyinstaller
pyinstaller --noconsole --onefile -n QANotz qanotz/__main__.py --paths .

# You can alternatively use 'pyinstaller QANotz.spec'