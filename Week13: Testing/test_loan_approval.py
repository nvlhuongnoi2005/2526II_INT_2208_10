import unittest

from loan_approval import decide_loan


class TestLoanApproval(unittest.TestCase):
    def test_invalid_age_below_lower_bound(self):
        self.assertEqual(decide_loan(17, 20.0, 701, "C"), "Invalid Input")

    def test_invalid_age_above_upper_bound(self):
        self.assertEqual(decide_loan(66, 20.0, 701, "C"), "Invalid Input")

    def test_invalid_income_below_lower_bound(self):
        self.assertEqual(decide_loan(18, 4.9, 701, "C"), "Invalid Input")

    def test_invalid_income_above_upper_bound(self):
        self.assertEqual(decide_loan(18, 500.1, 701, "C"), "Invalid Input")

    def test_invalid_credit_score_below_lower_bound(self):
        self.assertEqual(decide_loan(18, 20.0, 299, "C"), "Invalid Input")

    def test_invalid_credit_score_above_upper_bound(self):
        self.assertEqual(decide_loan(18, 20.0, 851, "C"), "Invalid Input")

    def test_invalid_employment(self):
        self.assertEqual(decide_loan(18, 20.0, 700, "X"), "Invalid Input")

    def test_high_risk_always_reject(self):
        self.assertEqual(decide_loan(18, 20.0, 500, "C"), "REJECT")

    def test_low_income_low_risk_contract_manual_review(self):
        self.assertEqual(decide_loan(30, 14.9, 701, "C"), "MANUAL REVIEW")

    def test_low_income_low_risk_freelance_reject(self):
        self.assertEqual(decide_loan(30, 14.9, 701, "F"), "REJECT")

    def test_low_income_medium_risk_contract_reject(self):
        self.assertEqual(decide_loan(30, 14.9, 501, "C"), "REJECT")

    def test_high_income_low_risk_contract_approve(self):
        self.assertEqual(decide_loan(65, 15.0, 701, "C"), "APPROVE")

    def test_high_income_low_risk_freelance_manual_review(self):
        self.assertEqual(decide_loan(65, 15.0, 701, "F"), "MANUAL REVIEW")

    def test_high_income_medium_risk_contract_approve(self):
        self.assertEqual(decide_loan(30, 20.0, 700, "C"), "APPROVE")

    def test_high_income_medium_risk_freelance_manual_review(self):
        self.assertEqual(decide_loan(30, 20.0, 700, "F"), "MANUAL REVIEW")


if __name__ == "__main__":
    unittest.main()