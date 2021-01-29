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

### Definition

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

The following diagram explains where are all the places where Load Balancers, can be placed to utilize full scalability and reliability.  

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbpresence.svg)

### Benefits of load balancing

A properly implemented load balancing system can have the following benefits:

1. Enhances User Experience, since continuous load distribution in turn provides *uninterrupted service*.
2. Service providers experience *less downtime* and *higher throughout*.
3. Predictive analytics to *determine bottlenecks* before they happen.
4. System admins experience *fewer failed or stressed components*.

## Dealing with Redundancy in Load Balancers

Load balancer can be a single point of failure; second load balancer can be connected to form a cluster.

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbredundacy.svg)



## Load Balancing Algorithms

***Health check***: Attempts to connect to backend servers to ensure that server is listening; on health check failure, server is automatically removed from pool, till health check is green again.

| Algorithm                  | Explanation                                                  |
| -------------------------- | ------------------------------------------------------------ |
| Least Connection Method    | Server with fewest active connections; large number of persistent client connections. |
| Least Response Time Method | Server with fewest active connections and lowest average response time. |
| Least Bandwidth Method     | Server serving least amount of traffic in Mbps.              |
| Round Robin Method         | Servers of equal specialization (processing power) and not many persistent connections; RR of server list. |
| Weighted Round Robin       | RR of weighted processing capacities server list.            |
| IP Hash                    | Hash IP                                                      |
| Consistent Hashing         | Click [here](#consistent-hashing).                           |

### Consistent Hashing

