import pytest

def fix_phone_num(phone_num_to_fix):
    # Remove non-digit characters
    cleaned = ''.join(c for c in phone_num_to_fix if c.isdigit())

    # Validate length
    if len(cleaned) != 10:
        raise ValueError("Can only format numbers that are exactly 10 digits long")

    area_code = cleaned[0:3]
    three_part = cleaned[3:6]
    four_part = cleaned[6:]
    
    fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
    return fixed_num

def test_fix_phone_num():
    assert fix_phone_num("5125558823") == '(512) 555 8823'
    
    # Invalid too short
    with pytest.raises(ValueError):
        fix_phone_num("51")
