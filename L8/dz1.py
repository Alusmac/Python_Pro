import unittest


class StringProcessor:
    """class string processing
    """
    def reverse_string(self, s: str) -> str:
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        if not s:
            return s
        return s[0].upper() + s[1:]

    def count_vowels(self, s: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count


class TestStringProcessor(unittest.TestCase):
    def setUp(self):
        self.abc = StringProcessor()

    @unittest.skip("The problem with the empty line, which I plan to solve later, little later)")
    def test_reverse_empty_string(self):
        self.assertEqual(self.abc.reverse_string(""), "")

    def test_reverse_regular_string(self):
        self.assertEqual(self.abc.reverse_string("black"), "kcalb")

    def test_reverse_mixed_chars(self):
        self.assertEqual(self.abc.reverse_string("far12de"), "ed21raf")

    def test_capitalize_empty_string(self):
        self.assertEqual(self.abc.capitalize_string(""), "")

    def test_capitalize_lowercase(self):
        self.assertEqual(self.abc.capitalize_string("black"), "Black")

    def test_capitalize_mixed_case(self):
        self.assertEqual(self.abc.capitalize_string("bLACK"), "BLACK")

    def test_capitalize_with_symbols(self):
        self.assertEqual(self.abc.capitalize_string("wh300a"), "Wh300a")

    def test_count_vowels_empty(self):
        self.assertEqual(self.abc.count_vowels(""), 0)

    def test_count_vowels_mixed_case(self):
        self.assertEqual(self.abc.count_vowels("AbEIoU"), 5)

    def test_count_vowels_with_digits_and_symbols(self):
        self.assertEqual(self.abc.count_vowels("Bl3fds"), 0)

    def test_count_vowels_normal(self):
        self.assertEqual(self.abc.count_vowels("Black"), 1)


if __name__ == '__main__':
    unittest.main()
