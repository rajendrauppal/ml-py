#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Development environment:
#   - Python 2.7.5 (32-bit)
#   - Windows 7 64-bit machine


import json
from pprint import pprint


def getMovieRatings(jsonFile):
    """ Reads movie ratings from json file and returns an object """
    with open(jsonFile) as ratingsFile:
        ratings = json.load(ratingsFile)
    return ratings


# Calculate similarity score
# Two methods: 1. Euclidean distance and 2. Pearson correlation

def calcSimilarityEuclidean(ratings, critic1, critic2):
    """ Calculates similarity score using Euclidean distance method """
    return 0


def calcSimilarityPearson(ratings, critic1, critic2):
    """ Calculates similarity score using Pearson correlation coefficient method """
    pass


def movieRecommendations():
    """ Movie recommendation program based on ratings of critics """
    ratings = getMovieRatings("movie_ratings.json")    
    for critic in ratings:
        print critic
        for movie in ratings[critic]:
            print ratings[critic][movie]

    sim = calcSimilarityEuclidean(ratings, "Mick LaSalle", "Toby")
    print sim


def main():
    movieRecommendations()


if __name__ == '__main__':
    main()
