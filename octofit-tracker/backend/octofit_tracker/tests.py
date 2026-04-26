from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test')
        self.assertEqual(str(user), 'testuser')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=10)
        self.assertEqual(str(activity), 'testuser - run')

    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(str(lb), 'Test Team: 50')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
