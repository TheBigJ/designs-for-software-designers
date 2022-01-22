# Data Partitioning

Data partitioning is a method of distributing data across multiple tables, systems or sites to improve query processing performance and make the data more manageable.

## Ok, but why ? 😐

Let's imagine we have a table on `product` available on any e-commerce website.

The columns ought to be present in the database are as follows:

- Product Id (*PRIMARY_KEY*)
- Company name 
- Product name
- Price
- Discount
- Product type
- Description
- Availability

So, let's say we keep adding data into our table the size of the table grows, reaching the size of around 50M rows and everyday we keep adding more products, querying the prices of old products and updating the details of products in real-time.

The problem here is scalability, as we data more data the time required to perform a simple query increases drastically, consequently increasing time to insert a new row or updating an existing row, most definitely causing problems in business and maintenance and management will for sure start to run into issues.

## Partitioning criteria

High-end RDBMS provide for different criteria to split the database. They take a *partitioning key* and assign a   partition based on certain criteria.

- **Range-based partitioning**: Here a partition is selected by determining if the partitioning key is within a certain range.

  For example, in the above `product` table, a valid partition could be for all products, with `Product name` starting between A-D. It distributes tuples based on the value intervals (ranges) of some attributes. In addition to supporting range queries, it is well-suited for exact-match queries.

- **List partitioning**: Here a partition is assigned a list of values. If the partitioning key has one of these values, the partition is chosen.

  For example, in the above `product` table, all the rows where the `Company name` is either `Nestle`, `PepsiCo`, `Cadbury`, etc, could build a partition for the `Food and beverages products` partition.

- **Round-robin partitioning**: Here uniform data distribution is ensured. With `n` partitions, `i`<sup>th</sup> tuple in insertion order is assigned to partition `(i mod n)`. This strategy enables the sequential access to a relation to be done in parallel. 

  > The direct access, howsoever, to individual tuples, based on a predicate, requires accessing the entire relation.

- **Hash partitioning**: It applies a *hash function* to some attribute that yields the partition number. This strategy allows exact-match queries on the selection attribute to be process by one node and all other queries to be processed by all the nodes in parallel.

-  **Composite partitioning**: Here the partitioning allows for certain combinations of the above partitioning scheme, by for example, first applying a range partitioning and then a hash partitioning.
  *Consistent hashing* could be considered a composite of hash and list partitioning where the hash reduces the key spaces to a size that can be listed.

## Partitioning methods

1. **Horizontal partitioning**: It involves putting different rows into different tables. For example, products with `Food type` cereals, drinks, beverages, etc are stored in `ProductsFood` whereas shampoo, hand sanitizers, soaps, etc are stored in `ProductsPersonalHygiene`. The partition tables are then called `ProductsFood` and `ProductsPersonalHygiene`, while a view with a union of these tables might be created over both of them to provide a complete view of all customers.

2. **Vertical partitioning**: It involves creating tables with fewer columns and using additional tables to store the remaining columns. Generally this practice is known as normalization. However, the vertical partitioning extends further and partitions columns even when already normalized. This type of splitting is also called *row splitting*, since rows get split by their columns, and might be performed explicitly or implicitly.

   A common form of vertical partitioning is to split static data from dynamic data, since the former is faster to access from the latter, particularly from a table where the dynamic data is not used as often as static. Creating a view across the two newly created tables restores the original table with a performance penalty, but accessing the static data alone with show higher performance.

   A columnar database can be regarded as a database that has been vertically partitioned until each column is stored in its own table.

## What about sharding ? What is it then ?? 😕

Before going to sharding, let's try exploring the concept first. Each shard is a horizonal partition of data in a database or search engine, each being held on a separate database server instance, to spread load. Some data within a database remains present in all shards, but some appear only in a single shard, each acts as the single source for this subset of data.

### Umm... how is this different from horizontal partitioning ? 😑

Horizontal partitioning splits one or more tables by row, usually within a single instance of a schema and a database server. It may offer an advantage by reducing index size (*resulting in reduced latency in search effort*) provided that there is some obvious, robust, implicit way to identify in which a particular row will be found, without first needing to search the index, e.g., the classic example of `ProductsFood` and `ProductsPersonalHygiene`, where their product type already indicates where they will be found.

You see, *sharding* goes way beyond this. It partitions the problematic table(s) in the same way, but it does this across potentially *multiple* instances of the schema. The obvious advantage would be that search load for the large partitioned table can now be split across multiple servers, not just multiple indexes on the same logical server.

Let me explain using a real example, MongoDB. So MongoDB supports *horizontal scaling* **TODO**

![](https://docs.mongodb.com/manual/images/sharded-cluster-production-architecture.bakedsvg.svg)

