# IR

Language Chosen: Python
Reason: Familiarity

Requirements:

- Python v2.7
- Flask 1.0.2

Steps to run:

- Clone the repo
- go to video-endpoint directory
- run parse.py (python parse.py)
- go to localhost server in browser where flask runs. Ex: http://127.0.0.1:5000/

Sample screenshots and high level design are in the screenshots folder.

Based on the requirements -

1. XML parsing is done in python with a separate class that does the parsing recursively and fetches the desired tags.
2. Output is displayed using flask's jinja templating engine
3. Considered writing a script to fetch data every minute but went with refreshing the page every minute.
4. The page refresh happens on the frontend. A call to refresh the page is triggered every minute which essentially pulls data from backend.


