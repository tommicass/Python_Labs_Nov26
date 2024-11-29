
import basic

def test_add():
    assert basic.add(4, 3) == 7, "Error should be 7"
    assert basic.add(4, 3, 2) == 9, "Error should be 9"
    return None

def test_mul():
    assert basic.mul(4, 3) == 13, "Error should be 13"
    assert basic.mul(4, 3, 2) == 24, "Error should be 24"
    return None

def test_div():
    assert basic.div(4, 3) == 1.334, "Error should be 1.334"
    return None

def main():
    print("Starting Unit Tests...")
    test_add()
    test_mul()
    test_div()
    print("Unit Tests Successful")
    return None

if __name__ == "__main__":
    main()