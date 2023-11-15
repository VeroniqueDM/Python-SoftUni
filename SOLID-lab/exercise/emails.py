from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self,  text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMLContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])

class EncryptedContent(IContent):
    def format(self):
        res = ''
        for let in self.text:
            res += chr(ord(let) + 5)
        return res
class MaskedContent(IContent):
    def format(self):
        return '*' * len(self.text)

class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
            self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content.format())


email = Email('IM', 'MyML')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(EncryptedContent('Hello, there'))
print(email)
email.set_content(MyMLContent('Hello, there'))
print(email)
email.set_content(MaskedContent('Hello, there'))
print(email)

