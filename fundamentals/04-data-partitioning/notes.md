# Sharding, Data Partitioning

Division of request pool among servers is Data Partitioning.

![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/request-pooling.svg)

There are 3 types of partitioning:

| Types       | Horizontal Paritioning                                       | Vertical Partitioning                                        | Directory-based Partitioning                                 |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Description | Range-based partitioning. Puts different rows into different tables. | Divide data for a specific feature to their own server       | A lookup service that knows the partitioning scheme and abstract away from database access code. <br />Allows addition of database servers or partitioning schemes without impacting applications. |
| Pros        |                                                              | Straight forward to implement.<br />Low impact on application. |                                                              |
| Cons        | If the value whose range is used for sharding isn't chosen carefully, the scheme will lead to unbalanced servers. | To support growth of application, database may need  further partitioning. | Can be single point of failure.                              |
|             | ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/horizontalpartitioning.svg) | ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/verticalpartitioning.svg) |                                                              |

## Partitioning criteria

1. **Key or hash-based partitioning**
   - Φ(key-attribute of entry) = #partition
   - *Problem*: Addition of new servers ⇒ Redistribution of data and service downtime
     - Fix: Consistent Hashing
2. **List partitioning**
   - Each partition is assigned a list of values
3. **Round robin partitioning**
   - With *n* partitions, the tuple<sub>i</sub> is assigned to (partition)<sub>i%n</sub>.
4. **Composite partitioning**
   - Combination of the above. E.g., consistent hashing.

## Sharding v/s Partitioning

  ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/horizontalpartitioning.svg)
