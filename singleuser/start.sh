#!/bin/bash

# Any environment setup can go here

# Start JupyterLab without a token and allow root
exec jupyter lab --no-browser --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.allow_origin='*' --NotebookApp.allow_root=True
