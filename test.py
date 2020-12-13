import wolframalpha 
from main import speak
query = 'Todays Whether'
app_id = 'API'
client = wolframalpha.Client(app_id)
res = client.query(query)
res1 = (next(res.results).text)[:-1]
speak(res1)