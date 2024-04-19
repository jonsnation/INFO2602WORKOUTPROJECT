from App.database import db

class Routine(db.Model):
    routine_id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), nullable=False)
    workout = db.relationship('Workout', backref='routine', lazy = True)

    def __init__(self, user_id, workout_id):
        self.user_id = user_id
        self.workout_id = workout_id

    def get_json(self):
        return {
            'routine_id': self.routine_id,
            'user_id': self.user_id,
            'workout': self.workout.get_json()
        }

