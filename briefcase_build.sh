#!/bin/bash

set -e

echo "🛠️  Cleaning..."
briefcase clean android

echo "📦 Creating app scaffolding..."
briefcase create android

echo "🔨 Building APK..."
briefcase build android

echo "🚀 Ready to run (connect your device or emulator)..."
briefcase run android
