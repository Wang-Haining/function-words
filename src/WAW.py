#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hw56@iu.edu
Created on May 18, 2020.
"""

import re
import json
import nltk
from collections import OrderedDict
from nltk import word_tokenize, regexp_tokenize
from nltk.tokenize import TweetTokenizer

PUNCK_RE = re.compile(r'[^\s\w]+$')


# from nltk.tokenize import sent_tokenize
from nltk.tokenize import TweetTokenizer

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize

from nltk.tokenize.stanford import StanfordTokenizer

from copy import deepcopy



# a=Tokenizer('casual').task_allocator()

# def sent_tokenizer(raw):
#     # prevent a situation that "." as an independent sentence. This is seen at 6ec9c0's profile.
#     # raw = raw.replace(" . . . ", '...')
#     sent_tokens = sent_tokenize(raw)
#     # double check the 0 length sent_token
#     sent_tokens = [sent_token for sent_token in sent_tokens if len(sent_token) != 0]
#     return sent_tokens

class Tokenizer(object):
    """
    Let users choose what tokenizer they would like to use.
    Supported tokenizers are the simple, casual, tweet, and regexp NLTK format tokenzier.
    If reg_exp is specified, use NLTK regexp tokenizer and leave everything for user's consideration (the elimination of
    punctuation included); otherwise, this function will eliminate all the punctuations for the simple, casual, and
    tweet tokenizer.
    By default, we use casual.
    """

    def __init__(self, tokenizer, punct_filter=True, reg_exp=None):
        self.name = tokenizer
        self.reg_exp = reg_exp
        self.punct_filter = punct_filter

    def tokenize(self):
        # misuse check here: whether tokenizer is empty string, or None, or things other than string
        if self.reg_exp is not None:
            pass
        else:
            if self.name == 'casual':
                return casual_tokenizer
            elif self.name == 'simple':
                return simple_tokenizer
            elif self.name == 'tweet':
                return tweet_tokenizer

# regexp_tokenize(s, pattern='\w+|\$[\d\.]+|\S+')


def casual_tokenizer(raw, punct_filter=True):
    word_punct_tokens = nltk.casual_tokenize(raw)
    if punct_filter:
        return punctuation_filter(word_punct_tokens)
    else:
        return word_punct_tokens


def simple_tokenizer(raw):
    word_punct_tokens = nltk.casual_tokenize(raw)


def tweet_tokenizer(raw):
    pass


def punctuation_filter(word_punct_tokens):
    word_tokens = []
    for token in word_punct_tokens:
        if PUNCK_RE.match(token) is None:
            word_tokens.append(token)
    return word_tokens








    # def task_allocator(self):
    #     if self.name == 'casual':
    #         return add1plus2
    #
    # def add1plus1(self):
    #     print(1 + 1)



class WordList(object):
    """
    This Class provides several popular word list for users to check against and offer flexibility for user to input
    word lists to their likings.
    """

    def __init__(self):
        pass


class Raw(object):
    """
    Basically, this is a class to examine whether the input is an English text.
    """

    def __init__(self):
        pass


class Results(object):
    """
    The Results class is used for showing the results.
    Users should get access to
        the total word count(int),
        the aggregate word count for words in the specified wordlist(int),
        the words-against-words count(Counter), and
        the words-against-words ratio(Counter).
    """
    def __init__(self):
        pass


def main(text=None, tokenizer='casual', wordlist=None, to_json=False, to_csv=False, to_dataframe=False, dir='./results'):
    """

    :param raw: a Raw instance
    :param tokenizer: a tokenzier instance
    :param wordlist: a Wordlist instance
    :return: a Results instance
    """
    # raw_input = deepcopy(raw)

    raw = Raw(text)
    tokenizer = Tokenizer(tokenizer)
    wordlist = WordList(wordlist)







def WPS_9_functionWords(self, text):
    """
    Function:
        512 features used in the WPS.
    """
    f_list = json.load(open("koppel_function_words.json"))

    functors = dict.fromkeys(f_list, 0)
    functors = OrderedDict(functors)
    functors_sum = 0
    for key, value in functors.items():
        for word_token in text.word_tokens:
            if word_token.lower() == key:
                functors[key] += 1
                functors_sum += 1
    for key, value in functors.items():
        functors[key] /= functors_sum
    functors_list = [value for value in functors.values()]
    self.wps_14_function_word_pct = functors_list


def D4hm_5_functionWord2word_ratios(self, text):
    # functors to word tokens ratio
    f_list = json.load(open("koppel_function_words.json"))

    for sent_token in text.sent_tokens:
        functors = dict.fromkeys(f_list, 0)
        functors = OrderedDict(functors)
        functors_count = 0
        sent_word_tokens = word_tokenizer(sent_token)
        for key, value in functors.items():
            for word_token in sent_word_tokens:
                if word_token.lower() == key:
                    functors_count += 1
        if len(sent_word_tokens) != 0:
            functor2word = functors_count / len(sent_word_tokens)
            self.d4hm_10_functor2word_ratio.append(functor2word)


def word_tokenizer(raw):
    """
    Function:
        Here I use nltk.casual tokenize, and then filter the punctuations.
        re tokenizer doesn't work perfectly
        # accept a string(contains one user's all writings in a certain model), return a list of tokens with NLTK word
        # _tokenized function, which will contain punctuations as well as words.
    Input:
        text: a string contains a given user's all writing in a certain model.
        clean: a bool, if True, you will get CLEAN word tokens, not friendly to string like "$3.5" or
         "12:35 p.m.", so not recommended.(realizing by calling keras function
         keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
          lower=True, split=' '). False otherwise.
    Output:
        word_tokens: a list of words without punctuations.
    Notice:
        Abbreviations are tokenized as a whole piece, ie, "won't".
    """
    # RE tokenizer is wrong
    # word_tokens = nltk.regexp_tokenize(text, pattern=r"\$[\d\.]+|\d+:\d+|[ap]+.m.|\w+[\']?[-]*\w+")
    word_tokens = []
    word_punct_tokens = nltk.casual_tokenize(raw)
    # eliminate punctuations
    PUNCK_RE = re.compile(r'[^\s\w]+$')
    for token in word_punct_tokens:
        if PUNCK_RE.match(token) is None:
            word_tokens.append(token)
    return word_tokens
