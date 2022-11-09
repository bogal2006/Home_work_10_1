from funsymbol import amountchar as am
def test(string_test: str):
    a = am(string_test)
    test_a = len(string_test.strip())
    assert a == test_a


test('test')
test('super')
test('1234567')
test('123456789')






