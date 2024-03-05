# Movie Cloud API
This movie cloud API allows anyone to get information about the top 1000 movies according to IMDB rating. It uses purely servless cloud technologies, CosmosDB and Azure Functions specifically. I then create a CLI program in Python using argparse to allow user input within a terminal to return the results, the results are JSON however they are returned in a neatly formatted table using the library tabulate.

# Architecture
The architecture its self is very simple however effective. At its core the main processing is being done by the Azure Function which is calling the CosmosDB based on the requests recieved by the client.
![/img/architecture.png](https://github.com/Billy-2727/movie_cloud_api/blob/master/img/architecture.png)

# Get Started
Below is a step-by-step on how to run the function call python scipt locally.

### Pre-requisites/Library Requirements
- Python (latest) - Download [here](https://www.python.org/downloads/)
- argparse -  pip install argparse
- tabulate - pip install tabulate

Once the above is installed all you need to do is clone the repository - once cloned you can run the below in you shell terminal. **Make sure you are in the script directory**
```
python call_func.py --{arg} {input} 
```
### Example
```
python call_func.py --director "Christopher Nolan"
```
![image](https://github.com/Billy-2727/movie_cloud_api/assets/81046105/c655cd3d-ad7d-4e43-aa1f-438082919bcf)
