# utils.py

def greet_user(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

def validate_positive_int(value, field_name="Value"):
    """Validate that the input is a positive integer."""
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{field_name} must be a positive integer.")
    return value

def calculate_total(price, qty):
    """Return total price."""
    return price * qty

def calculate_gst(amount, rate=0.18):
    """Calculate GST for a given amount."""
    return amount * rate
