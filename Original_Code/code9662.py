class ExtendedStack(list):

    def __checkValidForExtensionOperations(self):
        if len(self) >= 2:
            return True
        return False

    def sum(self):
        if self.__checkValidForExtensionOperations():
            elem1 = self.pop()
            elem2 = self.pop()
            res = elem1 + elem2
            self.append(res)

    def sub(self):
        if self.__checkValidForExtensionOperations():
            elem1 = self.pop()
            elem2 = self.pop()
            res = elem1 - elem2
            self.append(res)

    def mul(self):
        if self.__checkValidForExtensionOperations():
            elem1 = self.pop()
            elem2 = self.pop()
            res = elem1 * elem2
            self.append(res)

    def div(self):
        if self.__checkValidForExtensionOperations():
            elem1 = self.pop()
            elem2 = self.pop()
            res = elem1 // elem2
            self.append(res) 