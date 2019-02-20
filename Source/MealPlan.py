#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:22:24 2019

@author: Lemiltock
Follows PEP8
"""


def ChooseMeal(Type):
    '''
    Type: Str - [Bfast, Snack, Lunch, Dinner]
    Returns a random meal ID from DB
    '''
    return None


def NutCalc(UID, MealList):
    '''
    UID: int - UserID
    MealList: List of list for each day
        eg [[day1, Bfast, Snack, Lunch, Dinner]]
    Returns List of list for each day (serve sizes)
        eg [[day1, 80, 110, 75, 85]]
    >>> #Test here#
    '''
    return None


def Upload(MealList, NutList):
    '''
    MealList: List of list for each day
        eg [[day1, Bfast, Snack, Lunch, Dinner]]
    NutList: List of list for each day (serve sizes)
        eg [[day1, 80, 110, 75, 85]]
    Returns confirmation of DB upload and Commit
    '''
    return None


def ShopList(MealList, NutList, ShopAhead):
    '''
    MealList: List of list for each day
        eg [[day1, Bfast, Snack, Lunch, Dinner]]
    NutList: List of list for each day (serve sizes)
        eg [[day1, 80, 110, 75, 85]]
    ShopAhead: Int, number of days to shop ahead for
    Confirms Meal list uploaded before creating List
    Returns confirmation of DB upload and List
    '''
    return None


def MealGen(Start, End, Repeat, D2L, Users):
    '''
    Start: Str - start date for generation (inclusive)
    End: Str - end date for generation (inclusive)
    Repeat: Dict of Bools - if meals are ok to be repeated
        eg {Bfast: True, Snack: True, Lunch: False, Dinner: False}
    D2L: Bool - Dinner to Lunch, set as  True if Dinners will be kept for lunch
    Returns Meal list, Shopping list and recepies
    '''
    return None
