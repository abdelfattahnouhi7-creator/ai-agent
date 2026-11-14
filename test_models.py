from agent_models import check_model_answer

def test_gemini_marfoud():
    # جواب Gemini الحقيقي - رجع string
    answer = "return 'اللائحة خاوية' - no tests"
    assert check_model_answer(answer) < 4

def test_claude_maqbol():
    answer = """
    def clean_price(): replace strip
    if not prices: raise ValueError('خاوية')
    if remise > 100: raise ValueError
    test_normal assert 315.45 pytest
    """
    assert check_model_answer(answer) == 4
