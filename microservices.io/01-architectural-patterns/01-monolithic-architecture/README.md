# Pattern: Monolithic Architecture

## Context

- You are developing a server-side enterprise application. 
  - It support a variety of different clients including desktop browsers, mobile browsers and native mobile applications. 
  - The application might expose an API for 3<sup>rd</sup> parties to consume. 
  - It might also integrate with other applications via either web services or a message broker. 
  - The application handles requests by executing business logic; access a database; exchanging messages with other systems; and returning a HTML/JSON/XML response. 
  - There are logical components corresponding to different functional areas of the application.

## Problem

What's the application's deployment architecture ?

## Forces

- Team of developers working on the application.
- New team members must quickly become productive.
- The application must by easy to understand and modify.
- You want to practice CD of the application.
- You must run multiple instances of the application on multiple machines in order to satisfy scalability and availability requirements.
- You want to take advantage of emerging technologies.

## Solution

Applying monolithic architecture here,

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Simple to develop (Code base is small, so development is fast) | The larger the monolithic code base becomes, the more it intimidates developers, especially ones who are new to the team, increasing the difficulty in modification and understandability, which further slows the development down. |
| Simple to deploy (Deploy just one binary file on the appropriate runtime) | The larger the code base is, the slower the IDE will be and the less productive developers are. |
| Simple to scale (Scale the application by running multiple copies of the application behind a LB) | The frequency of CD is very difficult to be reduced.         |
|                                                              | Becomes obstacle in development scaling.                     |
|                                                              | Requires a long-term commitment to stack.                    |

