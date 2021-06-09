You can use our docker image with the following command: 
```bash
$ docker run -e PYTHONPATH=/usr/lib/python3.8/site-packages:/packages/python/lib/python3.8/site-packages \
  -v /my-packages-folder:/packages \
  -a STDIN -a STDOUT -a STDERR -i --rm \
  moderncloud/python-language-server:0.2 \
  python3 /startserver.py
```
