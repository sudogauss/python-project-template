# python-project-template

Write short project overview here...

## Build and use

To build project and use it:

```bash
    $ python3 -m build .                            # to build
    $ pip install [<project>.whl|<project>.tar.gz]  # install package
    $ <project>                                     # use installed command
```

***Note: You can export those commands to the pipeline***

## Tools

Running tests:

```bash
    $ pytest                    # runs all the tests with coverage
    $ pytest -m unit            # run only unit tests
    $ pytest -m core            # run only core tests
    $ pytest tests/<submodule>  # run only specific set of tests in the submodule
```

Tools and useful commands:

```bash
    $ black src/ tests/     # format code according to the configuration
    $ isort src/ tests/     # sort imports
    $ mypy src/             # execute type checking
    $ flake8 src/ tests/    # run linter
```

***Note: You can export those commands to the pipeline***

## Contributions

The following contribution rules apply:

- Use type hinting
- Document code with docstrings
- Don't hesitate to use inline comments
- Use tool section to sort imports and execute type checking
- Use full package imports
- Coverage should be kept up to at least 80%, only rare exception are authorized for pragma no coverage

Run the following command to install deve dependencies and start developing:

```bash
    $ pip install -e ".[dev]"
```