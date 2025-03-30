import pytest

def fix_phone_num(phone_num_to_fix):
    # Remove non-digit characters
    cleaned = ''.join(c for c in phone_num_to_fix if c.isdigit())

    # Check if it's exactly 10 digits
    if len(cleaned) != 10:
        raise ValueError("Phone number must contain exactly 10 digits")

    area_code = cleaned[0:3]
    three_part = cleaned[3:6]
    four_part = cleaned[6:]

    fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
    return fixed_num

def test_fix_phone_num():
    assert fix_phone_num("555-442-9876") == "(555) 442 9876"
    assert fix_phone_num("(321) 654-3333") == "(321) 654 3333"
    assert fix_phone_num("5554429876") == "(555) 442 9876"
    assert fix_phone_num("3216543333") == "(321) 654 3333"

def test_fix_phone_num_rejects_invalid_length():
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")
    with pytest.raises(ValueError):
        fix_phone_num("(321) 654 3333 123")

def test_valueerror_on_nondigits():
    with pytest.raises(ValueError):
        fix_phone_num("abc-def-ghij")
