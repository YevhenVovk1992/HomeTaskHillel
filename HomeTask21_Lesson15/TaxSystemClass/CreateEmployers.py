import abc


class Employer(abc.ABC):
    """
        Create an abstract parent class for employers.
        It take the name of the employer, income, expenses.
        Method 'report' create the tuple with income, expenses.
        Method 'calculate_EP' is abstract. It will use for calculation in the group
    """
    def __init__(self, name, company_turnover, expenses) -> None:
        self.name = name
        self.company_turnover = company_turnover
        self.expenses = expenses

    def report(self) -> tuple:
        return self.company_turnover, self.expenses

    @abc.abstractmethod
    def calculate_EP(self) -> None:
        pass

    def __str__(self) -> str:
        return f'FOP {self.name}'


class EmployerGroup1(Employer):
    """
        Group 1 has the tax 10% of the living wage. So it doesn't change.
        And only social contribution.
    """
    INCOME_LIMIT = 1000000
    ECB = 1430
    EP = 227

    def __init__(self, name, company_turnover, expenses, group) -> None:
        super().__init__(name, company_turnover, expenses)
        self.group = group

    def calculate_EP(self) -> int:
        return self.EP


class EmployerGroup2(Employer):
    """
        Group 2 has the tax 20% of the minimal salary. So it doesn't change.
        And only social contribution.
    """
    INCOME_LIMIT = 5000000
    ECB = 1430
    EP = 1200

    def __init__(self, name, company_turnover, expenses, group) -> None:
        super().__init__(name, company_turnover, expenses)
        self.group = group

    def calculate_EP(self) -> int:
        return self.EP


class EmployerGroup3(Employer):
    """
        Group 3 has the tax 5% of the amount of income.
        And only social contribution.
    """
    INCOME_LIMIT = 7000000
    ECB = 1430
    EP = 0.05

    def __init__(self, name, company_turnover, expenses, group) -> None:
        super().__init__(name, company_turnover, expenses)
        self.group = group

    def calculate_EP(self) -> int:
        return self.report()[0] * self.EP
