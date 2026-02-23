#!/bin/bash
set -euo pipefail

OS_NAME="$(uname -s)"

case "$OS_NAME" in
  Darwin*)   PLATFORM="macos" ;;
  Linux*)    PLATFORM="linux" ;;
  MINGW*|MSYS*|CYGWIN*) PLATFORM="windows" ;;
  *)
    echo "Unsupported OS: $OS_NAME"
    exit 1
    ;;
esac

ICON_ARG=""

case "$PLATFORM" in
  macos)
    if [[ -f QANotz.icns ]]; then
      ICON_ARG="QANotz.icns"
    fi
    ;;
  windows)
    if [[ -f QANotz.ico ]]; then
      ICON_ARG="QANotz.ico"
    fi
    ;;
esac

pyinstaller --noconsole -n QANotz main.py --paths . --icon=$ICON_ARG --clean

case "$PLATFORM" in
  macos)
    mv dist/QANotz.app ./QANotz-macos.app
    ;;
  windows)
    mv dist/QANotz ./QANotz-windows
    ;;
  linux)
    mv dist/QANotz ./QANotz-linux
    ;;
esac

rm -rf build dist
ls -lh QANotz*