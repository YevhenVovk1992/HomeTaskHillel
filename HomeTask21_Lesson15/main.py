"""
    Создать класс "налоговой системы", у которой будет метод, что принимает набор предпринимателей и
    для каждого выводит сумму налогов, которую он должен заплатить за 1 квартал.
    Так же тут нужны будут классы предпринимателей, которые могут отличаться в зависимости от группы ФОП,
    которую они выберут:
        https://diia.gov.ua/tax-systems/1-grupa
        https://diia.gov.ua/tax-systems/2-grupa
        https://diia.gov.ua/tax-systems/3-grupa
        Если что, ЕСВ (единый социальный взнос) сейчас - 1430 грн.
        (если что - реализуйте только формулу по налогам и лимиты, не изучайте все нюансы этих групп)
    У предпринимателя должен быть метод "подать отчетность", который будет сохранять как атрибуты 2 суммы -
    оборот и расходы по бизнесу. Потом пригодятся в подсчете налогов.
    Продумайте еще что делать, если оборот предпринимателя превысил допустимый лимит.
    Остальные атрибуты и методы - на усмотрение. Подумайте, где пропишете логику подсчета налогов для каждой группы :)
    В конце надо создать N ФОПов, подать отчетность за них, и передать их всех на подсчет налогов.
"""
from TaxSystemClass.CreateEmployers import EmployerGroup1, EmployerGroup2, EmployerGroup3
from TaxSystemClass.Tax import TaxSystem
from TaxSystemClass.EmployerGroups import Group


# Create N employers
FOP_Valet = EmployerGroup1('Valet', 250000, 50000, Group.GROUP1)
FOP_Garage = EmployerGroup1('Garage', 300000, 45000, Group.GROUP1)
FOP_Sale_out_home = EmployerGroup2('Antonio', 650000, 600000, Group.GROUP2)
FOP_Alex = EmployerGroup2('Alex', 600000, 20000, Group.GROUP2)
FOP_Maximus = EmployerGroup3('Maxim', 2500000, 500000, Group.GROUP3)

# Create a tax office
Tax_Servise = TaxSystem()

# Submit reports for employers
print(Tax_Servise.calculate_taxes(
    FOP_Valet, FOP_Garage, FOP_Sale_out_home, FOP_Alex, FOP_Maximus
))
print('_______________________________________')

# Calculate the tax if the limit is exceeded
FOP_Garage.company_turnover = 1100000
FOP_Maximus.company_turnover = 7500000
print(Tax_Servise.calculate_taxes(FOP_Garage, FOP_Maximus))

# Check for changes to objects of the class "Employer"
print(FOP_Garage.__dict__)
print(FOP_Maximus.__dict__)
