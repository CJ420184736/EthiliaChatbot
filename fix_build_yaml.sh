#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Moving good pyproject.toml up to ethilia/..."

# Move good file
mv ethilia/ethilia/pyproject.toml ethilia/pyproject.toml

# Remove old one if it somehow still exists
[ -f ethilia/ethilia/pyproject.toml ] && rm ethilia/ethilia/pyproject.toml

echo "📄 Rewriting codemagic.yaml..."
cat > codemagic.yaml <<EOF
workflows:
  build-ethilia-apk:
    name: Build Ethilia APK
    max_build_duration: 30
    environment:
      vars:
        BRIEFCASE_PLATFORM: android
    scripts:
      - name: Change directory into ethilia
        script: cd ethilia
      - name: Install Briefcase
        script: pip install -U briefcase
      - name: Build APK
        script: briefcase build android
      - name: Package APK
        script: briefcase package android
    artifacts:
      - ethilia/android/app/build/outputs/apk/**/*.apk
EOF

echo "💾 Committing and pushing to GitHub..."
git add codemagic.yaml ethilia/pyproject.toml
git commit -m "🔨 Fixed codemagic.yaml & moved valid pyproject.toml for Briefcase"
git push origin main

echo "✅ All done! Start a new build in Codemagic and you're good to go!"
