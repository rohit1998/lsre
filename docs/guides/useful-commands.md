# Useful commands

## Useful Just Commands

```bash
j # lists all just commands
jf <str> # finds <str> in just --list
jf alias #  gets all alias
```

## Some useful project commands

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

## Pyright node error

Try installing nvm and updating node version

```bash
# https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# add this to .bashrc/.zshrc
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

nvm install --lts
nvm use --lts
```
