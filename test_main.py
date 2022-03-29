import main
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("num1,output", [(10, False),(7, True)])
def test_CheckPrimeOrNot(num1,output):
    result=main.CheckPrimeOrNot(num1)
    assert result ==output

@pytest.mark.xfail
@pytest.mark.parametrize("num1,output", [(102, False),(101, True)])
def test_CheckPalindromeOrNot(num1,output):
    result=main.CheckPalindromeOrNot(num1)
    assert result ==output