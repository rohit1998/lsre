# Steps to release package to pypi

1. Update all the changes to main.
1. Create a release branch

    > Note: For first setup you can skip this step and use default first version `0.1.0`.

    ```bash
    git checkout main
    git pull
    uv version --bump patch # patch, minor, major. note new version
    j pr release-<NEW_VERSION>
    # wait for pr-checks to pass
    j mpr
    ```

1. Create a new tag for release

    ```bash
    git checkout main
    git pull origin main
    git tag v<NEW_VERSION>
    git push origin v<NEW_VERSION>
    ```

1. Verify that release workflow passes in actions tab. Also verify the new version on pypi.
