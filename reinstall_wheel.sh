#!/bin/bash

pip-autoremove nwunity
pip uninstall nwunity -y
pip install ./dist/*.whl --force-reinstall