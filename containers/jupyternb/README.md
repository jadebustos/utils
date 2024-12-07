# README

$ JUPYTER_CONFIG_DIR=$PWD jupyter server password
Enter password:
Verify password:
[JupyterPasswordApp] Wrote hashed password to ./jupyter_server_config.json
$ cat jupyter_server_config.json
{
  "IdentityProvider": {
    "hashed_password": "argon2:$argon2id$v=19$m=10240,t=10,p=8$4wUfa8Ikw4hqftKpmYbgLA$QC/iREH2JhL9MV95Uqr5X6CVipzYdFfgS1TGtuy1Hlc"
  }
}
You can add this file via a secret volume to your container, e.g. mounting it in /etc/jupyter/jupyter_server_config.json
