# core/redeem_logic.py

from utils.file_manager import get_path, load_json, save_json

REDEEM_FILE = get_path("data", "redeem_codes.json")
USER_DATA_FILE = get_path("data", "user_data.json")


def validate_redeem_code(code: str) -> int:
    """
    Validate redeem code permanently.
    Returns:
        coins awarded (0 = invalid or already used)
    """
    if not code:
        return 0

    code = code.upper().strip()

    # Load redeem codes (constant)
    redeem_codes = load_json(REDEEM_FILE, default={})

    # If code does not exist
    if code not in redeem_codes:
        return 0

    # Load user data (dynamic)
    user_data = load_json(USER_DATA_FILE, default={
        "coins": 0,
        "used_redeem_codes": []
    })

    # Already used?
    if code in user_data.get("used_redeem_codes", []):
        return 0

    # Redeem successful
    coins = redeem_codes[code]

    # Mark as used
    user_data["used_redeem_codes"].append(code)

    # Save back to disk
    save_json(USER_DATA_FILE, user_data)

    return coins
