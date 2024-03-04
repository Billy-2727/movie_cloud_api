import argparse
import requests
import json
from tabulate import tabulate

parser = argparse.ArgumentParser(
    description="Returns information about movies filtered by title, genre or director. Please use quotes around your input."
)
parser.add_argument(
    "--title",
    type=str,
    help="Returns table of information about a specific movie",
)
parser.add_argument(
    "--genre",
    type=str,
    help="Returns table movies in a specific genre",
)
parser.add_argument(
    "--director",
    type=str,
    help="Returns table of movies directed by given director",
)
args = parser.parse_args()

title = args.title
genre = args.genre
director = args.director

if not (title or genre or director):
    print("Please provide either '--title' or '--genre' or '--director' parameter.")
else:
    if title:
        query_param = f"title={title}"
    elif genre:
        query_param = f"genre={genre}"
    else:  # Director is provided
        query_param = f"director={director}"

    arg_input, raw_input = query_param.split("=")
    split_input = raw_input.split()
    camel_case_input = [word.capitalize() for word in split_input]
    replace_space = "+".join(camel_case_input)
    formatted_query = f"{arg_input}={replace_space}"

    url = f"https://movie-list-function-27.azurewebsites.net/api/httptrigger1?{formatted_query}"
    r = requests.get(url)
    data = json.loads(r.text)
    # Extract keys from the first item for table headers
    if data:
        headers = list(data[0].keys())

        # Format data into table
        table_data = [[item.get(header, "") for header in headers] for item in data]

        # Print table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No data found.")
