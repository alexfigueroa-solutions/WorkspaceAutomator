import json
import os

# Path to the default profile
DEFAULT_PROFILE_PATH = os.path.join(os.getcwd(), 'profiles', 'default', 'default.json')

def load_profile(profile_name="default"):
    with open(os.path.join(DEFAULT_PROFILE_PATH, 'r')) as file:
        return json.load(file)
