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
      ICON_ARG="--icon=QANotz.icns"
    fi
    ;;
  windows)
    if [[ -f QANotz.ico ]]; then
      ICON_ARG="--icon=QANotz.ico"
    fi
    ;;

pyinstaller \
  --noconsole \
  -n QANotz \
  qanotz/__main__.py \
  --paths . \
  $ICON_ARG \
  --clean

case "$PLATFORM" in
  macos)
    mv dist/QANotz.app ./QANotz-macos.app
    ;;
  windows)
    mv dist/QANotz.exe ./QANotz-windows.exe
    ;;
  linux)
    mv dist/QANotz ./QANotz-linux
    ;;
esac

rm -rf build dist
ls -lh QANotz*