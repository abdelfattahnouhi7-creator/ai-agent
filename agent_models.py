# agent_models.py - Brick 2 - المحقق ديال الموديلات
# الفكرة 1: شكون الموديل اللي ما كيكدبش عليك؟

def check_model_answer(answer_text):
    """
    answer_text: هو الجواب اللي عطاك الموديل
    كيرجع: score / 4 + التقرير
    نفس المحقق ديال agent_ideas.py ولكن للأجوبة ديال الموديلات
    """
    text = answer_text.lower()
    score = 0
    report = []

    # 1. واش نظف الثمن؟ - ماشي sum() مباشرة
    if "replace" in text or "strip" in text or "clean" in text or "نظف" in text:
        score += 1
        report.append("✅ 1/4 - تنظيف: PASS - نظف الثمن قبل الحساب")
    else:
        report.append("❌ 1/4 - تنظيف: FAIL - استعمل sum() مباشرة بلا تنظيف")

    # 2. واش رفض اللائحة الخاوية بـ ValueError؟
    if "valueerror" in text and ("خاوية" in text or "empty" in text or "خاوي" in text):
        score += 1
        report.append("✅ 2/4 - اللائحة الخاوية: PASS - رفضها بـ ValueError")
    elif "return" in text and ("خاوية" in text or "empty" in text):
        report.append("❌ 2/4 - اللائحة الخاوية: FAIL - رجع string، ماشي ValueError - بحال Gemini")
    else:
        report.append("❌ 2/4 - اللائحة الخاوية: FAIL - ما رفضهاش")

    # 3. واش رفض التخفيض > 100 و الثمن السالب؟
    if "100" in text and ("remise" in text or "تخفيض" in text or "discount" in text) and "valueerror" in text:
        score += 1
        report.append("✅ 3/4 - الرفض: PASS - رفض التخفيض و السالب")
    else:
        report.append("❌ 3/4 - الرفض: FAIL - ما رفضش التخفيض و السالب")

    # 4. واش عطا 4 اختبارات + النتائج؟
    if "test" in text and ("assert" in text or "pytest" in text or "315.45" in text):
        score += 1
        report.append("✅ 4/4 - الاختبارات: PASS - عطا 4 اختبارات + نتائج")
    else:
        report.append("❌ 4/4 - الاختبارات: FAIL - ما عطاش 4 اختبارات - بحال Gemini")

    print("\n=== المحقق ديال الموديلات - الفكرة 1 ===")
    for r in report:
        print(r)
    print(f"\nالنتيجة: {score}/4")
    if score == 4:
        print("✅ مقبول - هاد الموديل ما كيكدبش")
    else:
        print(f"❌ مرفوض - هاد الموديل جاب {score}/4")
    print("="*40)
    return score
