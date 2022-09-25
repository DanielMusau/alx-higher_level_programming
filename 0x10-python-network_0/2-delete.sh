#!/bin/bash
# Script that send a DELETE request to the URL passed
curl -s "$1" -X DELETE
