# Example OpenAgua engines

OpenAgua engines connect with [OpenAgua](www.openagua.org) to do something meaningful, like run a water system model. The [OpenAgua Engine](https://github.com/openagua/openagua-engine) Python package provides a suite of useful tools to help create such engines.

This repository includes several examples to demonstrate how to use OpenAgua Engine.

Documentation about the OpenAgua Engine package can be found along with its source code at https://github.com/openagua/openagua-engine.

# Getting started

1. Read the [getting started](https://github.com/openagua/openagua-engine#getting-started) section of the OpenAgua Engine documentation.
2. Get your keys in order. See the [keys documentation](https://github.com/openagua/openagua-engine#keys)
3. Install dependencies. You can either install from *requirements.txt* (`pip install -r requirements.txt`) or install packages manually. To install OpenAgua Engine: `pip install openagua_engine`. Note that while the package is called `openagua_engine`, within a script you `import openagua`.

# Descriptions of examples

This is a high level description of examples. The best way to understand the examples is 1) read the [OpenAgua Engine documentation](https://github.com/openagua/openagua-engine) and 2) look at the code itself.

**Operating system notes**

These examples were developed on Windows 10. They should work on Mac/Linux as well, but not necessarily. For example, it will be easier (necessary?) to run the WEAP example on Windows. Also note that these examples run a [Celery](docs.celeryproject.org) app. Celery does not officially support Windows, though it can be run on Windows. One way is to run the Celery app on Windows is with the `-P solo` CLI option.

## basic example

This is the "hello world" example. Start here to get your feet wet. As of writing, this does not use the OpenAgua API, but instead demonstrates basic interactivity: it can be started and stopped from the OpenAgua app, and updates one or more progress bar on the app.

## weap example

This under-development example demonstrates how to run a WEAP model from OpenAgua. Note that you need a valid WEAP license for this to work, since the WEAP API does not work without a valid license.
