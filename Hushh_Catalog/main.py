#Creating a Catalog

import glob
from PIL import Image
import json
from tqdm import tqdm
import pandas as pd
import os
from data_ingestion import receive_data 
import asyncio
#Data Ingestion
access_token = input("Enter your access_token : ")
brand_name = input("Enter your brand_name : ")

asyncio.get_event_loop().run_until_complete(receive_data(access_token, brand_name))

