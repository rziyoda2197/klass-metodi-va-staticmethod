class MathUtils:
    def oddiy_method(self, a, b):
        return a + b

    @classmethod
    def class_method(cls, a, b):
        return cls().oddiy_method(a, b)

    @staticmethod
    def static_method(a, b):
        return a * b

# Test qilish
math_utils = MathUtils()
print(math_utils.oddiy_method(5, 10))  # 15
print(MathUtils.class_method(5, 10))  # 15
print(MathUtils.static_method(5, 10))  # 50
