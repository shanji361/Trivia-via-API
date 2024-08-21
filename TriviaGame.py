import requests 
import random 

class Quiz():
  def __init__(self, category=None, difficulty=None, limit=5):
    self.category = category
    self.difficulty = difficulty
    self.limit = limit
    self.score = 0
    self.current_question = {}
    self.questions = []

  def activate(self):
    #If quiz is not yet activated
    if not self.questions:
      url = 'https://opentdb.com/api.php'
      params = {
        "amount": self.limit,
        "category": self.category,
        "difficulty": self.difficulty
      }
      r = requests.get(url, params)
      try:
        r = r.json()
      except:
        print("Error:", r.status_code)
        return
      else:
        self.questions = r['results']
        self.current_question = self.questions[0]
        return 

    else:
      print("Quiz already Activated")
      return

  def submit_answer(self, answer):
    if answer.lower() == self.current_question['correct_answer'].lower():
      print("Correct!")
      self.score += 1
    else:
      print("Incorrect!")

    #Loading the next question
    self.questions.pop(0)
    self.current_question = self.questions[0]

  def display_current_question(self):
    print(self.current_question['question'], "\n")
    choices = self.current_question['incorrect_answers']
    #Insert the correct answer amongst the incorrect answers in a random spot
    choices.insert(random.randint(0,len(choices)-1), self.current_question['correct_answer'])
    for choice in choices:
      print(choice)

  def tally_results(self):
    if self.correct + self.incorrect == self.limit:
      return self.correct, self.incorrect
    else:
      print("Quiz not completed")

  def check_score(self):
    print("You have answered", self.score, "questions correctly")
    return self.score


quiz = Quiz(limit=5) #create 5 rounds of game
quiz.activate()

while quiz.current_question:
    quiz.display_current_question()
    user_answer = input("\nYour answer: ")
    quiz.submit_answer(user_answer)

quiz.check_score()