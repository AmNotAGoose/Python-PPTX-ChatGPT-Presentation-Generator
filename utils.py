import json

from apis import openai_api, cohere_api

default_config_path = "./config/config.json"
default_settings_path = "./config/options.json"
default_save_location = "./generated_presentations"


def save_config(api_key):
    config_object = {
        'api_key': api_key,
        'save_location': default_save_location,
    }

    config_object_string = json.dumps(config_object)

    with open(default_config_path, 'w') as f:
        f.write(config_object_string)


def get_config() -> dict:
    with open(default_config_path, 'r') as f:
        config_object = json.load(f)
        return config_object


def get_settings() -> dict:
    with open(default_settings_path, 'r') as f:
        settings_object = json.load(f)
        return settings_object


def get_api_list():
    return list(get_settings()["models"].keys())


def get_model_list_from_api(api):
    return get_settings()["models"][api]
