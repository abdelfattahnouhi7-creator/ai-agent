# 🧱 IMPACT — Modular & Verified Code System

**IMPACT** هو نظام هندسي لبناء البرمجيات بطريقة معيارية (Modular) وصارمة. الفكرة بسيطة: كل وظيفة هي **"لبنة" (Brick)** مستقلة، مجربة، وموثقة بملف `.json`، واللبنات الجديدة كتتركب فوق القديمة بلا إعادة كتابة الكود أو تخمين.

## 📜 قواعد IMPACT الخمس
1. **جرب قبل ما تقول صافي:** أي لبنة خاصها تنجح في جميع الاختبارات الصارمة قبل اعتمادها.
2. **إلا فشل، صلح وعاود:** لا يتم التخلي عن الكود عند الخطأ، بل يُصلح ويعاد اختباره.
3. **رفض واضح:** عند أي مدخل خاطئ، يتم إرجاع `ValueError` صريح ومفهوم.
4. **وثق كلشي:** كل لبنة `.py` مرفوقة بملف `.json` يشرح مدخلاتها، مخرجاتها، والأخطاء التي تعالجها.
5. **ما تعاودش تبني اللي تبنى:** أي وظيفة موجودة في لبنة سابقة يتم استيرادها واستعمال نتائجها مباشرة.

---

## 🧩 اللبنات المتوفرة (6 لبنات)

| اللبنة | الدالة | الوظيفة | اللبنات المستعملة (Reused) | الاختبارات |
| :--- | :--- | :--- | :--- | :---: |
| **`brick-001`** | `average` | حساب المعدل الحسابي لقائمة أرقام بأمان | — | **3/3** ✅ |
| **`brick-002`** | `safe_divide` | قسمة آمنة تمنع القسمة على صفر وتتحقق من الأرقام | — | **3/3** ✅ |
| **`brick-003`** | `safe_percentage` | حساب النسبة المئوية مع رفض القيم السالبة أو الأكبر من المجموع | `brick-002` | **4/4** ✅ |
| **`brick-004`** | `safe_average_percentage` | حساب المعدل ثم تحويله لنسبة مئوية على 100 | `brick-001`, `brick-003` | **4/4** ✅ |
| **`brick-005`** | `safe_clean_price` | تنظيف وتحويل الأثمنة النصية (`"100 DH"`, `"100,50"`) إلى `float` | — | **4/4** ✅ |
| **`brick-006`** | `safe_total_with_discount` | تنظيف الثمن وحساب السعر النهائي بعد التخفيض | `brick-005`, `brick-003`, `brick-002` | **4/4** ✅ |

**🎯 المجموع العام للاختبارات:** **22/22 اختبار ناجح (100%)** عبر المدقق المركزي `agent.py`.

---

## 🚀 مثال سريع للاستعمال الصحيح

بما أن أسماء الملفات تحتوي على شرطة (`-`)، يتم تحميل واستعمال اللبنات بالطريقة الديناميكية الآمنة:

```python
import importlib.util
from pathlib import Path

# دالة التحميل المعتمدة في نظام IMPACT
def load_brick(brick_name, func_name):
    brick_path = Path("bricks") / f"{brick_name}.py"
    spec = importlib.util.spec_from_file_location(brick_name.replace("-", "_"), brick_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)

# استدعاء لبنة safe_total_with_discount
safe_total_with_discount = load_brick("brick-006", "safe_total_with_discount")

# حساب الثمن النهائي لسلعة ثمنها "200 DH" مع تخفيض 20%
final_price = safe_total_with_discount("200 DH", 20)
print(final_price)  # Output: 160.0
