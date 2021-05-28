Please run the following command first to build docker image.
```bash
$ sh build.sh
```

Then you can use it image with the following command:
```bash
$ docker run -e PYTHONPATH=/usr/lib/python3.8/site-packages:/packages/python/lib/python3.8/site-packages \
  -v /my-packages-folder:/packages \
  -a STDIN -a STDOUT -a STDERR -i --rm \
  moderncloud/python-language-server:0.1 \
  jedi-language-server
```
