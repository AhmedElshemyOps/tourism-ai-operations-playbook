# Upload to GitHub

## Recommended method: GitHub website

1. Sign in to GitHub.
2. Create a new **public** repository named `tourism-ai-operations-playbook`.
3. Do not initialise it with another README, licence or `.gitignore`; those files are already included.
4. Extract this ZIP on your computer.
5. Open the extracted repository folder.
6. On the empty GitHub repository page, choose **uploading an existing file**.
7. Drag all files and folders from inside the extracted folder into GitHub. Upload the contents, not the outer ZIP file.
8. Commit with the message: `Publish Tourism AI Operations Playbook v1.0.0`.
9. Open the Actions tab and confirm that **Repository Quality** passes.
10. Configure the repository details using `GITHUB-REPOSITORY-SETTINGS.md`.
11. Enable GitHub Pages from the `main` branch and `/docs` folder.
12. Create the `v1.0.0` release using `release-notes/v1.0.0.md`.
13. Pin the repository to your GitHub profile.

## Alternative method: Git command line

```bash
git init
git add .
git commit -m "Publish Tourism AI Operations Playbook v1.0.0"
git branch -M main
git remote add origin YOUR_NEW_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_NEW_REPOSITORY_URL` with the URL GitHub shows after you create the empty repository.

## After publishing

Add the repository link to:

- your Ahmed Quality Ops website;
- LinkedIn Featured section;
- CV under Selected Tourism and Technology Products;
- job applications relevant to tourism operations, product, quality or AI adoption.
