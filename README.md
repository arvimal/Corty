## Daisho - Your own TO-DO manager

### Introduction

[Daisho](https://en.wikipedia.org/wiki/Daish%C5%8D), in Japanese, means `big-little`.

This application aims to be small and simple, while aiming to solve big problems.

Daisho is written for v3. Make sure you have Python v3 installed on the machine, and call `daisho.py` with `python3.6`.

```bash
# pythonv3.6 daisho.py
```

**NOTE:**

Python v2 will be deprecated by 2020. Make sure you check [https://pythonclock.org/](https://pythonclock.org/).

### How does Daisho work?

#### Front-end

Daisho has to be started from the terminal, where it will wait for the user's inputs and act accordingly.

A help section is shown to the user, prior the application allows the user to interact with it. 

Daisho uses the `prompt_toolkit` framework to list command completions, save command-history etc. Make sure you have the `python3-prompt_toolkit` installed.

Fedora ships the package, and can be installed with:

```bash
# dnf install python3-prompt_toolkit
```

#### Back-end

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


