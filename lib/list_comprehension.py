#!/usr/bin/env python3

def return_evens(num_list):
    n_list=[ num for num in num_list if num%2==0 ]
    return n_list


def make_exclamation(sentence_list):
    s_list=[word + "!" for word in sentence_list]
    return s_list