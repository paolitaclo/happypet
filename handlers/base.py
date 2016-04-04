import os
import urllib

import webapp2
import json

import jinja2
import logging

log = logging.getLogger(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.PackageLoader('happypet', 'templates'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True
)

class BaseHandler(webapp2.RequestHandler):
  
  def __init__(self, request, response):self.initialize(request, response)
      
  def render_response(self, _template, **context):
    template = JINJA_ENVIRONMENT.get_template(_template)
    self.response.write(template.render(context))
    
  def render_json(self, obj):
    rv = json.dumps(obj)
    self.response.headers.content_type = 'application/json'
    self.response.write(rv)
    
    