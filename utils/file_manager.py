import json
import os

# ---------------------------------------------------------
#  PATH HANDLING
# ---------------------------------------------------------

def get_path(*paths) -> str:
    """
    Create an absolute path relative to the project root.
    Example: get_path("data", "user_data.json")
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    return os.path.join(base_dir, *paths)


# ---------------------------------------------------------
#  JSON LOADING / SAVING
# ---------------------------------------------------------

def load_json(path: str, default=None):
    """
    Safely load a JSON file.
    Returns `default` if the file does not exist or is invalid.
    """
    if not os.path.exists(path):
        return default

    try:
        with open(path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(path: str, data: dict):
    """
    Safely write to a JSON file.
    Creates missing directories automatically.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
