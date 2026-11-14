import re

def safe_clean_price(raw_price):
    if raw_price is None:
        raise ValueError("Invalid price")
    
    # إذا كان رقماً صحيحاً أو عشرياً مباشرة
    if isinstance(raw_price, (int, float)):
        if raw_price < 0:
            raise ValueError("Price cannot be negative")
        return float(raw_price)
    
    # إذا كان نصاً (String)
    if isinstance(raw_price, str):
        cleaned = raw_price.strip()
        if not cleaned:
            raise ValueError("Invalid price")
        
        # 1. التحقق المباشر من وجود علامة السالب قبل أي تحويل
        if '-' in cleaned:
            raise ValueError("Price cannot be negative")
        
        # 2. تنظيف النص الموحد: استبدال الفاصلة بنقطة، وحذف أي حروف غير الأرقام والنقطة (مثل DH)
        cleaned = cleaned.replace(',', '.')
        numeric_str = re.sub(r'[^\d.]', '', cleaned)
        
        # التحقق من أن النص النظيف يحتوي على رقم صحيح أو عشري صالح (بدون تكرار النقاط)
        if not numeric_str or numeric_str.count('.') > 1:
            raise ValueError("Invalid price")
            
        return float(numeric_str)
        
    raise ValueError("Invalid price")
