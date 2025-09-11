#!/usr/bin/env bash
set -euo pipefail
APK=${1:-"android-app/app/build/outputs/apk/debug/app-debug.apk"}
adb install -r "$APK"
