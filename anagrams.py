#!/usr/bin/python

"""
An anagram searching program. Takes an input word
and searches through a list of words to determine
an anagram with just two words and an anagram with
the most possible words.
"""

__author__ = "Arian Solberg"
__version__ = "1.0.1"
__email__ = "asolberg@gmail.com"

import re
import sys
import copy
import argparse

def removeListItem(user_list, remove_item):
  user_list_copy = copy.deepcopy(user_list)
  user_list_copy.remove(str(remove_item))
  return user_list_copy

def removeLetters(letters_list, letters_to_remove):
  letters_list_copy = copy.deepcopy(letters_list)
  for letter in letters_to_remove:
    letters_list_copy.remove(letter)  
  return letters_list_copy
  

def letterCountIsEqual(word1, word2):
  word2 = word2.strip()
  for i, letter in enumerate(word1):
    if word1.count(letter) != word2.count(letter):
      return 0
    if i == len(word1)-1:
      return 1
    

def findAnagrams(main_word, word_list, subtraction_string=""):
  subset_list = []
  for word in word_list:     
    for i, letter in enumerate(word):
      # Might need to check for other types of chars depending
      # on the rules such as spaces and hypens and punctuation
      # marks etc. 
      if word.count(letter) > main_word.count(letter):
        break
      if i == len(word) -1:
        subset_list.append(word)
  if len(subset_list) == 0:
    if letterCountIsEqual(input_word_perm, subtraction_string):
      # found anagram, append to list
      master_anagram_list.append(subtraction_string[1:])
    return
  for sub_word in subset_list:
    findAnagrams(removeLetters(main_word, sub_word), removeListItem(subset_list, sub_word), subtraction_string + " " + sub_word)
  


if __name__ == "__main__":

# Check for correct command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("word", help="Starting word")
  parser.add_argument("masterwordlist", help="Master list of words")
  args = parser.parse_args()
 
  #Global variables
  master_anagram_list = []
  input_word = list(args.word)
  word_list = []
  input_word_perm = copy.deepcopy(input_word)
 
  #Main search loop
  with open(args.masterwordlist) as f:
    for line in f:
      word_list.append(line.strip())
  findAnagrams(input_word, word_list)
 
# Report results
  longest_anagram = ""
  two_word_anagram = ""
  for anagram in master_anagram_list:
    if anagram.count(" ") > longest_anagram.count(" "):
      longest_anagram = anagram
    if two_word_anagram =="":
      if anagram.count(" ") == 1:
        two_word_anagram = anagram
  if two_word_anagram:
    print "An anagram with two words is: %s" % two_word_anagram
    print "An anagram with the most words is: %s" % longest_anagram
  elif longest_anagram:
    print "No two word anagram found!"
    print "An anagram with the most words is: %s" % longest_anagram
  else:
    print "No anagrams found."
