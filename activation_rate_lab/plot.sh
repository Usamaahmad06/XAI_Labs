#!/bin/bash
set -e

mkdir -p plots
uv run python plot.py
