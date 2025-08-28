# Learn Simple Regular Expressions

[![pr-checks](https://github.com/rohit1998/lsre/actions/workflows/pr-checks.yml/badge.svg)](https://github.com/rohit1998/lsre/actions/workflows/pr-checks.yml)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://rohit1998.github.io/lsre/)
[![PyPI version](https://img.shields.io/pypi/v/lsre.svg?color=blue)](https://pypi.org/project/lsre/)
[![Python versions](https://img.shields.io/pypi/pyversions/lsre.svg?color=blue)](https://pypi.org/project/lsre/)

A project to learn simple regular expressions. Also publish package to
pypi to learn automated publishing.

This project contains list of regex based functions.

>Warning: This is just for learning purposes and should not be used
>in production use case.

## Quick Start

### Installation

#### Using UV (Recommended)

```bash
uv add lsre
```

OR

```bash
uv pip install lsre
```

#### Using pip

```bash
pip install lsre
```

### Usage

```python
>>> from lsre import is_iso_date
>>> is_iso_date('2025-08-22')
True
>>> is_iso_date('1999-13-01')
False
```

## Architecture

Each function in module follows this template.

```mermaid
flowchart LR
    A["Input text"] --> B["lsre.is_url(text)"]
    B --> C{"Valid Input String?"}
    C -->|"Yes"| D["True if text is url else False"]
    C -->|"No"| E["Raise TypeError for wrong datatype"]
```

## More details

For full list of available functions, see the
[Code Reference](reference/lsre) section of the docs.
