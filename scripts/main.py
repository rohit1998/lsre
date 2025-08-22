"""Main module."""

import logging
import sys
from pathlib import Path
from typing import Any

import hydra
from dotenv import load_dotenv
from loguru import logger
from omegaconf import DictConfig, OmegaConf

from lsre.module import MyModule

this_dir = Path(__file__).resolve().parent

load_dotenv()


def setup_logging(cfg: DictConfig) -> None:
    """Setup logging configuration."""
    logging.getLogger().setLevel(logging.WARNING)
    logger.remove()

    cfg_dict: Any = OmegaConf.to_container(cfg, resolve=True)
    for logger_config in cfg_dict:
        if logger_config['sink'] == 'stdout':
            logger_config['sink'] = sys.stdout
        elif logger_config['sink'] == 'stderr':
            logger_config['sink'] = sys.stderr

        logger.add(**logger_config)


@hydra.main(
    version_base=None,
    config_path=str(this_dir / '../configs'),
    config_name='config',
)
@logger.catch
def main(cfg: DictConfig) -> None:
    """Main function."""
    setup_logging(cfg.logger)
    logger.debug('logger setup complete')

    name = cfg.name
    my_module = MyModule(name)

    greeting = my_module.run()
    logger.info(greeting)

    secret = my_module.get_secret()
    logger.info(f'My secret is {secret}')


if __name__ == '__main__':
    main()
