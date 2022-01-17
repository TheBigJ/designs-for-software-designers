# What are microservices ?

Microservices is an architectural style that structures an application as a collection of services that are

- Highly maintainable and testable;
- Loosely coupled;
- Independently deployable;
- Organized around business capabilities, and;
- Owned by a small team.

The microservice architecture pattern language us a collection of patterns for applying the microservice architecture. It has two goals:

1. The pattern language enables you to decide whether microservices are a good fit for your application.
2. The pattern language enables you to use the microservice architecture successfully.

## Problems in migration from monolithic hell to microservices - Anti-Patterns

The following types of anti-patterns are prominient while migration of monolithic architecture to microservices:

1. [Microservices are a magic pixie dust](#Microservices-are-a-magic-pixie-dust)
2. Microservices as the goal
3. Scattershot adoption
4. Trying to fly before you can walk
5. Focussing on technology
6. More the merrier
7. Red flag law

> Unlike a regular pattern, which is a (problem, solution) pair, an anti-pattern consists of 3 elements:
> 1. *Problem* - the problem which is being tried to solve,
> 2. *Anti-pattern solution* - the solution that doesn't work well,
> 3. *Refactored solution* - a better solution to the problem.


### Microservices are a magic pixie dust

It is the phenomenon of believing that a sprinkle of microservices will solve all of your development problems, which unfortunately is not the case. *Microservices* is just an architecture style that has good deployability and testability, enabling high velocity, autonomous teams and devOps style development due to its loosely coupled architecture.

Example of such an anti-pattern, could be using microservice architecture to address an inadequate development and deployment process. 

It is not feasible in most cases because, many enterprises rely on manual testing done by a separate QA team. They often use manual deployment process, and sometimes code is messy and overly complicated leading to duplicate and diverging code bases. Microservices can't don't sh*t here.

🔰 To avoid this anti-pattern, it's important to understand 3 things.
1. Need to understand underlying root causes for software delivery issues-be it deployment, development or your organization, or maybe monolith has outgrown its architecture.
2. Need to understand the problems microservice architecture addresses.
3. Need to have automated testing as pre-requisite in-order to be successful with microservices.

### Microservice as a goal

The problem outlined here is making the adoption of microservices as the goal and measuring success in terms of the number of services written.

An example could be an executive might announce a microservices transformation initiative and expect every development team to `do microservices`. Development teams then scramble to `do microservices`. Perhaps, a team's annual or quarterly bonus is affected by how well they `do microservices`.

The issue here is that while making microservices the goal, it ignores other obstacles to rapid , frequent and reliable software delivery including:

- Inefficient processes and practices - waterfall process, manual testing, manual deployment
- Silo'd organization
- Poor software quality - the application is a big ball of mud, the code is anything but clean, etc.

> An organization suffering from these problems might not benefit from adopting microservices, forced adoption can most possibly making things worse.

🔰 A much better way of increaing velocity, frequency and reliability of software delivery is by using the following metrics:
- Increased lead time (*time from commit to deploy*) - eliminate wasteful work, automation, etc.
- Increased deployment frequency (*number of deploys per day per developer*) - automated testing and deployment, etc.
- Reducing failure rate (*how often deployments fail*) - automated testing, automated deployment, etc.
- Reducing recovery time (*time to recover from on outage*) - improved monitoring, automated recovery, etc.

### Scattershot adoption

Multiple application development teams attempt to adopt the microservices architecture without any coordination.

> A common reason from this anti-pattern is that a leader of the orgnization made the adoption of microservices everyone's goal.

The evident issue is the simultaneous attempts at coordination is inefficient; the reason is lack of skills or the time to build and management development.

🔰 A better approach is for the organization to define and execute a microservice migration roadmap, something like this:
1. Strategy should be defined and communicated by the leadership.
2. Key delivery metrics should be baselined.
3. An infrastructure team responsible for creating the deployment and runtime infrastructure should be established.
4. A candidate monolithic application should be selected.
5. (***Monolithic strangling***) Services should be extracted from the monolith.
    - Team responsible for developing, testing and deploying the service ought to be established.
    - Service ought to be extracted from monolith.
    - Hold a retrospective, implement lessons learned including approach and infrastructure.
    - Document and share lessons learned.
6. Expand to other application.

### Trying to fly before you can walk

It is attempting to adopt the microservice architecture without practicing basic software development techniques, such as clean code, good design, and automated testing.

The microservice architecture requires good design skills and test automation; a badly designed, microservice architecture that lacks automated tests is likely to be worse than a monolith; moreover, messy code will reduce your ability to deliver software rapidly and frequently.

🔰 When adopting microservices, an organization needs to embrace fundamentals, such as:

- Clean code - implement automated code quality enforcement as part of the deployment pipeline.
- Automatic testing - developers must be required to write automated tests as part of development.
- Design skills - such as OOD(object-oriented) or DDD (domain-driven). Services must have stable, well-designed APIs.

### Focusing on technology

It occurs when an organization focuses on technological aspects of microservices, most commonly deployment infrastructure. The only problem is focusing on the tech stack is an easy trap to fall into. 

The issue which this anti-pattern comes with is undifferentiated heavy lifting. Another issue is sometimes organization makes a big upfront investment in a vendor's product, which becomes a huge anchor at times.

🔰 A far better approach for the organization is to focus on the essence of microservices: service decomposition and definition.

### More the merrier

It is intentional creation of a very fine-grained microservice architecture.

The creation of excessive fine-grained microservice leads to, at some point of time, increases the risk that changes will require multiple services to change it to lockstep, which requires more coordination and planning and slows down development.

🔰 A better approach would be:

- to start service decomposition with one service per team since that's the bare minimum needed for the teams to be loosely coupled,
- additional service should only be defined when doing so clearly solves a problem,
- split services that become too large, and,
- split teams that become too large.

###  Red flag law

> **The Red Flag Traffic Law**, in 19<sup>th</sup> century US and UK, these laws required a pedestrian to walk in front of each automobile waving a red flag to warn the drivers, consequently resulting in the automobiles being forced to travel at the same speed as a pedestrian.

In organizations, 















































