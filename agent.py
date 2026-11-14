def clean_price(value):
    """كنظف الثمن وكنرجعو float. كيرفض أي حاجة ما مفهوماش."""
    if isinstance(value, (int, float)):
        price = float(value)
    elif isinstance(value, str):
        s = value.strip().upper()
        # تنظيف Muse Spark - كيفهم كل العملات ديال المغرب
        for token in ["DH", "MAD", "درهم", "د.م", "DHS"]:
            s = s.replace(token, "")
        s = s.strip().replace(" ", "").replace(",", ".")
        if s == "":
            raise ValueError(f"ثمن خاوي: {value!r}")
        try:
            price = float(s)
        except ValueError:
            raise ValueError(f"ثمن ما مفهومش: {value!r}")
    else:
        raise ValueError(f"نوع الثمن ما مدعومش: {type(value).__name__} - {value!r}")
    if price < 0:
        raise ValueError(f"ثمن سالب مرفوض: {value!r}")
    return price

def calculate_invoice(prices, discount_percent=10):
    """كتحسب الفاتورة النهائية. كترجع float مقرب لـ 2 أرقام."""
    if not prices:
        raise ValueError("اللائحة خاوية: ما يمكنش نحسبو فاتورة بلا أثمنة.")
    if not isinstance(discount_percent, (int, float)):
        raise ValueError(f"التخفيض خاصو يكون رقم: {discount_percent!r}")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"التخفيض مرفوض: {discount_percent}% - خاصو يكون بين 0 و 100.")
    total = 0.0
    for p in prices:
        total += clean_price(p)  # ماشي sum()، كنظفو واحد بواحد
    final = total * (1 - discount_percent / 100)
    return round(final, 2)
