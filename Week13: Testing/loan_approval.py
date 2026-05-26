"""Loan approval decision module for CS2045."""

from numbers import Real


def _risk_level(credit_score):
    if 300 <= credit_score <= 500:
        return "High"
    if 501 <= credit_score <= 700:
        return "Medium"
    return "Low"


def decide_loan(age, income, credit_score, employment):
    """Return the loan decision for a personal loan application."""

    if not isinstance(age, int) or isinstance(age, bool) or age < 18 or age > 65:
        return "Invalid Input"

    if not isinstance(income, Real) or isinstance(income, bool):
        return "Invalid Input"

    income = round(float(income), 1)
    if income < 5.0 or income > 500.0:
        return "Invalid Input"

    if not isinstance(credit_score, int) or isinstance(credit_score, bool) or credit_score < 300 or credit_score > 850:
        return "Invalid Input"

    if employment not in {"C", "F"}:
        return "Invalid Input"

    risk = _risk_level(credit_score)

    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"
        return "REJECT"

    if employment == "C":
        return "APPROVE"

    return "MANUAL REVIEW"