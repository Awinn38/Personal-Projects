class TestClass:
    def test_one():
        x = "edureka"
        assert 'r' in x
        return print(x)

    def test_two():
        x = 'hello'
        assert hasattr(x,'check')

# def student(firstname,lastname = 'Mark', standard = 'Fifth'):
    
#     print(firstname,lastname,'studies in',standard,'Standard')

# Antonio = 'Antonio'
# student(Antonio)

TestClass.test_one()