## Table of Contents

- [Load Balancing](#load-balancing)
  * [Definition and Benefits](#definition-and-benefits)
  * [Dealing with Redundancy in Load Balancers](#dealing-with-redundancy-in-load-balancers)
  * [Load Balancing Algorithms](#load-balancing-algorithms)
    + [Least Connection Method](#least-connection-method)
    + [Least Response Time Method](#least-response-time-method)
    + [Least Bandwidth Method](#least-bandwidth-method)
    + [Round Robin Method](#round-robin-method)
    + [Weighted Round Robin](#weighted-round-robin)
    + [IP Hash](#ip-hash)
    + [Consistent Hashing](#consistent-hashing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Load Balancing

### Definition and benefits

The process of balancing load evenly on *N* servers is **Load Balancing**.

A properly implemented **load balancer** helps in the following ways:

1. It helps spread traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases.
2. Keeps tract of statuses of all the resources while distributing requests.
3. Avoids re-routing requests to a server which has the following issues:
   - elevated rate of errors,
   - non-responsiveness, and;
   - request overload.
4. Prevents single point of failure and increases, availability and responsiveness.

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbrole.svg)

![]()

## Dealing with Redundancy in Load Balancers

## Load Balancing Algorithms

### Least Connection Method

### Least Response Time Method

### Least Bandwidth Method

### Round Robin Method

### Weighted Round Robin

### IP Hash

### Consistent Hashing
