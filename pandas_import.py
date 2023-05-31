import pandas as pd

states = ["California","Texas","Florida","New york"]
population = ["213456","456799","123456","6424689"]

dict_states= {'States': states,'Population': population}

df_states= pd.DataFrame.from_dict(dict_states)
#print(df_states)
df_states.to_csv('states.csv',index = False )
