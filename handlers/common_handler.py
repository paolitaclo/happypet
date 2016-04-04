import logging

log = logging.getLogger(__name__)

from base import BaseHandler

class MainHandler(BaseHandler):
  def get(self):
    self.render_response('index.html')
    
    
class HTMLHandler(BaseHandler):
  def get(self, template):
    self.render_response(template + '.html')