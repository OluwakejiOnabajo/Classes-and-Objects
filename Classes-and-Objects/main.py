class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    #methods
    def change_name(self, name):
        self.name = name
        print(f"Name changed to {name}")
    
    def change_age(self, age):
        try: #try to convert age to int
            self.age = int(age)

        except: #if not possible, print error message
            print("Age must be a number")
        print(f"Age changed to {age}")

    def add_track(self, track):
        oldTrack = list(self.tracks)
        newTrack = list(track)
        print(f"Your new track is {oldTrack + newTrack}")

    def get_score(self):
        print(f"Your score is {self.score}")
    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
