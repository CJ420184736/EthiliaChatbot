#!/usr/bin/env bash
set -e

echo "🚀 Starting repo fix..."

# 1. Ensure you're in the repo root with 'ethilia/' inside
if [ ! -d ethilia/ethilia ]; then
  echo "❌ Cannot find ethilia/ethilia folder. Make sure you're in the repo root."
  exit 1
fi

# 2. Move pyproject.toml and src to correct nested path for Briefcase
echo "➡️ Moving files into ethilia/ethilia/..."
mv ethilia/pyproject.toml ethilia/ethilia/ || true
mv ethilia/src ethilia/ethilia/ || true

# 3. Check structure is correct
echo "🛠 Verifying structure..."
tree ethilia/ethilia/ | sed -n '1,10p'

# 4. Rewrite codemagic.yaml for correct paths
echo "🛠 Updating codemagic.yaml..."
cat > codemagic.yaml <<EOF
workflows:
  build_ethilia_apk:
    name: Build Ethilia APK
    max_build_duration: 30
    environment:
      vars:
        BRIEFCASE_PLATFORM: android
    scripts:
      - name: Install Briefcase
        script: pip install -U briefcase
      - name: Build APK
        script: cd ethilia/ethilia && briefcase build android
      - name: Package APK
        script: cd ethilia/ethilia && briefcase package android
    artifacts:
      - ethilia/ethilia/android/app/build/outputs/apk/**/*.apk
EOF

# 5. Commit and push changes
echo "🗃 Staging and pushing updates..."
git add codemagic.yaml ethilia/ethilia/pyproject.toml ethilia/ethilia/src
git commit -m "🔧 Repo structure fixed + codemagic.yaml updated"
git push origin main --force

echo "✅ Done. Now start a new build in Codemagic!"
