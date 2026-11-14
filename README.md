# 🤖 My First AI Agent

Agent كيجرب الكود، كيعاود، وكيصلح راسو بوحدو باستعمال Google Gemini.

## شنو كيدير؟
1. كيجرب الكود بـ 3 Tests: مدخل صحيح، مدخل غالط، حالة حدية
2. إلا فشل، كيصيفط المشكل لـ Gemini
3. Gemini كيصلح الكود وكيعاود يجرب
4. كيبقى يعاود حتى ينجح 3/3 ولا يساليو 3 محاولات

## شنو تعلمت؟
- ربطت Agent بـ API حقيقي ديال Google Gemini
- حليت خطأ 400 - المفتاح غالط
- حليت خطأ 404 - الموديل قديم (2.5-flash-lite -> 3.5-flash-lite)
- حليت Timeout - الكونيكسيون
- فهمت أن Tests ساهلين كيعطيو نجاح زائف
- الفرق بين كود خدام وكود مزيان (ZeroDivisionError vs ValueError)

## مثال
```python
# قبل
def add(a, b):
    return a * b

# من بعد ما صلحو Gemini
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid input")
    return a + b
