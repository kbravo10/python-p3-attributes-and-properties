#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = None, job = None):
        if(name != None):
            if(type(name) == str and 1 < len(name) < 25):
                name.upper()
                self._name = name.title()
            else:
                print("Name must be string between 1 and 25 characters.")
        if(job != None):
            located = False
            for jobs in APPROVED_JOBS:
                if(jobs == job):
                    located = True
                    self._job = job
            if(located != True):
                print("Job must be in list of approved jobs.")

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job

    name = property(get_name, __init__)
    job = property(get_job, __init__)
