# README

## Running the container

```console
$ podman run --rm -d --name notebook -v <YOUR LOCAL DIRECTORY>:/home/notebook/data:Z -p 8888:8888 quay.io/rhte_2019/notebook:v1
```

Your notebooks will be readed/saved from/to **\<YOUR LOCAL DIRECTORY\>**.

## Custom configuration 

You can create your custom configuration file **jupyter_server_config.json**:

```json
{
  "IdentityProvider": {
    "hashed_password": "argon2:..."
  }
}
```

Where the hashed password can be created:

```console
$ JUPYTER_CONFIG_DIR=$PWD jupyter server password
Enter password:
Verify password:
[JupyterPasswordApp] Wrote hashed password to ./jupyter_server_config.json
$ cat jupyter_server_config.json
{
  "IdentityProvider": {
    "hashed_password": "argon2:..."
  }
}
```

You can add this file via a secret volume to your container, mounting it in _/home/notebook/.jupyter/jupyter_server_config.json_
