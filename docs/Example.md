# Example

This example is based on a simple [Dogs vs. Cats Classification](https://www.kaggle.com/c/dogs-vs-cats) using PyTorch.

## Code

The Dockerfile and Python codes can be found in [docs/example_cat_dog_classification](example_cat_dog_classification).

The Entrypoint of the Dockerfile does not do anything because the actual training code will be executed by the Control API.

## Prerequisites

Create a Docker image that contains the code and dependencies.
- `/workspace/image/cat_dog_classification.tar`

```shell
docker build -t cat_dog_classification .
docker save -o cat_dog_classification.tar cat_dog_classification:latest
```

The train data should be loaded into the Workspace Private directory.
- `/workspace/private/train`
- `/workspace/private/test`

## Work Flow

Assume `A` is the master node which the user interacts with through the Control API and `B` is the worker node where the data is loaded.

1. `A` Create network

- `command`: `network_create`
- `name`: MyNetwork
- `mode`: master_slave
- `key`: o23e9nfd54gpz

2. `B` Join Network

- `command`: `network_join`
- `ip`: 192.168.0.10 (`A`)
- `port`: 8081
- `key`: o23e9nfd54gpz

3. `A` Upload image file

- `command`: `upload`
- `directory`: image
- `name`: cat_dog_classification.tar
- `file`: /home/user/cat_dog_classification.tar

4. `A` Save image file

- `command`: `file_save`
- `target`: all
- `directory`: image
- `name`: cat_dog_classification.tar

5. `A`Load image file

- `command`: `container_load`
- `target`: all
- `image`: cat_dog_classification.tar

6. `A` Create containers

- `command`: `container_create`
- `target`: all
- `image`: cat_dog_classification:latest
- `name`: cat_dog_classification

7. `A` Execute in containers

- `command`: `container_execute`
- `target`: all
- `name`: cat_dog_classification
- `command`: python train.py

8. `A` Fetch model file

- `command`: `file_fetch`
- `source`: 549edb24-53f9-49d7-8243-a0189c2f1808 (`B`)
- `target`: [ 52ef52e7-4a5c-4929-8e02-9109549d8e2f ] (`A`)
- `directory`: public
- `name`: catdog_model.pth

## Results

The container will train the model and save it to a `.pth` file in the Workspace Public directory.
- `/workspace/public/catdog_model.pth`

This file can be fetched to other nodes to be viewed or used.
