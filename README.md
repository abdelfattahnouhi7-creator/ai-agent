# IMPACT - الميثاق هو المحقق

> **الميثاق هو المحقق الذي يجبر النموذج على إعطاء المعلومة الكاملة و ليس التخمينات.**

99% من الناس يستعملون AI هكذا:
يسألونه و يصدقونه.

نحن نستعمله هكذا:
نسأله و نطلب منه الدليل.

---

## المشكلة: AI يخمّن

بدون IMPACT، طلبنا من AI أن يبني دالة فاتورة، فأعطانا هذا:

```python
def calculate_total(prices, discount_percentage):
    subtotal = sum(prices)
    total = subtotal - (subtotal * discount_percentage / 100)
    return total
