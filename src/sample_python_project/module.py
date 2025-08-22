"""Sample module."""

import os

from loguru import logger


class MyModule:
    """My module."""

    def __init__(self, name: str) -> None:
        """Initialize the module.

        Args:
            name: The name of the person to greet.
        """
        self.name = name

    def run(self) -> str:
        """Run the module.

        Returns:
            The greeting.
        """
        logger.debug('Running module')
        greeting = f'Hello {self.name}'
        logger.debug('Ran module')
        return greeting

    def get_secret(self) -> str:
        """Get the secret.

        Returns:
            The secret.
        """
        logger.debug('Getting secret')
        secret = os.getenv('MY_SECRET')
        if secret is None:
            logger.error('Secret not found')
            msg = 'Secret not found'
            raise ValueError(msg)
        logger.debug('Got secret')
        return secret
