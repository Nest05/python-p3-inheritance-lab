#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    def learn(self, knowledge):
        new_knowledge = self.knowledge.insert(0, knowledge)
        return new_knowledge
       