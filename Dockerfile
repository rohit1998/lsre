FROM ubuntu:24.04 AS base

# update the image
RUN apt update

# install wget
RUN apt install -y wget

# set uv project mode
ENV UV_LINK_MODE=copy

####################PROD####################

FROM base AS prod

# prod user, inbuilt ubuntu user
USER ubuntu

# Install uv using the official installer
RUN wget -qO- https://astral.sh/uv/install.sh | sh
ENV PATH="/home/ubuntu/.local/bin/:$PATH"

# set working directory
WORKDIR /home/ubuntu/app

# copy code to image
COPY --chown=ubuntu:ubuntu . .

# install non dev dependencies
RUN uv sync --no-dev

# run code
CMD ["uv", "run", "--no-sync", "scripts/main.py"]

####################DEV####################

FROM base AS dev

# remove the default ubuntu user
RUN touch /var/mail/ubuntu && chown ubuntu /var/mail/ubuntu && userdel -r ubuntu

# uid and gid for appuser. Same as host user
ARG APP_UID
ARG APP_GID

# Install useful packages
RUN apt install -y sudo
RUN apt install -y zsh
RUN apt install -y vim
RUN apt install -y git
RUN apt install -y curl
RUN apt install -y unzip
RUN apt install -y pre-commit
RUN apt install -y fonts-powerline

# Install GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
      | sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
      https://cli.github.com/packages stable main" \
      | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt install -y gh

# Fix some locale thing
RUN apt install -y locales
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8

# add and enable dev user
RUN set -eux; \
    if getent group "$APP_GID" >/dev/null; then \
        echo "Using existing group with GID $APP_GID"; \
    else \
        groupadd --gid "$APP_GID" appuser; \
    fi; \
    useradd --create-home --uid "$APP_UID" --gid "$APP_GID" --shell /bin/zsh appuser
RUN usermod -aG sudo appuser
RUN echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER appuser

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install Powerlevel10k theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Install additional oh my zsh plugins
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# install justfile
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /home/appuser/.local/bin

# Copy custom shell configuration files
COPY --chown=appuser:appuser ./.devcontainer/.zshrc /home/appuser/.zshrc
COPY --chown=appuser:appuser ./.devcontainer/.p10k.zsh /home/appuser/.p10k.zsh

# set working directory
WORKDIR /home/appuser/app

# Install uv using the official installer
RUN wget -qO- https://astral.sh/uv/install.sh | sh
ENV PATH="/home/appuser/.local/bin/:$PATH"

# install all dependencies except code (project install in post-create.sh after copying code)
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --no-install-project

###########################################
