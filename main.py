import random

class Project:
    # This class is for simulating various projects with randomised variable combinations
    def __init__(self):
        avg_exp, avg_rating = self.initiate_members()
        client_history = self.initiate_clients()
        print(avg_exp, avg_rating, client_history)
        return


    def initiate_members(self):
        """
        This function is for calculating the average experience and average rating of the team members
        :return: average experience, average rating
        """
        team_exp = 0
        team_rating = 0
        no_of_members = random.randint(4,11)
        for i in range(no_of_members+1):
            add_member = Member()
            team_exp += add_member.member_exp
            team_rating += add_member.member_rating
        avg_exp = team_exp/no_of_members
        avg_rating = team_rating/no_of_members
        return avg_exp, avg_rating

    def initiate_clients(self):
        add_client = Client()
        client_history = add_client.client_history
        return client_history

class Member:
    # Class for simulating team members as various combinations of experience and rating
    def __init__(self):
        self.member_exp = random.randint(0, 21)
        self.member_rating = random.randint(1, 6)
        return

class Client:
    # Class for simulating various client characteristics
    def __init__(self):
        self.client_history = random.randint(0, 2)
        return

Project()