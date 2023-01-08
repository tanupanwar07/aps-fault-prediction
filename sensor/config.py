import pymongo
import pandas as pandas
import json
from dataclasses import dataclass
import os
@dataclass
class Env_Variable:
    mongodb_url:str=os.getenv("Mongo_URL")

env_var= Env_Variable()

mongo_client=pymongo.MongoClient(env_var.mongodb_url)









