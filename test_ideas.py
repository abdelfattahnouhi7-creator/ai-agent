# test_ideas.py - اختبارات المحقق ديال الأفكار - Brick 1
from agent_ideas import check_idea

def test_idea_bad_marfouda():
    # الفكرة الخايبة من agent_ideas.py - قالت "الناس كاملين" + "ندير تطبيق"
    idea_bad = "فكرة مشروع للناس كاملين، ندير تطبيق ديال الفواتير"
    score = check_idea(idea_bad)
    assert score < 4

def test_idea_good_maqbola():
    # الفكرة المزيانة - تاجر محدد + مشكل + حل مختلف + تجربة
    idea_good = """
    المستفيد: تاجر صغير في كنيطرة، عمرو 35 سنة، عندو محل ديال الملابس
    المشكل: كيعاني حيت كيحسب الفاتورة بيدو و كيضيع الوقت و كيغلط في الحساب
    الحل المختلف: ماشي بحال التطبيقات الكبار، هادا بسيط و بالدارجة و كيخدم بلا انترنت
    التجربة: هاد الأسبوع نجرب - نسول 3 تجار في السوق واش بغاو هادشي، بلا فلوس، غير محادثة
    """
    score = check_idea(idea_good)
    assert score == 4

def test_idea_bila_mostafid_marfouda():
    # فكرة بلا مستفيد محدد - خاصها تترفض
    idea = "مشروع كيعاون الناس يحلو المشكل ديالهم بتجربة صغيرة مختلفة"
    score = check_idea(idea)
    assert score < 4
