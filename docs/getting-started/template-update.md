# Keeping your project updated with template

1. add and fetch template main as remote branch

    ```bash
    git remote add template-origin git@github.com:rohit1998/sample_python_project.git
    git fetch template-origin
    ```

1. Optional, manually eyeball changes

    ```bash
    git diff HEAD..template-origin/main
    ```

1. Check commit log of template and main branch.

    ```bash
    git log --pretty=format:"%h %ad %s" --date=format-local:"%Y-%m-%dT%H:%M:%SZ" | grep -E "Initial commit|Updating Project from Template"
    git log HEAD..template-origin/main --pretty=format:"%h %ad %s" --date=format-local:"%Y-%m-%dT%H:%M:%SZ"
    ```

1. Find all commits beyond the last template update date. Commit message will be either `Initial Commit` or `Updating Project from Template`. Copy all needed commit lines.

    ```bash
    # take raw commit lines, get hash sorted by time
    echo "git cherry-pick $(echo "<COMMIT_LINES>" | awk '{print $1}' | tac | tr '\n' ' ' | sed 's/ $//')"
    ```

1. Cherry pick commits to new branch

    ```bash
    just b template-update
    git cherry-pick <COMMIT_IDS>
    # if conflict happens resolve it and run
    git cherry-pick --continue

    # to abort
    git reset --hard
    git cherry-pick --abort
    ```

1. Raise a PR. Check all changes. Revert files via commit more changes if a particular change is not needed.
1. Close PR as a squash and use `Updating Project from Template` as message.
1. Remove remote origin

    ```bash
    git remote remove template-origin
    ```
