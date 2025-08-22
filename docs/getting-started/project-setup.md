# Steps on how to setup your project

1. Create a project repo on github based on [this](https://github.com/rohit1998/sample_python_project) template.
1. On this new repo, run the pr-checks workflow from Actions tab. Ensure everything passes.
1. Set settings for the repo to protect main branch.
    1. Settings → General settings as [follows](https://github.com/rohit1998/sample_python_project/settings). (except, do not tick template repository check)
    1. Settings → Branches → Create classic branch protection rule as [follows](https://github.com/rohit1998/sample_python_project/settings/branch_protection_rules/65469829).
1. Setup repo on your local.

    ```bash
    git clone git@github.com:rohit1998/<branch-name>.git
    ```

1. Open this repo in vscode.
1. Update .env file.

    ```bash
    cp .env.example .env
    ```

    >Note: in .env file, run command in comments above tagged as shell, in host shell and update values. For rest put whatever values you like.
1. Host development verification. Run this command.

    ```bash
    # pre-commit code-checks scripts/main.py
    # prod-docker dev-docker-shell dev-docker-compose-shell
    # see all just commands for details
    just ah # all-host
    ```

1. Rebuild and reopen project in container.
1. Docker development verification. Run these commands.

    ```bash
    # pre-commit code-checks scripts/main.py
    # see all just commands for details
    just ad # all devcontainer
    ```

    > Bonus: also go to `http://localhost:<LIVE_SERVER_PORT>/` and check your site/coverage html.
1. Update Files to follow your project name. Follow [this](https://github.com/rohit1998/rl-learn-code/pull/1/files) PR template to make changes.
1. Do the Docker development verification again. Run `just ad`
1. Close devcontainer.
1. Do the host development verification again. Run `just ah`
1. Rebuild and Reopen in container.
1. Raise PR.

    ```bash
    git checkout -b project-setup
    git add .
    git commit -m "project setup"
    git push
    ```

1. Check that pr-check workflow passes and rebase and merge.
1. Make sure to checkout main in local and pull changes.

# Some useful project commands

1. Clearing orphan branches from local

    ```bash
    git fetch --prune
    ```

1. Deleting other orphan branches

    ```bash
    # list branches
    git branch -a

    # WARNING delete branches except develop, master, main
    git branch | grep -v "develop" | grep -v "master" | grep -v "main" | xargs git branch -D

    ```
