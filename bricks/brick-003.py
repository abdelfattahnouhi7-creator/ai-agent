import importlib.util
from pathlib import Path

# تحميل لبنة brick-002.py مباشرة بالمسار ديالها بلا ما نبدلو سمية الملف
brick_path = Path(__file__).parent / "brick-002.py"
spec = importlib.util.spec_from_file_location("brick_002", brick_path)
brick_002 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brick_002)
safe_divide = brick_002.safe_divide


def safe_percentage(part, total):
    if not isinstance(part, (int, float)) or not isinstance(total, (int, float)):
        raise ValueError("Values must be numbers")
    if total == 0:
        raise ValueError("Total cannot be zero")
    if part < 0 or total < 0:
        raise ValueError("Values cannot be negative")
    if part > total:
        raise ValueError("Part cannot be greater than total")
    
    return safe_divide(part, total) * 100
