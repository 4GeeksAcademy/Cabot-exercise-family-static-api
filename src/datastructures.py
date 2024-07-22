
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {    
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3],
                "id": self._generateId(),
            },    
            {    
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "id": self._generateId(),
            },    
            {    
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1],
                "id": self._generateId(),
            },    
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 100)

    def add_member(self, member):
        #post
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
            else:
                return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
            #in our get_member functions accepts the variable id. 
            #there is a for loop that searches for each member in the self._members array/list
            #then using the id we passed we are going to check if the member's id matches the id we passed
            #then return that entire member's information, not just their id#


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
