"""Main module."""

import logging
import sys
from pathlib import Path
from typing import Any

import hydra
from dotenv import load_dotenv
from loguru import logger
from omegaconf import DictConfig, OmegaConf

import lsre

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

    text_list = cfg.text_list
    for text in text_list:
        logger.debug(f'Running checks for {text}')

        results = {
            'alphanumeric': lsre.is_alphanumeric(text),
            'email': lsre.is_email(text),
            'url': lsre.is_url(text),
            'ipv4': lsre.is_ipv4(text),
            'ipv6': lsre.is_ipv6(text),
            'phone_number': lsre.is_phone_number(text),
            'credit_card': lsre.is_credit_card(text),
            'iso_date': lsre.is_iso_date(text),
            'time': lsre.is_time(text),
            'hex_color': lsre.is_hex_color(text),
            'uuid': lsre.is_uuid(text),
            'slug': lsre.is_slug(text),
            'strong_password': lsre.is_strong_password(text),
        }

        for check_name, passed in results.items():
            logger.info(
                f'{text} is ' + ('' if passed else 'not ') + f'{check_name}'
            )

    logger.debug('Finished all tests')


if __name__ == '__main__':
    main()
