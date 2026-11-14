import importlib.util
from pathlib import Path

def load_brick(brick_name, func_name):
    brick_path = Path(__file__).parent / f"{brick_name}.py"
    spec = importlib.util.spec_from_file_location(brick_name.replace("-", "_"), brick_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)

# استرجاع اللبنات السابقة
average = load_brick("brick-001", "average")
safe_percentage = load_brick("brick-003", "safe_percentage")

def safe_average_percentage(scores):
    if not isinstance(scores, (list, tuple)):
        raise ValueError("Scores must be a list or tuple")
    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")
    
    # 1. حساب المعدل باستخدام brick-001
    avg = average(scores)
    
    # 2. حساب النسبة المئوية للمعدل على 100 باستخدام brick-003
    return safe_percentage(avg, 100)
