# Control API

Iris Nodes can be controlled using HTTP API.

## Command

- Requests are sent to `http://iris-node:8080/command`.
- Body should be sent as `application/json`.

### Network Create

Create and configure a network.

- `name`: Name of the network to create.
- `mode`: Network behavior mode.
- `key`: Key to join this network.

```json
{
  "command": "network_create",
  "password": "MyApiPassword",
  "options": {
    "config": {
      "name": "MyNetwork",
      "mode": "master_slave",
      "key": "o23e9nfd54gpz"
    }
  }
}
```

### Network Join

Join an existing network.

- `ip`: IP of a network member node.
- `port`: Socket port of the network member node.
- `key`: Key to join the network.

```json
{
  "command": "network_join",
  "password": "MyApiPassword",
  "options": {
    "ip": "192.168.0.10",
    "port": "8081",
    "key": "o23e9nfd54gpz"
  }
}
```

### Network Leave

Leave current network.

```json
{
  "command": "network_leave",
  "password": "MyApiPassword"
}
```

### File Save

Send a file from the current node to the target nodes.

- `target`: Target nodes to save the file. ("all" or array of node ids)
- `directory`: Workspace directory.
- `name`: Name of file.

```json
{
  "command": "file_save",
  "password": "MyApiPassword",
  "options": {
    "target": "all",
    "directory": "image",
    "name": "cat_dog_classification.tar"
  }
}
```

### File Fetch

Send a file from the source node to the target nodes.

- `source`: Source node to fetch file. (node id)
- `target`: Target nodes to save the file. ("all" or array of node ids)
- `directory`: Workspace directory.
- `name`: Name of file.

```json
{
  "command": "file_fetch",
  "password": "MyApiPassword",
  "options": {
    "source": "549edb24-53f9-49d7-8243-a0189c2f1808",
    "target": ["52ef52e7-4a5c-4929-8e02-9109549d8e2f"],
    "directory": "public",
    "name": "catdog_model.pth"
  }
}
```

### Container Load

Load a Docker image on target nodes.

- `target`: Target nodes to load image. ("all" or array of node ids)
- `image`: Name of image file.

```json
{
  "command": "container_load",
  "password": "MyApiPassword",
  "options": {
    "target": "all",
    "image": "cat_dog_classification.tar"
  }
}
```

### Container Create

Create containers on target nodes based on a certain image.

- `target`: Target nodes to create container. ("all" or array of node ids)
- `image`: Docker image to use.
- `name`: Name of container.

```json
{
  "command": "container_create",
  "password": "MyApiPassword",
  "options": {
    "target": "all",
    "image": "cat_dog_classification:latest",
    "name": "cat_dog_classification"
  }
}
```

### Container Execute

Execute a command in a certain container on target nodes.

- `target`: Target nodes to execute command. ("all" or array of node ids)
- `name`: Name of container.
- `command`: Command to execute.

```json
{
  "command": "container_execute",
  "password": "MyApiPassword",
  "options": {
    "target": "all",
    "name": "cat_dog_classification",
    "command": "python train.py"
  }
}
```

### Container Remove

Remove a container on target nodes.

- `target`: Target nodes to remove container. ("all" or array of node ids)
- `name`: Name of container.

```json
{
  "command": "container_remove",
  "password": "MyApiPassword",
  "options": {
    "target": "all",
    "name": "cat_dog_classification"
  }
}
```

## File

- Requests are sent to `http://iris-node:8080/file`.
- Body should be sent as `form-data`.

### Upload

Upload a file to a node through an HTTP request.

- `directory`: Workspace directory.
- `image`: Name of image file.
- `file`: File to upload from current device.

```
command: upload
directory: image
name: cat_dog_classification.tar
file: /home/user/cat_dog_classification.tar
```

## View

- Requests are sent to `http://iris-node:8080/view`.
- Body should be sent as `application/json`.

### Map

View network map.

```json
{
  "command": "map",
  "password": "MyApiPassword"
}
```

### File

View Workspace files on a node.

```json
{
  "command": "file",
  "password": "MyApiPassword"
}
```
