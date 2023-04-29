import re
from collections import defaultdict
from itertools import tee, islice
from typing import Dict, Tuple, Iterable

def pairwise(iterable: Iterable) -> Iterable:
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def nwise(iterable: Iterable, n: int = 3) -> Iterable:
    iterators = tee(iterable, n)
    for i, it in enumerate(iterators):
        next(islice(it, i, i), None)
    return zip(*iterators)

def calculate_frequencies(sentence: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    digraphs = {"".join(digraph): 0 for digraph in pairwise(sentence)}
    trigraphs = {"".join(trigraph): 0 for trigraph in nwise(sentence, n=3)}
    for digraph in pairwise(sentence):
        digraphs["".join(digraph)] += 1
    for trigraph in nwise(sentence, n=3):
        trigraphs["".join(trigraph)] += 1
    return digraphs, trigraphs

def compare_frequencies(frequencies1: Dict[str, int], frequencies2: Dict[str, int]) -> int:
    total_difference = sum(abs(frequencies1.get(key, 0) - frequencies2.get(key, 0)) for key in set(frequencies1.keys()) | set(frequencies2.keys()))
    return total_difference

def authenticate_user(user1_sentence: str, user2_sentence: str, random_sentence: str) -> int:
    user1_digraphs, user1_trigraphs = calculate_frequencies(user1_sentence)
    user2_digraphs, user2_trigraphs = calculate_frequencies(user2_sentence)
    random_digraphs, random_trigraphs = calculate_frequencies(random_sentence)
    digraph_difference1 = compare_frequencies(user1_digraphs, random_digraphs)
    digraph_difference2 = compare_frequencies(user2_digraphs, random_digraphs)
    trigraph_difference1 = compare_frequencies(user1_trigraphs, random_trigraphs)
    trigraph_difference2 = compare_frequencies(user2_trigraphs, random_trigraphs)
    user1_score = digraph_difference1 + trigraph_difference1
    user2_score = digraph_difference2 + trigraph_difference2
    return 1 if user1_score < user2_score else 2

if __name__ == "__main__":
    user1_sentence = input("User 1, please type a sentence: ")
    user2_sentence = input("User 2, please type a sentence: ")
    random_sentence = input("Random person, please type a sentence: ")
    authenticated_user = authenticate_user(user1_sentence, user2_sentence, random_sentence)
    print(f"The random person's typing is closest to User {authenticated_user}.")
