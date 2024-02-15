@echo off
TITLE Radiux Robot
:: Enables virtual env mode and then starts Radiux
env\scripts\activate.bat && py -m RadiuxManager
