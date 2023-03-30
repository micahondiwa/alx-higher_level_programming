#!/bin/bash
#Content length from HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
