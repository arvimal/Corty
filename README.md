[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Daisho - A CLI todo manager

### 1. Introduction

[Daisho](https://en.wikipedia.org/wiki/Daish%C5%8D), in Japanese, means `big-little`.

This application aims to be small and simple, while aiming to solve big problems [which can always remain debatable :)].

**NOTE:** Daisho is written in Python v3.

### 2. How does Daisho work?

**Daisho** requires the following packages to function properly.

        1. MongoDB
        2. Colorama
        3. python3-prompt_toolkit

The steps to install them discussed are in the respective sections.

#### 2.1. Front-end

Daisho has to be started from the terminal, where it will wait for the user's inputs and act accordingly.

A help section is shown to the user, prior the application allows the user to interact with it.

Daisho uses the awesome `prompt_toolkit` framework to list command completions, save command-history etc. Make sure you have the `python3-prompt_toolkit` installed.

Fedora ships the package, and can be installed with:

```bash
# dnf install python3-prompt_toolkit
```

Daisho uses the `colorama` module to colorize the output.

#### 2.2. Back-end

Daisho uses a MongoDB database running on localhost to store user-data.

Hence, it is imperative to have MongoDB running on localhost, listening on the default port of `27017`.

Since `Daisho` is written and tested on a `Fedora 27` machine, the following steps to install and configure MongoDB cater to Fedora.

Other distributions may refer their mode of package installation.

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


