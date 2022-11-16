#! /usr/bin/python3
# -*- coding: utf-8 -*-

# 2020年1月4日，学习《Python3 面向对象编程》


class Contact:
    # 这种定义，使all_contacts成为一个静态成员
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send ",
              "'{}' order to '{}'".format(order, self.name))


c = Contact("Some body", "somebody@example.net")
s = Supplier("Some body", "somebody@example.net")
s.order("I need pliers")
c.order("I need pliers")

s = [each[0] for each in c.all_contacts]

# 扩展内置对象


# 继承自list
class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


# 删除前一个类
del Contact


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jehna C", "jehna@example.net")
[c.name for c in Contact.all_contacts.search('John')]

Contact.all_contacts.search('John')


class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 1
longkeys['hello2'] = 'word'
longkeys.longest_key()


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


c = Friend("zz", "zz@example.net", "1234")
[i.email for i in c.all_contacts]


class MailSender():
    def send_mail(self, message):
        print("Sending mail to " + self.email)


class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("John Smith", "jsmith@example.net")
e.send_mail("Hello, test e-mail here")

dir(list)
help(list.__add__)