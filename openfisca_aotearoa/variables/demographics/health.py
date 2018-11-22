# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class is_of_full_capacity(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "is of full capacity (a person shall be deemed to be of full capacity if he is not of unsound mind)"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443689.html#DLM443689"