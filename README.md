# countfiles

Like `tree` on Linux, but for number of files.

The basics:

```shell
klaatu@gort-ubuntu:~/kod/countfiles$ countfiles -h
usage: countfiles [-h] [--max-depth MAX_DEPTH] [--min-filecount MIN_FILECOUNT] [--no-color] [--version] path

Show accumulated number of files per directory.

positional arguments:
  path

optional arguments:
  -h, --help            show this help message and exit
  --max-depth MAX_DEPTH, -md MAX_DEPTH
                        Iterate all the way, but only show directories down to this depth.
  --min-filecount MIN_FILECOUNT, -mfc MIN_FILECOUNT
                        Iterate all the way, but only show directories with this number of files or more.
  --no-color
  --version, -V         show program's version number and exit
```

Example output:

```shell
klaatu@gort-ubuntu:~/kod/countfiles$ countfiles .
[      1331]  .
├── [         2]  build
│   ├── [         2]  lib
│   │   └── [         2]  countfiles
│   └── [         0]  bdist.linux-x86_64
├── [         2]  countfiles
├── [         6]  countfiles.egg-info
├── [        33]  .git
│   ├── [         9]  objects
│   │   ├── [         1]  67
│   │   ├── [         1]  f2
│   │   ├── [         1]  ec
│   │   ├── [         1]  09
│   │   ├── [         1]  fe
│   │   ├── [         1]  ee
│   │   ├── [         0]  pack
│   │   ├── [         1]  17
│   │   ├── [         1]  5a
│   │   ├── [         0]  info
│   │   └── [         1]  3d
│   ├── [         0]  branches
│   ├── [        12]  hooks
│   ├── [         3]  logs
│   │   └── [         2]  refs
│   │       ├── [         1]  heads
│   │       └── [         1]  remotes
│   │           └── [         1]  origin
│   ├── [         2]  refs
│   │   ├── [         1]  heads
│   │   ├── [         0]  tags
│   │   └── [         1]  remotes
│   │       └── [         1]  origin
│   └── [         1]  info
├── [         1]  __pycache__
└── [      1281]  .venv
    ├── [      1267]  lib
    │   └── [      1267]  python3.9
    │       └── [      1267]  site-packages
    │           ├── [       249]  setuptools
    │           │   ├── [        28]  _vendor
    │           │   │   ├── [        22]  packaging
    │           │   │   │   └── [        11]  __pycache__
    │           │   │   └── [         3]  __pycache__
    │           │   ├── [         2]  extern
    │           │   │   └── [         1]  __pycache__
    │           │   ├── [       108]  _distutils
    │           │   │   ├── [        30]  __pycache__
    │           │   │   └── [        48]  command
    │           │   │       └── [        24]  __pycache__
    │           │   ├── [        26]  __pycache__
    │           │   └── [        51]  command
    │           │       └── [        25]  __pycache__
    │           ├── [       808]  pip
    │           │   ├── [       515]  _vendor
    │           │   │   ├── [        43]  distlib
    │           │   │   │   ├── [        13]  __pycache__
    │           │   │   │   └── [        11]  _backport
    │           │   │   │       └── [         5]  __pycache__
    │           │   │   ├── [        86]  chardet
    │           │   │   │   ├── [         4]  cli
    │           │   │   │   │   └── [         2]  __pycache__
    │           │   │   │   ├── [        39]  __pycache__
    │           │   │   │   └── [         4]  metadata
    │           │   │   │       └── [         2]  __pycache__
    │           │   │   ├── [        12]  colorama
    │           │   │   │   └── [         6]  __pycache__
    │           │   │   ├── [        66]  html5lib
    │           │   │   │   ├── [        10]  treebuilders
    │           │   │   │   │   └── [         5]  __pycache__
    │           │   │   │   ├── [        16]  filters
    │           │   │   │   │   └── [         8]  __pycache__
    │           │   │   │   ├── [         6]  treeadapters
    │           │   │   │   │   └── [         3]  __pycache__
    │           │   │   │   ├── [         8]  __pycache__
    │           │   │   │   ├── [        12]  treewalkers
    │           │   │   │   │   └── [         6]  __pycache__
    │           │   │   │   └── [         6]  _trie
    │           │   │   │       └── [         3]  __pycache__
    │           │   │   ├── [        22]  pep517
    │           │   │   │   ├── [         4]  in_process
    │           │   │   │   │   └── [         2]  __pycache__
    │           │   │   │   └── [         9]  __pycache__
    │           │   │   ├── [        36]  requests
    │           │   │   │   └── [        18]  __pycache__
    │           │   │   ├── [        10]  progress
    │           │   │   │   └── [         5]  __pycache__
    │           │   │   ├── [        14]  resolvelib
    │           │   │   │   ├── [         5]  __pycache__
    │           │   │   │   └── [         4]  compat
    │           │   │   │       └── [         2]  __pycache__
    │           │   │   ├── [        10]  webencodings
    │           │   │   │   └── [         5]  __pycache__
    │           │   │   ├── [        22]  packaging
    │           │   │   │   └── [        11]  __pycache__
    │           │   │   ├── [        22]  tenacity
    │           │   │   │   └── [        11]  __pycache__
    │           │   │   ├── [        26]  cachecontrol
    │           │   │   │   ├── [        10]  __pycache__
    │           │   │   │   └── [         6]  caches
    │           │   │   │       └── [         3]  __pycache__
    │           │   │   ├── [         4]  __pycache__
    │           │   │   ├── [         6]  tomli
    │           │   │   │   └── [         3]  __pycache__
    │           │   │   ├── [        16]  idna
    │           │   │   │   └── [         8]  __pycache__
    │           │   │   ├── [         4]  pkg_resources
    │           │   │   │   └── [         2]  __pycache__
    │           │   │   ├── [        10]  msgpack
    │           │   │   │   └── [         5]  __pycache__
    │           │   │   ├── [        16]  platformdirs
    │           │   │   │   └── [         8]  __pycache__
    │           │   │   ├── [         7]  certifi
    │           │   │   │   └── [         3]  __pycache__
    │           │   │   └── [        78]  urllib3
    │           │   │       ├── [        20]  contrib
    │           │   │       │   ├── [         6]  _securetransport
    │           │   │       │   │   └── [         3]  __pycache__
    │           │   │       │   └── [         7]  __pycache__
    │           │   │       ├── [        24]  util
    │           │   │       │   └── [        12]  __pycache__
    │           │   │       ├── [        12]  packages
    │           │   │       │   ├── [         4]  ssl_match_hostname
    │           │   │       │   │   └── [         2]  __pycache__
    │           │   │       │   ├── [         4]  backports
    │           │   │       │   │   └── [         2]  __pycache__
    │           │   │       │   └── [         2]  __pycache__
    │           │   │       └── [        11]  __pycache__
    │           │   ├── [       288]  _internal
    │           │   │   ├── [        24]  cli
    │           │   │   │   └── [        12]  __pycache__
    │           │   │   ├── [         8]  locations
    │           │   │   │   └── [         4]  __pycache__
    │           │   │   ├── [        30]  operations
    │           │   │   │   ├── [        14]  build
    │           │   │   │   │   └── [         7]  __pycache__
    │           │   │   │   ├── [         4]  __pycache__
    │           │   │   │   └── [         8]  install
    │           │   │   │       └── [         4]  __pycache__
    │           │   │   ├── [        10]  distributions
    │           │   │   │   └── [         5]  __pycache__
    │           │   │   ├── [        34]  commands
    │           │   │   │   └── [        17]  __pycache__
    │           │   │   ├── [        26]  resolution
    │           │   │   │   ├── [        18]  resolvelib
    │           │   │   │   │   └── [         9]  __pycache__
    │           │   │   │   ├── [         4]  legacy
    │           │   │   │   │   └── [         2]  __pycache__
    │           │   │   │   └── [         2]  __pycache__
    │           │   │   ├── [         9]  __pycache__
    │           │   │   ├── [        16]  network
    │           │   │   │   └── [         8]  __pycache__
    │           │   │   ├── [        22]  models
    │           │   │   │   └── [        11]  __pycache__
    │           │   │   ├── [         8]  index
    │           │   │   │   └── [         4]  __pycache__
    │           │   │   ├── [        60]  utils
    │           │   │   │   └── [        30]  __pycache__
    │           │   │   ├── [        12]  vcs
    │           │   │   │   └── [         6]  __pycache__
    │           │   │   ├── [        14]  req
    │           │   │   │   └── [         7]  __pycache__
    │           │   │   └── [         6]  metadata
    │           │   │       └── [         3]  __pycache__
    │           │   └── [         2]  __pycache__
    │           ├── [         8]  pycodestyle-2.8.0.dist-info
    │           ├── [        12]  colorama
    │           │   └── [         6]  __pycache__
    │           ├── [         8]  pip-21.3.1.dist-info
    │           ├── [         8]  mccabe-0.6.1.dist-info
    │           ├── [         8]  flake8-4.0.1.dist-info
    │           ├── [         7]  pyflakes-2.4.0.dist-info
    │           ├── [        46]  pyflakes
    │           │   ├── [         6]  __pycache__
    │           │   ├── [        30]  test
    │           │   │   └── [        15]  __pycache__
    │           │   └── [         4]  scripts
    │           │       └── [         2]  __pycache__
    │           ├── [         4]  _distutils_hack
    │           │   └── [         2]  __pycache__
    │           ├── [         9]  setuptools-52.0.0.dist-info
    │           ├── [         2]  __pycache__
    │           ├── [        34]  pkg_resources
    │           │   ├── [        28]  _vendor
    │           │   │   ├── [        22]  packaging
    │           │   │   │   └── [        11]  __pycache__
    │           │   │   └── [         3]  __pycache__
    │           │   ├── [         2]  extern
    │           │   │   └── [         1]  __pycache__
    │           │   ├── [         1]  __pycache__
    │           │   └── [         2]  tests
    │           │       └── [         2]  data
    │           │           └── [         2]  my-test-package-source
    │           │               └── [         1]  __pycache__
    │           ├── [        54]  flake8
    │           │   ├── [         4]  api
    │           │   │   └── [         2]  __pycache__
    │           │   ├── [        10]  main
    │           │   │   └── [         5]  __pycache__
    │           │   ├── [         6]  formatting
    │           │   │   └── [         3]  __pycache__
    │           │   ├── [        10]  __pycache__
    │           │   ├── [         8]  options
    │           │   │   └── [         4]  __pycache__
    │           │   └── [         6]  plugins
    │           │       └── [         3]  __pycache__
    │           └── [         7]  colorama-0.4.4.dist-info
    ├── [        13]  bin
    └── [         0]  include
```
