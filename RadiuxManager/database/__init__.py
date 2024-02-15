#MIT License
#Copyright (c) 2023, ©NovaNetworks

from async_pymongo import AsyncClient

from RadiuxManager import MONGO_DB_URI

DBNAME = "RadiuxManager"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
