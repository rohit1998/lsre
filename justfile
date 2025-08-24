# === VARIABLES ===

project_name := "learn-simple-regular-expressions"
docker_image_prod := project_name + "-prod"
docker_image_dev := project_name + "-dev"
github_owner := "rohit1998"
github_repo := "lsre"

# === ALIASES ===

alias c := check
alias p := pre-commit
alias r := run
alias b := new-branch-off-main
alias pu := push-branch
alias pr := create-branch-and-pr
alias cpr := create-pr
alias mpr := merge-pr
alias ad := all-devcontainer-verification
alias ah := all-host-verification

# === GENERAL ===

# general: list everything by default
[group('general')]
default:
    @just --list --unsorted --list-prefix "j " --alias-style separate

# general: uv run scripts/main.py
[group('general')]
run:
    uv run scripts/main.py

# === VERIFICATION COMMANDS ===

# verification: run all devcontainer verification commands
[group('verification')]
all-devcontainer-verification: pre-commit check build run

# verification: run all host verification commands
[group('verification')]
all-host-verification: all-devcontainer-verification docker-run-prod docker-run-dev-shell docker-compose-run-dev-shell

# === PRE-COMMIT ===

# pre-commit: uv run pre-commit run --all-files
[group('pre-commit')]
pre-commit:
    uv run pre-commit run --all-files

# === DOCKER ===

# docker: build prod docker image
[group('docker')]
docker-build-prod:
    docker build \
    -t {{docker_image_prod}} \
    --target prod .

# docker: build prod docker image without cache
[group('docker')]
docker-build-prod-nocache:
    docker build \
    -t {{docker_image_prod}} \
    --no-cache \
    --pull \
    --target prod .

# docker: build and run prod docker container
[group('docker')]
docker-run-prod: docker-build-prod
    docker run \
    -it {{docker_image_prod}}

# docker: build and run shell in prod docker container
[group('docker')]
docker-run-prod-shell: docker-build-prod
    docker run \
    -it {{docker_image_prod}} /bin/bash

# docker: build dev docker image
[group('docker')]
docker-build-dev:
    docker build \
    --build-arg APP_UID=$(id -u) \
    --build-arg APP_GID=$(id -g) \
    -t {{docker_image_dev}} \
    --target dev .

# docker: build dev docker image without cache
[group('docker')]
docker-build-dev-nocache:
    docker build \
    --build-arg APP_UID=$(id -u) \
    --build-arg APP_GID=$(id -g) \
    -t {{docker_image_dev}} \
    --no-cache \
    --pull \
    --target dev .

# docker: build and run shell in dev docker container
[group('docker')]
docker-run-dev-shell: docker-build-dev
    docker run \
    -v .:/home/appuser/app \
    -v /home/appuser/app/.venv/ \
    -it {{docker_image_dev}} /bin/zsh

# === DOCKER COMPOSE ===

# docker-compose: stop all running containers
[group('docker-compose')]
docker-compose-down:
    docker compose down

# docker-compose: build and run all containers
[group('docker-compose')]
docker-compose-up: docker-compose-down
    docker compose up --build

# docker-compose: run shell in dev container
[group('docker-compose')]
docker-compose-run-dev-shell:
    docker compose run -it dev_service /bin/zsh

# === CODE CHECKS ===

# code-check: uv lock --locked
[group('code-check')]
lock-check:
    uv lock --locked

# code-check: uv run ruff check
[group('code-check')]
lint-check:
    uv run ruff check

# code-check: uv run ruff format --check
[group('code-check')]
format-check:
    uv run ruff format --check

# code-check: uv run pyright
[group('code-check')]
type-check:
    uv run pyright

# code-check: uv run pytest
[group('code-check')]
test:
    uv run pytest

# code-check: Run all checks
[group('code-check')]
check: lock-check lint-check format-check type-check test docs-build

# === BUILDS ===

# build: uv build after all checks
[group('build')]
build: check
    uv build

# === CODE FIXES ===

# code-fix: uv run ruff check --fix
[group('code-fix')]
lint:
    uv run ruff check --fix

# code-fix: uv run ruff format
[group('code-fix')]
format:
    uv run ruff format

# === DOCS ===

# docs: mkdocs serve
[group('docs')]
docs-serve:
    uv run mkdocs serve

# docs: mkdocs build
[group('docs')]
docs-build:
    uv run mkdocs build

# === GIT ===

# git: checkout main and pull latest changes
[group('git')]
checkout-and-pull-main:
    #!/usr/bin/env bash
    set -euo pipefail
    if git checkout main; then
        git pull
    else
        git stash
        git checkout main
        git pull
        git stash pop --index
    fi

# git: put changes in new branch based off main
[group('git')]
new-branch-off-main branch-name: checkout-and-pull-main
    git checkout -b {{branch-name}}

# git: add commit and push all changes to current branch remote
[group('git')]
push-branch commit-message:
    git commit -m "{{commit-message}}"
    git push

# git: create new branch based off main and push changes to remote
[group('git')]
push-new-branch-off-main branch-name commit-message: (new-branch-off-main branch-name) (push-branch commit-message)

# === GITHUB ===

# github: create pull request for current branch
[group('github')]
create-pr:
    gh pr create --fill

# github: create branch and pr
[group('github')]
create-branch-and-pr branch-name commit-message=branch-name: (push-new-branch-off-main branch-name replace(commit-message, '-', ' ')) (create-pr)

# github: set pr to merge with main
[group('github')]
merge-pr:
    #!/usr/bin/env bash
    set -euo pipefail

    gh pr merge --rebase
    branch=$(git rev-parse --abbrev-ref HEAD)
    just checkout-and-pull-main

    case "$branch" in
        main|master|develop|HEAD)
            echo "Refusing to delete protected branch: $branch"
            exit 0
            ;;
        *)
            git branch -D "$branch"
            ;;
    esac
