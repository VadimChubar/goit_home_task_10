from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):

    # def add_contact(self, name: Name, phone: Phone = None):
    #     contact = Record(name=name, phone=phone)
    #     self.data[name.value] = contact

    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    # def find_by_name(self, name):
    #     try:
    #         return self.data[name]
    #     except KeyError:
    #         return None
    #
    # def find_by_phone(self, phone: str):
    #     for record in self.data.values():  # type: Record
    #         if phone in [number.value for number in record.phones]:
    #             return record
    #     return None


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, old_number: Phone, new_nuber: Phone):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_nuber)
        except ValueError:
            return f"{old_number} does not exists"

    def delete_phone(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"{phone} does not exists"

# book = AddressBook()
# new_record = Record(name=Name(value="Bill"))
# new_record.add_phone("380670000000")
# new_record.add_phone("380671111111")
# print(new_record.phones)
# print(new_record.name)
# book.add_record(new_record)
# print(book.data)

