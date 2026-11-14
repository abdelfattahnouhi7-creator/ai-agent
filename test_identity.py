# test_identity.py
# المحقق ديال الفكرة 2
# كيجرب واش الموديل كيحترم قوانين العقل في السلوك، ماشي غير في المعرفة
# البديهيات: A = A / عدم التناقض / الثالث المرفوع

import re

# ==========================================
# الفخ 1 - قانون الهوية: A = A
# ==========================================
# A = دالة كترجع float
# إلا رجعات شي نوع آخر، راه بدلات A في الوسط

def check_identity(result, expected_type=float):
    """
    واش A بقات A؟
    result: النتيجة اللي رجعها الموديل
    expected_type: النوع اللي بدينا بيه - float
    """
    if type(result) != expected_type:
        return {
            "pass": False,
            "law": "A = A",
            "reason": f"بدلتي A في الوسط. بدينا بـ {expected_type.__name__} و سالينا بـ {type(result).__name__}",
            "result": result
        }
    return {
        "pass": True,
        "law": "A = A",
        "reason": f"A بقات A - رجعتي {expected_type.__name__}",
        "result": result
    }

# ==========================================
# الفخ 2 - قانون عدم التناقض
# ==========================================
# ما يمكنش تقول A و لا-A في نفس الوقت
# مثال: تقول "الكود صحيح" و "الكود فيه غلط" في نفس الجواب

def check_no_contradiction(answer: str):
    """
    واش الجواب فيه تناقض؟
    answer: الجواب ديال الموديل كنص
    """
    answer_lower = answer.lower()

    # زوج ديال الكلمات اللي ما يمكنش يكونو بجوج في نفس الحكم
    contradictions = [
        ("صحيح", "غالط"),
        ("صحيح", "خطأ"),
        ("مزيان", "غالط"),
        ("float", "string"),
        ("نعم", "لا"),
        ("yes", "no"),
        ("true", "false"),
    ]

    found = []
    for a, b in contradictions:
        if a in answer_lower and b in answer_lower:
            # إلا كانو بجوج - واش واحد فيهم منفي؟ إلا لا، راه تناقض
            # مثال: "ماشي غالط" ماشي تناقض
            found.append((a, b))

    if found:
        return {
            "pass": False,
            "law": "عدم التناقض",
            "reason": f"قلتي A و لا-A في نفس الوقت: {found}",
            "answer": answer
        }
    return {
        "pass": True,
        "law": "عدم التناقض",
        "reason": "ما كاينش تناقض - قلتي حاجة وحدة",
        "answer": answer
    }

# ==========================================
# الفخ 3 - قانون الثالث المرفوع
# ==========================================
# إما A أو لا-A. ما كاينش حالة وسط.
# إما PASS أو FAIL. ما كاينش MAYBE.

FORBIDDEN_MIDDLE_WORDS = [
    "ممكن", "تقريبا", "تقريباً", "على حسب",
    "maybe", "almost", "depends", "perhaps",
    "نوعا ما", "إلى حد ما", "قد يكون",
]

def check_excluded_middle(answer: str):
    """
    واش الموديل هرب للحالة الوسط؟
    answer: الجواب ديال الموديل
    """
    answer_lower = answer.lower()

    found_middle = [w for w in FORBIDDEN_MIDDLE_WORDS if w in answer_lower]

    if found_middle:
        return {
            "pass": False,
            "law": "الثالث المرفوع",
            "reason": f"هربتي للحالة الوسط. قلتي: {found_middle}. الحكم خاصو يكون إما آه أو لا.",
            "answer": answer
        }
    return {
        "pass": True,
        "law": "الثالث المرفوع",
        "reason": "حكم واضح - إما A أو لا-A، ما هربتيش للوسط",
        "answer": answer
    }

# ==========================================
# المحقق الكامل - كيجمع 3 قوانين
# ==========================================

def check_model_behavior(code_result, text_answer: str):
    """
    كيجرب السلوك كامل ديال الموديل في 3 قوانين
    code_result: النتيجة اللي رجعها الكود ديال الموديل
    text_answer: الجواب النصي ديال الموديل
    """
    r1 = check_identity(code_result)
    r2 = check_no_contradiction(text_answer)
    r3 = check_excluded_middle(text_answer)

    all_pass = r1["pass"] and r2["pass"] and r3["pass"]

    return {
        "all_pass": all_pass,
        "identity": r1,
        "no_contradiction": r2,
        "excluded_middle": r3,
    }

# ==========================================
# تجربة المحقق براسو
# ==========================================

if __name__ == "__main__":
    print("=== تجربة المحقق ديال الفكرة 2 ===\n")

    # مثال 1 - موديل احترم القوانين
    print("--- مثال 1: موديل مزيان ---")
    res = check_model_behavior(315.45, "لا، الكود ما كيرجعش float")
    print(f"A = A: {res['identity']}")
    print(f"عدم التناقض: {res['no_contradiction']}")
    print(f"الثالث المرفوع: {res['excluded_middle']}")
    print(f"النتيجة: {'PASS' if res['all_pass'] else 'FAIL'}\n")

    # مثال 2 - موديل خرق A = A
    print("--- مثال 2: موديل خرق A = A ---")
    res = check_model_behavior("315.45", "نعم الكود مزيان")
    print(f"A = A: {res['identity']}")
    print(f"النتيجة: {'PASS' if res['all_pass'] else 'FAIL'}\n")

    # مثال 3 - موديل هرب للحالة الوسط
    print("--- مثال 3: موديل هرب للوسط ---")
    res = check_model_behavior(315.45, "ممكن يكون صحيح تقريبا على حسب")
    print(f"الثالث المرفوع: {res['excluded_middle']}")
    print(f"النتيجة: {'PASS' if res['all_pass'] else 'FAIL'}\n")
