#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays body of the response.
curl -X POST "$1" -H "Content-Type: application/json" --data @"$2"
