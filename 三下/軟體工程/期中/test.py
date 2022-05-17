import ktv
def test_2p():
    i=2
    result=ktv.people(i)
    result2=ktv.box(i)
    if result > result2:
        print(f"人數{i}位以包廂算比較便宜")
    else:
        print(f"人數{i}位以人數算比較便宜")
    assert result<result2
def test_3p():
    i=3
    result=ktv.people(i)
    result2=ktv.box(i)
    if result > result2:
        print(f"人數{i}位以包廂算比較便宜")
    else:
        print(f"人數{i}位以人數算比較便宜")
    assert result > result2

def test_4p():
    i=4
    result=ktv.people(i)
    result2=ktv.box(i)
    if result > result2:
        print(f"人數{i}位以包廂算比較便宜")
    else:
        print(f"人數{i}位以人數算比較便宜")
    assert result > result2

def test_5b():
    b=5
    result2 = ktv.box(b)
    result = ktv.people(b)
    if result > result2:
        print(f"人數{b}位以包廂算比較便宜")
    else:
        print(f"人數{b}位以人數算比較便宜")
    assert result > result2
def test_8b():
    b=8
    result2 = ktv.box(b)
    result = ktv.people(b)
    if result > result2:
        print(f"人數{b}位以包廂算比較便宜")
    else:
        print(f"人數{b}位以人數算比較便宜")
    assert result > result2

def test_12b():
    b=12
    result2 = ktv.box(b)
    result = ktv.people(b)
    if result > result2:
        print(f"人數{b}位以包廂算比較便宜")
    else:
        print(f"人數{b}位以人數算比較便宜")
    assert result > result2

def test_15b():
    b=15
    result2 = ktv.box(b)
    result = ktv.people(b)
    if result > result2:
        print(f"人數{b}位以包廂算比較便宜")
    else:
        print(f"人數{b}位以人數算比較便宜")
    assert result > result2

def test_20b():
    b=20
    result2 = ktv.box(b)
    result = ktv.people(b)
    if result > result2:
        print(f"人數{b}位以包廂算比較便宜")
    else:
        print(f"人數{b}位以人數算比較便宜")
    assert result > result2
if __name__ == '__main__':
    test_2p()
    test_3p()
    test_4p()
    test_5b()
    test_8b()
    test_12b()
    test_15b()
    test_20b()