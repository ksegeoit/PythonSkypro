from Address import Address
from Mailing import Mailing

from_address = Address("129327", "Moscow", "Menginskogo", 23, 318)
to_address = Address("628181", "Nuagan", "Oblyotova", 38, 12)

mail_to = Mailing(to_address, from_address, 666, str(1000666666110))

print(mail_to)