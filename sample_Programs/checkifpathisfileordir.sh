#!/bin/bash
echo "Enter the path:"
read path
echo "Path value is $path"
[ -d "$path" ] && echo "It's a directory and exist"
[ -f "$path" ] && echo "It's a file and exist"