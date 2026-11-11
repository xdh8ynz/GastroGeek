import unittest

from core.utility import preprocessing


class UtilityTestCase(unittest.TestCase):
    def test_preprocessing_md(self):
        expected_content = "something_text"

        content = """
        ```md
            something_text
        ```
        """

        self.assertEqual(preprocessing(content), expected_content)

    def test_preprocessing_json(self):
        expected_content = "something_text"

        content = """
                ```json
                    something_text
                ```
                """

        self.assertEqual(preprocessing(content), expected_content)

    def test_preprocessing_backticks(self):
        expected_content = "something_text"

        content = """
        ```
        something_text
        ```
        """

        self.assertEqual(preprocessing(content), expected_content)


if __name__ == "__main__":
    unittest.main()
