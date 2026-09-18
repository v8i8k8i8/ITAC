import os
import yaml


ENV = os.getenv("ENV", "qa")


config_path = f"configs/env/{ENV}.yml"

with open(config_path, "r") as file:
    config = yaml.safe_load(file)