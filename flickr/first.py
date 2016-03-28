import flickr_api
from pymongo import MongoClient

connection = MongoClient()
database = connection.flickr



key = "aa002510472d4cf5eb72710428014d3b"
secret = "22829bcbe03a185a"

flickr_api.set_keys(key,secret)


user = flickr_api.Person.findByUserName('orestistou')


# with this we get a list of objects with
# the users in them.

contactList = []

users = [user]
tempUsers = []
usersTable = database.users

index = 0
for i in range(3):
    for tempUser in users:
        for contact in tempUser.getPublicContacts():
            tempUsers.append(contact)
            contactList.append(contact.get("id"))
        person = {"id" : user.get('id'),"contacts" : contactList}
        index += 1
        print index
        usersTable.insert(person)
    users = tempUsers
    tempUsers = []







# favorites = user.getFavorites()


#
# print contacts
#
# print favorites

#
# info = contacts[1].getInfo()


# check the context of the first friend favorites
# first = contacts[0]
#
# print first


#
# for i in info:
#     print i

# for contact in contacts:
#     temp = contact.getPublicContacts()
#     contactsOfcontacts += temp
#
#
# for person in contactsOfcontacts:
#     info = person.getInfo()
#     if 'location' in info:
#         print info['location']
