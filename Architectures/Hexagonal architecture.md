# Blog 1: Hexagonal architecture in Golang

**Core**: In this architecture, everything is surrounding the core of the application. It is a tech-agnostic component that contains all the business logic. It is a *box* capable of resolving all the business logic independently of the infra in which the application is mounted (enabling us to test the core in isolation and gives us the ability to easily change infra components).

**Actors**: They are real world things that want to interact with the core (e.g., humans, dbs, other apps). They can be of two types depending on who triggers the interaction:

1. ***Drivers (or primary) actors***, are those who trigger the communication with the core, to invoke a specific service on the core. E.g., human or CLI
2. ***Driven (or secondary) actors***, are those who are expecting the core to be the one who trigger the communication, i.e., core needs something that the actor provides, so it sends a request to the actor and invoke a specific action on it. E.g., if the core needs to save data into a MySQL database, then the core trigger the communication to execute an INSERT query on the MySQL client.

![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/hexagonal.svg)



> Note: The actors and the core *speak* different languages. E.g., an external application sends a request over http to perform a core service call (which does not understand what http means); another example is when the core (tech-agnostic) wants to save data into a `mysql` database (which speaks SQL). 

What helps us to make such translations are *Ports & Adapters*.

**Ports**: These are interfaces that define how the communication between an actor and the core has to be done, which again can differ based on the actor:

- ***Ports for driver actors***, define the set of actions that the core provides and expose to the outside. Each action generally correspond with a specific case of use.
- ***Ports for driven actors***, define the set of actions that the actor has to implement.

**PORTS BELONG TO THE CORE**, as the core is the one who define which interactions are needed to achieve the business logic goals.



**Adapters**: These are responsible for the transformation between a request from the actor to the core, and vice versa, which again can differ based on the port type:

- ***An adapter for a driver port***, transforms a specific technology request into a call on a core service.
- ***An adapter for a driven port***, transforms a tech-agnostic request from the core into a specific tech request on the actor

<span style="color:orange">To connect the adapters to the corresponding ports using **Dependency Injection**</span>.