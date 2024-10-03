#%%
claves = [
    {"llave":"ALSEA.MX", "trend":"alsea"},
    {"llave":"BBVA.MX", "trend":"bbva"},
    {"llave":"C.MX", "trend":"citibanamex"},
    {"llave":"CHDRAUIB.MX", "trend":"chedraui"},  
    {"llave":"FEMSAUB.MX", "trend":"femsa"}, 
    {"llave":"HCITY.MX", "trend":"city express"}, 
    {"llave":"LABB.MX", "trend":"genomma lab"}, 
    {"llave":"LIVEPOLC-1.MX", "trend":"liverpool tienda"}, 
    {"llave":"LIVEPOL1.MX", "trend":"liverpool tienda"},  
    {"llave":"VOLARA.MX", "trend":"volaris"}
     ]

#%% 
import pandas as pd
import yfinance as yf

#%%
for clave in claves:
    clave

#%%
serie = yf.Ticker(clave['llave'])
clave['industry'] = serie.info['industry']
# %%

# https://pypi.org/project/yfinance/