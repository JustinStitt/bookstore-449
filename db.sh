#!/usr/bin/sh

curl -X POST "http://localhost:8000/add_book" -H "accept: application/json" -H\
"Content-Type: application/json" -d "{ \"author\": \"foobar\", \"description\":
\"a cool book\", \"price\": 1.99, \"stock\": 2, \"title\": \"qazqux\"}"
