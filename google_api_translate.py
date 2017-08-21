# @Author: Karthick <ramya>
# @Date:   2017-08-21T12:05:24+02:00
# @Last modified by:   ramya
# @Last modified time: 2017-08-21T12:09:39+02:00


# Example from google-api
# https://github.com/google/google-api-python-client/blob/master/samples/translate/main.py

"""Simple command-line example for Translate.
Command-line application that translates some text.
"""
from __future__ import print_function

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from googleapiclient.discovery import build


def main():

  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build('translate', 'v2',
            developerKey='AIzaSyAdEESnjem20MfBsN2ewkP0qEmyAx-3ICM')
  print(service.translations().list(
      source='en',
      target='de',
      q=['How are you?', 'Please help me translate some text from English to German']
    ).execute())

if __name__ == '__main__':
  main()
