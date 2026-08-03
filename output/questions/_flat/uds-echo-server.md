# UDS Echo Server

---

| Field | Value |
|---|---|
| **Slug** | `uds-echo-server` |
| **Domain** | distributed-systems |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/uds-echo-server |

---

## Preview

Write a UNIX Domain Socket server which can echo back data sent by a client.

## Problem Statement

This challenge tests your understanding of Sockets and Multi-Threaded programming. 

Your task is to write a UNIX Domain Socket([UDS](http://en.wikipedia.org/wiki/Unix_domain_socket)) server which can accept connection from 'N' clients. Each client will send text data over the socket. Read the data and send it back to the client. The server should be Multi-Threaded and should service all clients in parallel.

To support Multi-Threading you can use the POSIX thread library (C,C++) or the default threading library for other languages. 


**Communication Protocol**

Read data from client and send the response back.

String "END" marks end of communication from a client. Send response "END" and disconnect the client.  


Example request 1:


    Client 1:
    Hello World
    END

Example response 1:


    Client 1:
    Hello World

Example request 2:


    Client 2:
    This is line 1
    This is line 2
    END

Example response 2:


    Client 2:
    This is line 1
    This is line 2

## Sample Tests

### Test 1

```
Client 1:
Hello World
END
```

### Test 2

```
Client 1:
Hello World
```

### Test 3

```
Client 2:
This is line 1
This is line 2
END
```

### Test 4

```
Client 2:
This is line 1
This is line 2
```
