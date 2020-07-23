# Inventory tracker

## Overview
This server is to track and update inventory. 

* [GET] /inventory
* [GET] /inventory/part_number
* [POST] /inventory/part_number
* [PUT] /inventory/part_number
* [GET] /inventory/lot_number
* [POST] /inventory/lot_number
* [PUT] /inventory/lot_number


## Requirements
Python 3.5.2+

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t app-inventory .

# starting up a container
docker run -p 8081:8080 app-inventory
```

## Starting database
```
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=adminpwd -p 3306:3306 -v /c/Users/ENGINEERING-FLN1/Documents/workspace/test-db:/var/lib/mysql mysql:5.7.30
```
## Regenerating server

Before regenerating the microservice, make sure you include the file that you **DON'T** want to delete in `.swagger-codegen-ignore`

To regenerate the microservice, you can run the following code:
```
java -jar ./swagger-codegen-cli.jar generate -Dmodels -Dapis -i ./app-inventory/api/v1.0.0.yaml -l python-flask -c ./app-inventory/api/config.json -o ./app-inventory
```