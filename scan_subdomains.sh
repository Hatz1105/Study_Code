#!/bin/bash
if [ -z "$1"]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

subfinder -d $1 -silent | httpx -title -status