class Phonebook():
    def __init__(self):
        self._database = [""not found"" for i in range(10 ** 7)]
    def add(self, phone, name):
        self._database[phone] = name
    def find(self, phone):
        print(self._database[phone])
    def delete(self, phone):
        self._database[phone] = ""not found""

def handler(phonebook, stream):
    for command in stream:
        if command.startswith(""add""):
            _, phone, name = command.split()
            phonebook.add(int(phone), name)
        else:
            _, phone = command.split()
            if command.startswith(""find""):
                phonebook.find(int(phone))
            else:
                phonebook.delete(int(phone))

if __name__ == ""__main__"":
    phonebook = Phonebook()
    count = int(input())
    handler(phonebook, [input() for i in range(count)])
 