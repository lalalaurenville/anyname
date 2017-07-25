
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template(
            'templates/moves.html')
        self.response.write(template.render())

class FashionHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template(
            'templates/Fashion.html')
        self.response.write(template.render())

class FoodHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template(
            'templates/food2.html')
        self.response.write(template.render())

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template(
            'templates/events.html')
        self.response.write(template.render())
class ConcertsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/concerts.html')
        self.response.write(template.render())
class SportsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/sports.html')
        self.response.write(template.render())
class MoviesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/movies.html')
        self.response.write(template.render())
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Fashion.html', FashionHandler),
    ('/food', FoodHandler),
    ('/events.html', EventsHandler),
    ('/concerts.html', ConcertsHandler),
    ('/sports.html', SportsHandler),
    ('/movies.html', MoviesHandler)
], debug=True)
