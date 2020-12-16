import wolframalpha 
from main import speak
# query = 'Todays Whether'
# app_id = 'API'
# client = wolframalpha.Client(app_id)
# res = client.query(query)
# res1 = (next(res.results).text)[:-1]
# speak(res1)
def client_query(quest) : 
    client = wolframalpha.Client('')
    result = client.query(quest)
    result = (next(result.results).text)
    result = result[0:6]
    speak(result)

client_query('1 dollar to rupee')