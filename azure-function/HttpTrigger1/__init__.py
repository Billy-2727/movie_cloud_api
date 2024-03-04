import json
import logging
import azure.functions as func
from azure.cosmos import CosmosClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    # Replace with your Cosmos DB connection details
    cosmos_connection_string = {YOUR_CONNECTION_STRING}
    database_id = "movie-db"
    container_id = "movie-list"

    # Initialize Cosmos DB client
    cosmos_client = CosmosClient.from_connection_string(cosmos_connection_string)
    database = cosmos_client.get_database_client(database_id)
    container = database.get_container_client(container_id)

    # Extract required query parameter (genre or director) from the request
    title = req.params.get("title")
    genre = req.params.get("genre")
    director = req.params.get("director")

    # Check if either genre or director is provided
    if not (title or genre or director):
        return func.HttpResponse(
            "Please provide either 'title' or 'genre' or 'director' parameter in the request.",
            status_code=400,
        )

    # Construct the query based on the provided parameter
    if title:
        query = f"SELECT c.Series_Title, c.IMDB_Rating, c.Genre, c.Director FROM c WHERE c.Series_Title = '{title}'"
    elif genre:
        query = f"SELECT c.Series_Title, c.IMDB_Rating, c.Genre, c.Director FROM c WHERE c.Genre = '{genre}'"
    else:  # Director is provided
        query = f"SELECT c.Series_Title, c.IMDB_Rating, c.Genre, c.Director FROM c WHERE c.Director = '{director}'"

    # Execute the query
    query_results = container.query_items(
        query=query,
        enable_cross_partition_query=True,  # Only if your container is partitioned
    )

    # Process the query results
    results_list = []
    for item in query_results:
        result_item = {}
        for key in ["Series_Title", "IMDB_Rating", "Genre", "Director"]:
            if key in item:
                result_item[key] = item[key]
                logging.info(f"{key}: {item[key]}")
        results_list.append(result_item)

    # Return JSON response
    return func.HttpResponse(
        json.dumps(results_list), status_code=200, mimetype="application/json"
    )
