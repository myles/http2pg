"""
Copyright 2009 Myles Braithwaite <me@mylesbraithwaite.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import psycopg2.extras
import psycopg2
import logging
import web

try:
	import json as simplejson
except ImportError:
	import simplejson

log = logging.getLogger('http2pg.http')

urls = (
	'/query', 'Query',
)

class Query:
	
	def POST(self):
		query = web.data()
		
		conn = psycopg2.connect("dbname=myles_website user=myles")
		cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		
		cur.execute(query)
		log.info(cur.query)
		
		rows = cur.fetchall()
		
		cur.close()
		conn.close()
		
		results = []
		for row in rows:
			results += [dict(row),]
		
		return simplejson.dumps(results)

app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()