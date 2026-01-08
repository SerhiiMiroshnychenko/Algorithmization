class Loan:
    def __init__(self, sum_credit, rate_yearly, term_months):
        self.sum = sum_credit
        self.rate = (rate_yearly / 12) / 100
        self.months = term_months

    def calculate_overpayment(self):
        raise NotImplementedError


class AnnuityLoan(Loan):
    def calculate_overpayment(self):
        if self.rate == 0:
            return 0
        a = (1 + self.rate) ** self.months
        k = (self.rate * a) / (a - 1)
        monthly_pay = self.sum * k
        return monthly_pay * self.months - self.sum


class DifferentiatedLoan(Loan):
    def calculate_overpayment(self):
        total_pay = 0
        rem_sum = self.sum
        base_pay = self.sum / self.months

        for _ in range(self.months):
            interest = rem_sum * self.rate
            total_pay += base_pay + interest
            rem_sum -= base_pay

        return total_pay - self.sum


if __name__ == "__main__":
    for credit in (credit_type(100_000, 12, 12) for credit_type in (AnnuityLoan, DifferentiatedLoan)):
        print(f'Переплата для {type(credit)}: {credit.calculate_overpayment():.2f}')
