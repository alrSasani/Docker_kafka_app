## things to test:
### the tests will run in a docker container and have access to all the services.

- fixtures
- Mocks
- marks
- class based
- function based


1. api
    - test connection
    - test if the data is correct and you can also use data models to make sure it is valid data
```python
    import test44


```
2. psgl DB
    - test connection
    - test create table 
    - test put data
    - remove all

3. mongo DB
    - test connection
    - test create collection 
    - test put data
    - remove all

4. kafka producer
    - test if it can connect to api
    - test if it can get the data
    - test if it gets the same data

5. kafka consumer
    - test if you get data from producer
    - test if you have access to DBs
    - test if you can save to DBs
    - test if the data are correctly saved to DBs
