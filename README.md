<img src='https://bettercodehub.com/edge/badge/arvimal/Corty?branch=main'> [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Corty

### 1. Introduction

The development of Corty has been mainly in Fedora Linux.

It aims to be simple, and easy to use. It is a CLI application, and supports command auto-completion, colour-coded outputs etc.

### 2. How does Corty work?

Corty has a client-server architecture that communicates through a GraphQL API interface. 

The user interacts with the server through the Corty CLI, which is a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) interface that waits for user input.

A help is printed each time `Corty` starts. This helps the user with a quick overview of the primary commands available.  

Command auto-completion is supported, and a TAB press cycles through each primary. The `Enter` key selects the command. Once the primary command is selected, a second TAB lists the secondary level of commands specific to the selected primary. 

The server uses MongoDB as its database backend. While starting up, the client ensures that it has a proper connection to the server, as well as the MongoDB database. The connection is regularly checked through a heart-beat signal. 

### 3. Installation

**Corty** requires the following packages.

   1. MongoDB
   2. python3-colorama
   3. python3-prompt-toolkit
   4. python3-pymongo
   5. python3-graphql-server
   6. python3-graphene
   7. graphql

MongoDB has to be running on localhost (for now), listening on the default port `27017`. Splitting the database off, is something that should happen later.

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


