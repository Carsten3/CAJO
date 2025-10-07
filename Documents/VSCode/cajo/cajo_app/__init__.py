from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cajo_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class Introduction(Page):
    pass
    
class PreferenceElicitation(Page):
    pass

class GroupDistribution(Page):
    pass

class GroupInteraction(Page):
    pass

class GroupDecision(Page):
    pass

class Survey(Page):
    pass


page_sequence = [Introduction, PreferenceElicitation, GroupDistribution, GroupInteraction, GroupDecision, Survey]
