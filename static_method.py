class TestStaticMethod:
    @staticmethod
    def test_method(self):
        return self.upper()

print(TestStaticMethod.test_method('Username'))
