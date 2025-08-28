# Setup git configuration
git config --global user.name "Rohit Gupta"
git config --global user.email "gupta.rohit21198@gmail.com"
git config --global push.default current
git config --global safe.directory /home/appuser/app

# add commit signing
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true

sudo chown -R appuser:appuser /home/appuser/commandhistory

# install project dependencies
uv sync --all-groups
