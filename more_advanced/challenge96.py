#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import pprint


URL= "https://opentdb.com/api.php?amount=10&category=9&difficulty=hard&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    questions= requests.get(URL).json()
    pprint.pprint(questions)

    for question in questions.get("results"):
        print(question.get("question"))
        print(question.get("correct_answer"))
        print(question.get("incorrect_answers"))
        
        choices = []
        choices = [question.get("correct_answer"), question.get("incorrect_answer")[0], question.get("incorrect_answer")[1], question.get("incorrect_answer")[2]]
        


if __name__ == "__main__":
    main()

