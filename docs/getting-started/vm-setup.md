# New VM Setup

1. Update VM

    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```

1. Install docker from docker [docs](https://docs.docker.com/engine/install/debian/#install-using-the-repository)
1. Generate a new ssh key from github [docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) (use `ed25519`)
1. Add it to github from github [docs](https://github.com/settings/keys) (both `authentication` and `signing`)
1. Setup Your github

    ```bash
    # Setup git configuration
    git config --global user.name "Rohit Gupta"
    git config --global user.email "gupta.rohit21198@gmail.com"
    git config --global push.default current

    # add commit signing
    git config --global gpg.format ssh
    git config --global user.signingkey ~/.ssh/id_ed25519.pub
    git config --global commit.gpgsign true

    # Install GitHub CLI
    (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
        && sudo mkdir -p -m 755 /etc/apt/keyrings \
        && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        && cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
        && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
        && sudo mkdir -p -m 755 /etc/apt/sources.list.d \
        && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
        && sudo apt update \
        && sudo apt install gh -y
    ```

1. Run these commands to setup shell

    ```bash
    # Install useful packages
    sudo apt install -y sudo
    sudo apt install -y wget
    sudo apt install -y zsh
    sudo apt install -y vim
    sudo apt install -y git
    sudo apt install -y curl
    sudo apt install -y unzip
    sudo apt install -y pre-commit
    sudo apt install -y fonts-powerline
    wget -qO- https://astral.sh/uv/install.sh | sh
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to $HOME/.local/bin

    # optional install nvm
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    nvm install --lts
    nvm use --lts

    # Fix some locale thing
    sudo apt install -y locales
    sudo echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    sudo echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    sudo echo "LANG=en_US.UTF-8" > /etc/locale.conf
    sudo locale-gen en_US.UTF-8

    # Install Oh My Zsh https://github.com/ohmyzsh/ohmyzsh#basic-installation
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

    # Install Powerlevel10k theme https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#oh-my-zsh
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

    # Install additional oh my zsh plugins
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```

1. Replace/Put [this](https://gist.github.com/rohit1998/172f2d891c9006c84a39dd89c390a813#file-p10k-zsh) file at location `~/.p10k.zsh`
1. For zshrc, replace your `~/.zshrc` with [this](https://gist.github.com/rohit1998/172f2d891c9006c84a39dd89c390a813#file-zshrc)

    OR RUN THESE

    ```bash
    cat <<'EOF' >> ~/.zshrc

    # Custom aliases
    alias j="just"
    jf() {just | grep "$1";}

    EOF

    ```

    ```bash
    cat <<'EOF' | cat - ~/.zshrc > temp && mv temp ~/.zshrc
    # Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
    # Initialization code that may require console input (password prompts, [y/n]
    # confirmations, etc.) must go above this block; everything else may go below.
    if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
      source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
    fi

    EOF
    ```

    ```bash
    cat <<'EOF' >> ~/.zshrc

    # To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
    [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

    EOF

    ```

    ```bash
    sed -i 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
    ```

    ```bash
    sed -i 's/^plugins=(.*)$/plugins=(git sudo history encode64 copypath zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc
    ```

    ```bash
    cat <<'EOF' >> ~/.zshrc

    # Check if DOTENV_FILE is set and the file exists
    if [[ -n "$DOTENV_FILE" && -f "$DOTENV_FILE" ]]; then
      # Export each non-comment, non-empty line as environment variable
      export $(grep -v '^#' "$DOTENV_FILE" | grep -v '^$' | xargs)
    fi

    EOF

    ```

    if nvm installed

    ```bash
    cat <<'EOF' >> ~/.zshrc

    # nvm
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

    EOF
    ```
