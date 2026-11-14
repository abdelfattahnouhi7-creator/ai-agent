# MY-IMPACT

مشروع كيثبت بلي الفائز ماشي اللي كيجيب الكود، الفائز هو اللي كيجيب الدليل.

## النتيجة النهائية - 14 نونبر 2026

| الموديل | النتيجة |
| :--- | :--- |
| Muse Spark | 4/4 ✅ + |
| Claude | 4/4 ✅ |
| ChatGPT | 4/4 ✅ |
| Gemini | 1/4 ❌ |

## agent.py v3 - 6/6 ✅

جمعنا التنظيف ديال Muse Spark + pytest ديال Claude.

- كيفهم: `DH` + `MAD` + `درهم` + `د.م`
- كيرفض: اللائحة الخاوية، الثمن السالب، التخفيض > 100، `None`
- الاختبارات: `test_agent.py` - 6 tests

## كيفاش تجرب؟

```bash
pip install pytest
pytest test_agent.py -v
