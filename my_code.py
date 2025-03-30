import pytest

def fix_phone_num(phone_num_to_fix):
  # given "5125558823". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:3] # 512 (first three digits)
  three_part = phone_num_to_fix[3:6] # 555 (next three digits)
  four_part = phone_num_to_fix[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
    assert fix_phone_num("555-442-9876") == "5554429876"
    assert fix_phone_num("(321) 654-3333") == "3216543333"
    assert fix_phone_num("5554429876") == "5554429876"
    assert fix_phone_num("3216543333") == "3216543333"

def test_fix_phone_num_rejects_invalid_length():
    fix_phone_num("555-442-98761")
    fix_phone_num("(321) 654 3333")
