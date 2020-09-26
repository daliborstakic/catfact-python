""" Importing module requests """
import requests

# API url
url = "https://cat-fact.herokuapp.com/facts/random"

# Data retrieval
data = requests.get(url).json()
