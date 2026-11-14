# agent_ideas.py - المحقق ديال الأفكار
# MY-IMPACT v2 - داز في المحقق 6/6
# القاعدة: أي فكرة خاصها تجيب 4/4 عاد تتقبل

def check_idea(idea_text):
    """
    idea_text: هو النص ديال الفكرة اللي عطاك AI
    كيرجع: score / 4 + التقرير
    """
    text = idea_text.lower()
    score = 0
    report = []

    # --- 1. شكون هو المستفيد بالضبط؟ ---
    # إلا قال "الناس" و "الجميع" و ما عطاش شخص محدد = FAIL
    vague_words = ["الناس", "الجميع", "الكل", "الناس كاملين", "les gens", "everyone", "people"]
    # خاصو يعطي تفاصيل: عمر، مدينة، مهنة
    has_person = any(w in text for w in ["عمر", "سنة", "كنيطرة", "تاجر", "طالب", "أستاذ", "سائق", "صاحب", "سيدة", "شاب"])
    has_vague_only = any(w in text for w in vague_words) and not has_person

    if has_vague_only:
        report.append("❌ 1/4 - المستفيد: FAIL - قلتي 'الناس'، شكون بالضبط؟ شحال في عمرو؟ فين كيعيش؟")
    elif has_person:
        score += 1
        report.append("✅ 1/4 - المستفيد: PASS - شخص محدد")
    else:
        report.append("❌ 1/4 - المستفيد: FAIL - ما حددتيش شكون هو المستفيد")

    # --- 2. شنو المشكل الحقيقي؟ ---
    has_problem = any(w in text for w in ["مشكل", "مشكلة", "كيعاني", "كيتشكى", "صعوبة", "كيضيع", "probleme", "مشكل"])
    if has_problem:
        score += 1
        report.append("✅ 2/4 - المشكل: PASS - مشكل حقيقي مذكور")
    else:
        report.append("❌ 2/4 - المشكل: FAIL - ما قلتيش شنو المشكل اللي كيعاني منو")

    # --- 3. شنو الحل المختلف؟ ---
    has_diff = any(w in text for w in ["مختلف", "ماشي بحال", "فرق", "جديد", "مختلف على", "différent", "different"])
    if has_diff:
        score += 1
        report.append("✅ 3/4 - الحل المختلف: PASS - قلتي علاش مختلف")
    else:
        report.append("❌ 3/4 - الحل المختلف: FAIL - علاش الحل ديالك ماشي بحال اللي كاين؟")

    # --- 4. كيفاش نجربو بأقل تكلفة؟ ---
    has_test = any(w in text for w in ["نجرب", "تجربة", "أسبوع", "بلا فلوس", "محادثة", "ورقة", "فيديو", "نسول", "test", "تجرب"])
    has_app_only = "تطبيق" in text and not has_test
    if has_app_only:
        report.append("❌ 4/4 - التجربة: FAIL - قلتي 'ندير تطبيق'، هادي ماشي تجربة صغيرة. شنو أول خطوة هاد الأسبوع بلا فلوس؟")
    elif has_test:
        score += 1
        report.append("✅ 4/4 - التجربة: PASS - تجربة صغيرة مذكورة")
    else:
        report.append("❌ 4/4 - التجربة: FAIL - كيفاش غادي تجربو بأقل تكلفة؟")

    # --- الحكم النهائي ---
    print(f"\n=== المحقق ديال الأفكار - MY-IMPACT v2 ===")
    for r in report:
        print(r)
    print(f"\nالنتيجة: {score}/4")
    if score == 4:
        print("✅ مقبولة - فكرة دازت في المحقق")
    else:
        print(f"❌ مرفوضة - جابت {score}/4، خاصها ترجع تتصلح")
    print("="*40)
    return score

# --- تجربة المحقق ---
if __name__ == "__main__":
    # فكرة 1: تخمين - غادي تفشل
    idea_bad = "فكرة مشروع للناس كاملين، ندير تطبيق ديال الفواتير"
    print("\n--- الفكرة 1: تخمين ---")
    check_idea(idea_bad)

    # فكرة 2: مركبة - غادي تنجح
    idea_good = """
    المستفيد: تاجر صغير في كنيطرة، عمرو 35 سنة، عندو محل ديال الملابس
    المشكل: كيعاني حيت كيحسب الفاتورة بيدو و كيضيع الوقت و كيغلط في الحساب
    الحل المختلف: ماشي بحال التطبيقات الكبار، هادا بسيط و بالدارجة و كيخدم بلا انترنت
    التجربة: هاد الأسبوع نجرب - نسول 3 تجار في السوق واش بغاو هادشي، بلا فلوس، غير محادثة
    """
    print("\n--- الفكرة 2: مركبة ---")
    check_idea(idea_good)
