class Employee:
    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._worked_normal_hours = 0
        self._worked_overhours = 0

    def register_time(self, hours):
        if hours > 8:
            self._worked_normal_hours += 8
            self._worked_overhours += hours - 8
        else:
            self._worked_normal_hours += hours

    def pay_salary(self):
        to_pay = (
                self._worked_normal_hours * self.rate_per_hour +
                self._worked_overhours * 2 * self.rate_per_hour
        )
        self._worked_normal_hours = 0
        self._worked_overhours = 0
        return to_pay


class TestEmployee:

    def test_init(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        assert employee.first_name == "Jan"
        assert employee.last_name == "Nowak"
        assert employee.rate_per_hour == 100.0

    def test_register_time(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee._worked_normal_hours == 5

    def test_pay_salary_when_no_worked_hours(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        assert employee.pay_salary() == 0

    def test_pay_salary_with_worked_hours(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 5 * 100
        assert employee.pay_salary() == 0

    def test_pay_salary_overhours(self):
        employee = Employee('Jan', 'Nowak', 50)
        employee.register_time(10)
        assert employee.pay_salary() == 8 * 50 + 2 * 2 * 50
        assert employee.pay_salary() == 0

    def test_pay_salary_many_days(self):
        employee = Employee('Jan', 'Nowak', 100)
        employee.register_time(10)
        employee.register_time(10)
        employee.register_time(10)
        assert employee.pay_salary() == 3 * 8 * 100 + 3 * 2 * 200


class PremiumEmployee(Employee):
    def __init__(self, f_name, l_name, rph):
        super().__init__(f_name, l_name, rph)
        self.bonuses = 0

    def give_bonus(self, bonus):
        self.bonuses += bonus

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonuses
        self.bonuses = 0
        return to_pay


class TestPremiumEmployee:
    def test_initialization(self):
        pe = PremiumEmployee("Jan", "Nowak", 100)
        assert pe.first_name == "Jan"
        assert pe.last_name == "Nowak"
        assert pe.rate_per_hour == 100.0

    def test_give_bonus(self):
        pe = PremiumEmployee("Jan", "Nowak", 100)
        assert pe.pay_salary() == 0
        pe.give_bonus(500)
        pe.give_bonus(300)
        assert pe.pay_salary() == 800
        assert pe.pay_salary() == 0

        pe.register_time(5)
        pe.give_bonus(300)
        assert pe.pay_salary() == 800

