read -p "Insira o commit: " tag


git add .
git commit -m "$tag"
git push -u origin main