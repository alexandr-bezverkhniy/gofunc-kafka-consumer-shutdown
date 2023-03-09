# gofunc-kafka-consumer-shutdown
POC to test graceful shutdown in go - kafka consumer via shopify/sarma

## Requirements:

- Pyhton 3.x
- [HTTPx CLI](https://github.com/servicex-sh/httpx#how-to-install) - httpx is a CLI to execute requests from JetBrains Http File. See more docs [here](https://httpx.sh/docs/tutorial-basics/misc)

## Run test

**1.** Start docker cluster:
```
docker-compose up -d
```
Make sure it is up and run

**2.** Start consumer via:
```
go run sample-sarma.go
```
You should see next log messages in case of success:
```
2023/03/09 13:11:05 Starting a new Sarama consumer
2023/03/09 13:11:08 Sarama consumer up and running!...
```

**3.** Init new virtual environment for Python and activate it
```
python3 -m venv .venv &&  source ./.venv/bin/activate
```

**4.** Run the test publisher 
```
python test.py -c 1000 
```
where `-c 1000` count of messages


## TODO

- Test all the ways to graceful shutdown go-routines ([good article](https://www.rudderstack.com/blog/implementing-graceful-shutdown-in-go/))
