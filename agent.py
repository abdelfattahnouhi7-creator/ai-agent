import importlib.util
import math
from pathlib import Path


def load_brick_func(brick_name, func_name):
    brick_path = Path("bricks") / f"{brick_name}.py"
    if not brick_path.exists():
        raise FileNotFoundError(f"الملف {brick_path} غير موجود")
    spec = importlib.util.spec_from_file_location(brick_name.replace("-", "_"), brick_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)


def run_impact_audit():
    audit_suite = [
        {
            "id": "brick-001",
            "func_name": "average",
            "tests": [
                ({"nums": [10, 20, 30]}, 20.0),
                ({"nums": [5]}, 5.0),
                ({"nums": (2, 4, 6)}, 4.0),
            ],
        },
        {
            "id": "brick-002",
            "func_name": "safe_divide",
            "tests": [
                ({"a": 10, "b": 2}, 5.0),
                ({"a": 5, "b": 0}, ValueError),
                ({"a": "10", "b": 2}, ValueError),
            ],
        },
        {
            "id": "brick-003",
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
    results_summary = []

    print("=" * 65)
    print("🚀 بدء نظام تدقيق وتشغيل اللبنات (IMPACT Audit System - Final)")
    print("=" * 65)

    for brick in audit_suite:
        b_id = brick["id"]
        f_name = brick["func_name"]
        tests = brick["tests"]

        passed_count = 0
        brick_failures = []

        try:
            func = load_brick_func(b_id, f_name)
        except Exception as e:
            results_summary.append((b_id, 0, len(tests), f"فشل في التحميل: {e}"))
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
                    brick_failures.append(f"Test {idx} failed: got {res}, expected {expected}")
            except Exception as e:
                if expected == ValueError and type(e) is ValueError:
                    passed_count += 1
                    total_passed += 1
                else:
                    brick_failures.append(
                        f"Test {idx} raised unexpected error: {type(e).__name__} - {e}"
                    )

        status_msg = "نجح بالكامل" if not brick_failures else " | ".join(brick_failures)
        results_summary.append((b_id, passed_count, len(tests), status_msg))

    print("\n📊 جدول نتائج تدقيق اللبنات:")
    print("-" * 65)
    print(f"{'اللبنة (Brick)':<12} | {'النجاح':<8} | {'الحالة':<38}")
    print("-" * 65)

    for b_id, passed, total, status in results_summary:
        status_icon = "✅ ناجح" if passed == total else f"❌ جزئي/فشل ({status})"
        print(f"{b_id:<12} | {passed}/{total:<6} | {status_icon}")

    print("-" * 65)
    print(f"🎯 النتيجة الإجمالية: {total_passed}/{total_tests} اختبار ناجح.")
    print("=" * 65)


if __name__ == "__main__":
    run_impact_audit()
