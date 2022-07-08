#!/bin/bash
curl -s 'https://raw.githubusercontent.com/meetDeveloper/freeDictionaryAPI/master/meta/wordList/english.txt' | egrep "^${1}"
