# python-web-flask-memcached-counter

## Description
A POC python flask web counter
that uses memcached as a datastore.

Memcached is not a database that persists data
neither is it a websocket that updates multiple
clients.

Testing frameworks: *testify* and *selenium*

## Tech stack
- python
  - flask
  - testify
  - pymemcached
  - selenium
- memcached

## Docker stack
- python:latest
- bitnami/memcached:latest
- selenium:latest

## To run
`sudo ./install.sh -u`
Available at http://localhost

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
