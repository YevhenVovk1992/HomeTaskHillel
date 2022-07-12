from TaxSystemClass.EmployerGroups import Group


class TaxSystem:
    """
        Class 'TaxSystem' accepts employers and output tax amount.
        '_mapping' - logic to replace the group when the limit is exceeded.
    """
    _mapping = {Group.GROUP1: Group.GROUP2, Group.GROUP2: Group.GROUP3, Group.GROUP3: Group.GROUP3}

    def _exceeded_limit(self, employer) -> bool:
        if employer.report()[0] > employer.INCOME_LIMIT:
            return True
        else:
            return False

    def calculate_taxes(self, *employers) -> dict:
        _fine = 0
        rezult = {}
        for employer in employers:
            if self._exceeded_limit(employer):
                if employer.group is Group.GROUP3:
                    _fine = employer.report()[0] - employer.INCOME_LIMIT
                employer.group = self._mapping[employer.group]
            tax = employer.calculate_EP() + employer.ECB + _fine*0.15
            rezult[employer.name] = tax
        return rezult
