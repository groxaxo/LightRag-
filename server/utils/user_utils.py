"""
User ID generation utilities
Provides username validation and automatic user_id generation
"""

import re

from pypinyin import lazy_pinyin, Style


def to_pinyin(text: str) -> str:
    """
    Convert Chinese to pinyin
    Uses pypinyin library for conversion
    """
    # Use pypinyin for conversion
    pinyin_list = lazy_pinyin(text, style=Style.NORMAL)
    return "".join(pinyin_list)


def validate_username(username: str) -> tuple[bool, str]:
    """
    Validate username format

    Args:
        username: Username

    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not username:
        return False, "Username cannot be empty"

    if len(username) < 2:
        return False, "Username must be at least 2 characters"

    if len(username) > 20:
        return False, "Username cannot exceed 20 characters"

    # Check for invalid characters
    # Allow letters, numbers, underscore, and unicode characters
    if not re.match(r"^[\w\u4e00-\u9fa5]+$", username, re.UNICODE):
        return False, "Username can only contain letters, numbers, and underscores"

    return True, ""


def generate_user_id(username: str) -> str:
    """
    Generate user_id from username

    Args:
        username: Username

    Returns:
        str: Generated user_id
    """
    # 1. Basic cleanup
    username = username.strip()

    # 2. Convert to pinyin (if contains Chinese characters)
    user_id = to_pinyin(username)

    # 3. Handle special characters, keep only letters, numbers and underscores
    user_id = re.sub(r"[^a-zA-Z0-9_]", "", user_id)

    # 4. Ensure it doesn't start with a number
    if user_id and user_id[0].isdigit():
        user_id = "u" + user_id

    # 5. If empty or too short, use default prefix
    if len(user_id) < 2:
        user_id = "user" + str(hash(username) % 10000).zfill(4)

    # 6. Length limit
    if len(user_id) > 20:
        user_id = user_id[:20]

    return user_id.lower()


def generate_unique_user_id(username: str, existing_user_ids: list[str]) -> str:
    """
    Generate unique user_id, add numeric suffix if duplicate

    Args:
        username: Username
        existing_user_ids: List of existing user_ids

    Returns:
        str: Unique user_id
    """
    base_user_id = generate_user_id(username)

    # If not duplicate, return directly
    if base_user_id not in existing_user_ids:
        return base_user_id

    # If duplicate, add numeric suffix
    counter = 1
    while True:
        candidate = f"{base_user_id}{counter}"
        if candidate not in existing_user_ids:
            return candidate
        counter += 1

        # Prevent infinite loop
        if counter > 9999:
            # Use timestamp as suffix
            import time

            candidate = f"{base_user_id}{int(time.time()) % 10000}"
            return candidate


def is_valid_phone_number(phone: str) -> bool:
    """
    Validate phone number format (supports Chinese mainland phone numbers)

    Args:
        phone: Phone number string

    Returns:
        bool: Whether it's a valid phone number
    """
    if not phone:
        return False

    # Remove spaces and special characters
    phone = re.sub(r"[\s\-\(\)]", "", phone)

    # Chinese mainland phone format: starts with 1, second digit is 3-9, total 11 digits
    pattern = r"^1[3-9]\d{9}$"

    return bool(re.match(pattern, phone))


def normalize_phone_number(phone: str) -> str:
    """
    Normalize phone number format

    Args:
        phone: Original phone number

    Returns:
        str: Normalized phone number
    """
    if not phone:
        return ""

    # Remove all non-digit characters
    phone = re.sub(r"\D", "", phone)

    # If it's a Chinese mainland phone number, ensure correct format
    if len(phone) == 11 and phone.startswith("1"):
        return phone

    return phone
