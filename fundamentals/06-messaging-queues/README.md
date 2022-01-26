# Messaging Queues

The following is a typical implementation of a system without messaging queue.

![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/typicalsystemswithoutmq.svg)

The issue here is as requests increases more and more, the load on management system would increase, to the point where it would ultimately stop taking in requests as it would not have any resources to process the request. This is bad for business as it would cause customers to loose interest thereby declining popularity of the business. We wouldn't want that right ?

We would take implement the inherent idea behind producer-consumer problem using messaging queues.

The following is a simple implementation of the above.

 ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/asyncsystemwithmq.svg)

Now the brunt of the load is taken off by the messaging queues.
