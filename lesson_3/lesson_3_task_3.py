from  address import Address
from mailing import Mailing

to_address = Address(123456, "москва", "Приморская", 1, 45)
from_address = Address(4638356, "Мга", "Ленина", 7, 56)
cost = 1987
track = 132345677

my_mailing = Mailing(track, to_address, from_address, cost)
print(my_mailing)