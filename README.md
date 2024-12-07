Python Resources and General Code snippets, also some unorganised general documents such as linux CLI referal documents, will add more as i go.

To ensure smooth synchronization between your local repository and GitHub, here’s a clear step-by-step guide for keeping your repository up to date and successfully reflecting changes:

## 1. Start on the Main Branch

Always start by ensuring you're on the main branch (or the default branch of your repo):

```git checkout main```

## 2. Pull the Latest Changes

Before making any changes locally, pull the latest updates from GitHub to avoid conflicts:

```git pull origin main```

## 3. Create a New Branch for Your Work

To keep the main branch clean and organized, create a new branch for your changes:

``git checkout -b feature/branch-name``

Replace feature/branch-name with something meaningful, e.g., update/documentation.

## 4. Make Changes Locally

Make your updates or add new files to your local repository. Use your editor of choice (like VS Code) to modify or create files.
## 5. Stage Your Changes

Once your changes are ready, stage them for the next commit:

```git add <file_path>```

Use ```git add .``` to stage all changes in your working directory.

## 6. Commit Your Changes

Commit the staged changes with a clear, descriptive message:

```git commit -m "Describe your changes here"```

## 7. Push the Branch

Push your branch to the remote repository:

```git push -u origin feature/branch-name```

## 8. Create a Pull Request on GitHub

Go to your GitHub repository in your browser.
Click on Compare & Pull Request (you'll see this option after pushing a branch).
Add details to the pull request and submit it for review.

## 9. Merge the Pull Request

Once the pull request is approved (or you're ready to merge it):

Merge the pull request via GitHub.
Switch back to the main branch locally:

```git checkout main```

Pull the latest updates to ensure your local main branch is up to date:

```git pull origin main```

## 10. Keep Your Local Repo Clean

After merging, you can delete old feature branches both locally and remotely:

- Delete locally:

```git branch -d feature/branch-name```

- Delete remotely:

```git push origin --delete feature/branch-name```

Quick Checklist for Any New Changes:

1. Start on main branch: ```git checkout main```
2. Pull latest changes: ```git pull origin mai```n
3. Create a branch: ```git checkout -b feature/branch-name```
4. Make changes: Modify or add files locally.
5. Stage changes: ```git add .```
6. Commit changes: ```git commit -m "Your message"```
7. Push changes: ```git push -u origin feature/branch-name```
8. Create and merge a pull request.
9. Pull updates to main after merge.

These steps ensure your workflow is clean, efficient, and always synchronized with GitHub.

