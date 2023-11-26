import re


def check_zip_code (text):
    return bool(re.search(r" (\b\d{5}(?!-)\b)| (\b\d{5}-\d{4}\b)", text))


assert check_zip_code("The zip codes for New York are 10001 thru 11104.") is True
assert check_zip_code("90210 is a TV show") is False
assert check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.") is True
assert check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.") is False

assert check_zip_code("x\n90201") is False
assert check_zip_code("the zip somewhere is 98230-0000") is True
assert check_zip_code("the zip somewhere else is not 98230-00000000") is False

