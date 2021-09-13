#!/bin/bash
set -e

# Run tests
pytest --cov=app --cov-report=term-missing tests