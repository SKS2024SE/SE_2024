#!/bin/bash
grep -l -e 'sample' file_* | xargs grep -c -e 'CSC510' | grep -E ':([3-9]|([1-9][0-9]))$' | xargs -I X sh -c 'Y=$(ls -l $(echo X | cut -d ':' -f 1)) && echo -n "$(echo X | cut -d ':' -f 2) " && echo "$Y"' | sort -k1nr -k6nr | cut -d ' ' -f 10 | sed 's/file_/filtered_/'