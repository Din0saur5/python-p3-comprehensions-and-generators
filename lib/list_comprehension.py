#!/usr/bin/env python3

def return_evens(num_list):
    evens = [item for item in num_list if item%2==0]
    return evens

def make_exclamation(sentence_list):
   excl = [f'{item}!' for item in sentence_list]
   return excl