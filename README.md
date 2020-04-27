[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Daisho - A CLI todo manager

### 1. Introduction

[Daisho](https://en.wikipedia.org/wiki/Daish%C5%8D), means `big-little`.

The development of Daisho has been mainly in Fedora Linux.

It aims to be simple, and easy to use. It is a CLI application, and supports command auto-completion, colour-coded outputs etc.

**NOTE:** Daisho is written in Python v3.

### 2. How does Daisho work?

Daisho runs on CLI as a simple [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) that waits for user input.

A help is printed each time `Daisho` starts. This lists the primary commands available for the user.

Since it supports command auto-completion, the secondary commands available under a primary, are listed. The `Tab` key cycles through these and `Enter` selects it. This ensures the user is never searching for the supported options, and reduce the

Daisho uses MongoDB on the localhost, to store the user data.

The REPL ensures the connection to the back-end MongoDB server at start-up, and constantly checks it through a heart-beat signal.

### 3. Installation

**Daisho** requires the following packages.

   1. MongoDB
   2. python3-colorama
   3. python3-prompt-toolkit
   4. python3-pymongo

Hence, it is imperative to have MongoDB running on localhost, listening on the default port `27017`.

Install MongoDB from their opensource release page. Other distributions may refer their mode of package installation.

```bash
# sudo dnf install mongodb-server -y

# sudo systemctl start mongod

# sudo systemctl status mongod
● mongod.service - High-performance, schema-free document-oriented database
   Loaded: loaded (/usr/lib/systemd/system/mongod.service; disabled; vendor preset: disabled)
   Active: active (running) since Tue 2018-01-09 15:09:15 IST; 14min ago
  Process: 19904 ExecStart=/usr/bin/mongod $OPTIONS run (code=exited, status=0/SUCCESS)
 Main PID: 19906 (mongod)
    Tasks: 22 (limit: 4915)
   Memory: 38.3M
      CPU: 1.986s
   CGroup: /system.slice/mongod.service
           └─19906 /usr/bin/mongod -f /etc/mongod.conf run
```


