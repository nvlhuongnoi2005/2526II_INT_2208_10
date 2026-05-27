import unittest

from loan_approval import decide_loan


class TestLoanApproval(unittest.TestCase):
    TEST_CASES = [
        ("TC_01", 17, 20.0, 701, "C", "Invalid Input"),
        ("TC_02", 66, 20.0, 701, "C", "Invalid Input"),
        ("TC_03", 18, 4.9, 701, "C", "Invalid Input"),
        ("TC_04", 18, 500.1, 701, "C", "Invalid Input"),
        ("TC_05", 18, 20.0, 299, "C", "Invalid Input"),
        ("TC_06", 18, 20.0, 851, "C", "Invalid Input"),
        ("TC_07", 18, 20.0, 700, "X", "Invalid Input"),
        ("TC_08", 18, 20.0, 500, "C", "REJECT"),
        ("TC_09", 30, 14.9, 701, "C", "MANUAL REVIEW"),
        ("TC_10", 30, 14.9, 701, "F", "REJECT"),
        ("TC_11", 30, 14.9, 501, "C", "REJECT"),
        ("TC_12", 65, 15.0, 701, "C", "APPROVE"),
        ("TC_13", 65, 15.0, 701, "F", "MANUAL REVIEW"),
        ("TC_14", 30, 20.0, 700, "C", "APPROVE"),
        ("TC_15", 30, 20.0, 700, "F", "MANUAL REVIEW"),
    ]

    def test_loan_approval_cases(self):
        for case_id, age, income, credit_score, employment, expected in self.TEST_CASES:
            with self.subTest(case_id=case_id):
                self.assertEqual(decide_loan(age, income, credit_score, employment), expected)


if __name__ == "__main__":
    unittest.main()