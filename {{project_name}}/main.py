#!/usr/bin/env python3
"""Main script demonstrating the use of lib_a package."""

import logging

from lib_a import hello_world

logger = logging.getLogger(__name__)


def main():
    """Main function."""
    message = hello_world()
    logger.info(message)
    logger.info("Hello from completely-new!")


if __name__ == "__main__":
    main()
