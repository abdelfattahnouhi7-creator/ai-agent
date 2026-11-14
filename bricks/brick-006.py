import importlib.util
from pathlib import Path

def load_brick(brick_name, func_name):
    brick_path = Path(__file__).parent / f"{brick_name}.py"
    spec = importlib.util.spec_from_file_location(brick_name.replace("-", "_"), brick_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)

# استرجاع اللبنات السابقة ديناميكياً
safe_clean_price = load_brick("brick-005", "safe_clean_price")
safe_percentage = load_brick("brick-003", "safe_percentage")
safe_divide = load_brick("brick-002", "safe_divide")

def safe_total_with_discount(raw_price, discount_percent):
    # 1. تنظيف الثمن وتحويله إلى float نقي باستعمال brick-005
    price = safe_clean_price(raw_price)
    
    # 2. الاستعمال الحقيقي لـ brick-003 (safe_percentage) للحصول على نسبة التخفيض الفعلي وتأكيد صحتها
    # النتيجة هنا هي قيمة التخفيض المئوية (مثلا 20.0)
    discount_ratio = safe_percentage(discount_percent, 100)
    
    # 3. حساب النسبة المتبقية للدفع (مثلا 100 - 20 = 80%)
    remaining_percentage = 100.0 - discount_ratio
    
    # 4. الاستعمال الحقيقي لـ brick-002 (safe_divide) للقسمة على 100 بدل القسمة العادية (/)
    # الثمن النهائي = الثمن * (النسبة المتبقية / 100)
    multiplier = safe_divide(remaining_percentage, 100.0)
    
    final_price = price * multiplier
    return float(final_price)
