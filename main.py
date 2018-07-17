__author__ = 'Mojca'

#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class CvHandler (BaseHandler):
    def get(self):
        self.render_template("cv.html")

class AboutHandler(BaseHandler):
    def get(self):
        self.render_template("about.html")

class ContactHandler(BaseHandler):
    def get(self):
        self.render_template("contact.html")

class RealizedProjectsHandler(BaseHandler):
    def get(self):
        self.render_template("realized.projects.html")

class ActualProjectsHandler(BaseHandler):
    def get(self):
        self.render_template("actual.projects.html")

class DeasignStudioHandler(BaseHandler):
    def get(self):
        self.render_template("design.studio.html")

class GraphicDeasignHandler(BaseHandler):
    def get(self):
        self.render_template("graphic.design.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/cv', CvHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/realized.projects', RealizedProjectsHandler),
    webapp2.Route('/actual.projects', ActualProjectsHandler),
    webapp2.Route('/design.studio', DeasignStudioHandler),
    webapp2.Route('/graphic.design', GraphicDeasignHandler),

], debug=True)