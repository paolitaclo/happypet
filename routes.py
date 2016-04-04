import webapp2

from handlers import *

route_list = [
  ('/', MainHandler),
  (r'/(.*)', HTMLHandler)
]
  