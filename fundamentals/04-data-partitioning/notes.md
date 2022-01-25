# Sharding, Data Partitioning

Division of request pool among servers is Data Partitioning.

![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/request-pooling.svg)

There are 3 types of partitioning:

| Types       | Horizontal Paritioning                                       | Vertical Partitioning                                        | Directory-based Partitioning                                 |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Description | Range-based partitioning. Puts different rows into different tables. | Divide data for a specific feature to their own server       | A lookup service that knows the partitioning scheme and abstract away from database access code. <br />Allows addition of database servers or partitioning schemes without impacting applications. |
| Pros        |                                                              | Straight forward to implement.<br />Low impact on application. |                                                              |
| Cons        | If the value whose range is used for sharding isn't chosen carefully, the scheme will lead to unbalanced servers. | To support growth of application, database may need  further partitioning. | Can be single point of failure.                              |
|             | ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/horizontalpartitioning.svg) |                                                              |                                                              |

