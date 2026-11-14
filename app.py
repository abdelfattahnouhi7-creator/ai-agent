import importlib.util
import math
from pathlib import Path
import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="IMPACT System", page_icon="🧱", layout="centered")

# دالة التحميل الديناميكي المعتمدة في نظام IMPACT
def load_brick(brick_name, func_name):
    brick_path = Path("bricks") / f"{brick_name}.py"
    if not brick_path.exists():
        raise FileNotFoundError(f"الملف {brick_path} غير موجود")
    spec = importlib.util.spec_from_file_location(brick_name.replace("-", "_"), brick_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)

# العنوان الرئيسي
st.title("IMPACT - 🧱")
st.markdown("نظام هندسي لبناء وبرمجية اللبنات بمعايير صارمة واختبارات موثقة.")

st.divider()

# ---------------------------------------------------------
# القسم الأول: زر التدقيق الشامل (Run Audit 22/22)
# ---------------------------------------------------------
st.header("📊 تدقيق اللبنات الشامل")
st.markdown("اضغط على الزر أدناه لتشغيل جميع الاختبارات والتأكد من صحة اللبنات (22 اختبار).")

if st.button("Run Audit 22/22", type="primary"):
    audit_suite = [
        {
            "id": "brick-001",
            "name": "Average",
            "func_name": "average",
            "tests": [
                ({"nums": [10, 20, 30]}, 20.0),
                ({"nums": [5]}, 5.0),
                ({"nums": (2, 4, 6)}, 4.0),
            ],
        },
        {
            "id": "brick-002",
            "name": "Safe Divide",
            "func_name": "safe_divide",
            "tests": [
                ({"a": 10, "b": 2}, 5.0),
                ({"a": 5, "b": 0}, ValueError),
                ({"a": "10", "b": 2}, ValueError),
            ],
        },
        {
            "id": "brick-003",
            "name": "Safe Percentage",
            "func_name": "safe_percentage",
            "tests": [
                ({"part": 25, "total": 100}, 25.0),
                ({"part": 10, "total": 0}, ValueError),
                ({"part": 120, "total": 100}, ValueError),
                ({"part": -5, "total": 100}, ValueError),
            ],
        },
        {
            "id": "brick-004",
            "name": "Safe Average Percentage",
            "func_name": "safe_average_percentage",
            "tests": [
                ({"scores": [80, 90, 100]}, 90.0),
                ({"scores": []}, ValueError),
                ({"scores": [110, 120]}, ValueError),
                ({"scores": [-20, 10]}, ValueError),
            ],
        },
        {
            "id": "brick-005",
            "name": "Safe Clean Price",
            "func_name": "safe_clean_price",
            "tests": [
                ({"raw_price": "100 DH"}, 100.0),
                ({"raw_price": "100,50"}, 100.5),
                ({"raw_price": ""}, ValueError),
                ({"raw_price": "-50 DH"}, ValueError),
            ],
        },
        {
            "id": "brick-006",
            "name": "Safe Total with Discount",
            "func_name": "safe_total_with_discount",
            "tests": [
                ({"raw_price": "200 DH", "discount_percent": 20}, 160.0),
                ({"raw_price": "200,50", "discount_percent": 10}, 180.45),
                ({"raw_price": "-100 DH", "discount_percent": 15}, ValueError),
                ({"raw_price": "200 DH", "discount_percent": 120}, ValueError),
            ],
        },
    ]

    total_passed = 0
    total_tests = 0
    table_data = []

    for brick in audit_suite:
        b_id = brick["id"]
        b_name = brick["name"]
        f_name = brick["func_name"]
        tests = brick["tests"]
        
        passed_count = 0
        brick_failed = False

        try:
            func = load_brick(b_id, f_name)
        except Exception as e:
            table_data.append({
                "اللبنة": f"{b_id} ({b_name})",
                "النجاح": f"0/{len(tests)}",
                "الحالة": f"❌ خطأ في التحميل: {e}"
            })
            total_tests += len(tests)
            continue

        for idx, (kwargs, expected) in enumerate(tests, 1):
            total_tests += 1
            try:
                res = func(**kwargs)
                is_match = (
                    isinstance(res, (int, float))
                    and isinstance(expected, (int, float))
                    and math.isclose(res, expected, rel_tol=1e-9)
                ) or (res == expected)

                if is_match:
                    passed_count += 1
                    total_passed += 1
                else:
                    brick_failed = True
            except Exception as e:
                if expected == ValueError and type(e) is ValueError:
                    passed_count += 1
                    total_passed += 1
                else:
                    brick_failed = True

        status_str = "✅ ناجح بالكامل" if not brick_failed and passed_count == len(tests) else f"⚠️ جزئي ({passed_count}/{len(tests)})"
        table_data.append({
            "اللبنة": f"{b_id} ({b_name})",
            "النجاح": f"{passed_count}/{len(tests)}",
            "الحالة": status_str
        })

    # عرض الجدول في Streamlit
    st.table(table_data)
    
    if total_passed == total_tests:
        st.success(f"🎯 النتيجة الإجمالية: {total_passed}/{total_tests} اختبار ناجح بنجاح تام!")
    else:
        st.warning(f"🎯 النتيجة الإجمالية: {total_passed}/{total_tests} اختبار ناجح.")

st.divider()

# ---------------------------------------------------------
# القسم الثاني: جرب بنفسك (Safe Total with Discount)
# ---------------------------------------------------------
st.header("🧪 جرب بنفسك: حساب الثمن مع التخفيض")
st.markdown("هذا القسم يستعمل **brick-006** (التي تعتمد بدورها على brick-005 و brick-003 و brick-002).")

with st.form("discount_form"):
    col1, col2 = st.columns(2)
    with col1:
        raw_price_input = st.text_input("الثمن الخام (Raw Price)", value="200 DH")
    with col2:
        discount_input = st.number_input("نسبة التخفيض % (Discount %)", min_value=0.0, max_value=200.0, value=20.0)
    
    submitted = st.form_submit_button("حسب (Calculate)")
    
    if submitted:
        try:
            # تحميل الدالة بطريقة آمنة ديناميكياً
            safe_total_func = load_brick("brick-006", "safe_total_with_discount")
            result = safe_total_func(raw_price_input, float(discount_input))
            st.success(f"🎉 الثمن النهائي النقي: **{result}**")
        except ValueError as ve:
            st.error(f"❌ خطأ معالجة (ValueError): {ve}")
        except Exception as e:
            st.error(f"❌ حدث خطأ غير متوقع: {e}")
