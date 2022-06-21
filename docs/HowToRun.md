# How to run

An Iris Node can be run by only giving a few arguments.

The actual features can be used through the Control API.

## Arguments

- `Name`: A name to identify a node.
- `IP`: A IP address so that other nodes can join the network through this node.
- `API Port`: A port used by the Control API.
- `Socket Port`: A port used for inter node communications.
- `Password`: A password for Control API authentication.

## With Docker

```shell
docker-compose build
docker-compose up -d
```

## Directly

```shell
npm run build
npm start -- --name MyNode --ip 192.168.0.10 --api 8080 --socket 8081 --password "MyApiPassword"
```
