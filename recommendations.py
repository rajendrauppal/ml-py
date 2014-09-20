#!/usr/bin/env python

"""
The MIT License (MIT)

Copyright (c) 2014 Rajendra Kumar Uppal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Development environment:
#   - Python 2.7.5 (32-bit)
#   - Windows 7 64-bit machine


import json
from pprint import pprint


def getMovieRatings(jsonFile):
    with open(jsonFile) as dataFile:
        data = json.load(dataFile)
    pprint(data)


def movieRecommendations():
    getMovieRatings("movie_ratings.json")


def main():
    movieRecommendations()


if __name__ == '__main__':
    main()