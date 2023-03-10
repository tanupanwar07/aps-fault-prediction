import pymongo
import pandas as pd
import json

from sensor.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb.

database_name="aps"
collection_name="sensor"

data_file_path="/config/workspace/aps_failure_training_set1.csv"


if __name__=="__main__":
    df=pd.read_csv(data_file_path)
    print(f"rows and cols: {df.shape}")

 # convert dataframe to json to dump record in mongodb
df.reset_index(drop=True,inplace=True)

json_record=list(json.loads(df.T.to_json()).values())
print(json_record[0])


# insert converted json record  in mongodb

mongo_client[database_name][collection_name].insert_many(json_record)
