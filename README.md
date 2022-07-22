# fast-api-tech-talk-1
Tech Talk about FastAPI Python Framework


## Steps to run this project

- Create and activate a virtual environment with at least Python 3.9

- Be sure that `scripts/init.sh` has execution permissions.

- Run the postgres container:

```sh
docker-compose up -d
```

- Make the initial setup with the dependencies:

```sh
make initial-setup
```

- Run the project (Make sure to load .env variables)
    -  You can use VS Code `Run and Debug` with the supplied launch.json file

- Enjoy your API at http://127.0.0.1:8000
- Remember you can use the docs http://127.0.0.1:8000/docs