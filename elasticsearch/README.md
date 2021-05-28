# Elasticsearch

## tshark integration

* Ubuntu 20.04, tshark 3.2.3

```
$ sudo apt install -y tshark jq
$ python3 -m venv .venv
$ . .venv/bin/activate
(.venv)$ pip install -r test-requirements.txt
(.venv)$ pytest -s
```
