class Loan:
    def __init__(self, sum_credit, rate_yearly, months):
        self.s = sum_credit
        self.r = rate_yearly / 12 / 100  # місячна ставка
        self.m = months

    def overpayment(self):
        raise NotImplementedError


class AnnuityLoan(Loan):
    def overpayment(self):
        # Формула ануїтету
        if self.r == 0:
            return 0
        k = (self.r * (1 + self.r) ** self.m) / ((1 + self.r) ** self.m - 1)
        monthly_pay = self.s * k
        total_pay = monthly_pay * self.m
        return total_pay - self.s


class DifferentiatedLoan(Loan):
    def overpayment(self):
        # Диференційований платіж
        total_pay = 0
        rem_sum = self.s
        base_pay = self.s / self.m

        for _ in range(self.m):
            interest = rem_sum * self.r
            total_pay += base_pay + interest
            rem_sum -= base_pay

        return total_pay - self.s


# Приклад використання
if __name__ == "__main__":
    sum_cr = 100000
    rate = 12
    term = 12

    annuity = AnnuityLoan(sum_cr, rate, term)
    diff = DifferentiatedLoan(sum_cr, rate, term)

    print(f"Ануїтет переплата: {annuity.overpayment():.2f}")
    print(f"Диференц. переплата: {diff.overpayment():.2f}")
    