
import requests

GEMINI_KEY = "حط_المفتاح_هنا"

MODELS = ["gemini-3.5-flash-lite", "gemini-3.8-flash", "gemini-flash-latest"]

def ask_llm_real(code, failures):
    prompt = f"Fix this Python code. Return only code.\n{code}\nFailures: {failures}"
    headers = {"x-goog-api-key": GEMINI_KEY, "Content-Type": "application/json"}
    for model in MODELS:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
            r = requests.post(url, headers=headers, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
            data = r.json()
            if "error" in data:
                continue
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return text.replace("```python", "").replace("```", "").strip(), f"Gemini صلح الكود بـ {model}"
        except:
            continue
    return code, "كل الموديلات فشلو"

ask_llm_to_fix = ask_llm_real

def agent_fix(code, func_name):
    import io, contextlib
    for attempt in range(1, 4):
        print(f"\n--- محاولة {attempt}/3 ---")
        # هنا كيجرب 3 Tests ديالك
        tests = [(5, 3, 8), ("a", "a", "error"), (0, 0, 0)]
        passed = 0
        failures = ""
        for a, b, expected in tests:
            try:
                ns = {}
                exec(code, ns)
                res = ns[func_name](a, b)
                if res == expected or (expected == "error" and False):
                    passed += 1
                else:
                    failures += f"add({a},{b}) = {res}, expected {expected}\n"
            except Exception as e:
                if expected == "error":
                    passed += 1
                else:
                    failures += f"add({a},{b}) error: {e}\n"
        print(f"نجحو {passed}/3")
        if passed == 3:
            print("🎉 مجرب ✅")
            return code, "نجح"
        code, msg = ask_llm_to_fix(code, failures)
        print(f"🔧 الإصلاح: {msg}")
    return code, "فشل"

if __name__ == "__main__":
    broken = "def add(a, b):\n    return a * b"
    fixed, _ = agent_fix(broken, "add")
    print("\n--- الكود النهائي ---")
    print(fixed)
