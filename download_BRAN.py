#!/usr/share/anaconda3/bin/python
#-*-encoding:UTF-8-*-
import urllib.request
from urllib.error import HTTPError, URLError
import os
import pandas as pd
from datetime import datetime as dt, timedelta

###############################################################
#######       Área que pode ser modificada!!!!         ########
###############################################################
# Caminho no EKMAN

path = "/data/MOVAR/modelos/REANALISES/BRAN/"
#################################################
# Corte da área

# download oeste
latnorte = '20'
latsul = '-80'
lonleste1 = '50'
lonoeste1 = '0'

# download leste
latnorte = '20'
latsul = '-80'
lonleste2 = '360'
lonoeste2 = '270'

# erro
#Invalid bbox. Bounding Box must have east > west; if crossing 180 meridian, use east boundary > 180

#################################################
# Período

time_start = '1993-01-01'
time_end = '1993-01-01' 
inicio = time_start[0:4]+'_'+time_start[5:7]  #'1993_01'

#################################################
# Variáveis

# Opções -----------------------------

# ocean_eta_t :  sea surface height
# ocean_salt :  salinity
# ocean_temp :  temperature
# ocean_u :  u-component of current
# ocean_v :  v-component of current

#------------------------------------

variavel = 'eta_t'

###############################################################
#####       Área que NÃO deve ser modificada!!!!         ######
###############################################################

if variavel == 'eta_t':
  var_name = 'ssh'
  VAR_name = 'SSH'

elif variavel == 'salt':
  var_name = 's'
  VAR_name = 'S'  

elif variavel == 'temp':
  var_name = 't'
  VAR_name = 'T' 

elif variavel == 'u':
  var_name = 'u'
  VAR_name = 'U'       

elif variavel == 'v':
  var_name = 'v'
  VAR_name = 'V'  


# Baixar dados diarios do BRAN ###################################
print('Download do arquivo diário do BRAN... '+time_start)

url_principal = 'https://dapds00.nci.org.au/thredds/ncss/gb6/BRAN/BRAN2020/daily/'


# download oeste ------------------------------------------
print('Download oeste')

url1 = url_principal + 'ocean_'+variavel+'_'+inicio+'.nc?var='+variavel+'&north='+latnorte+'&west='+lonoeste1+'&east='+lonleste1+'&south='+latsul+'&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start='+time_start+'T12%3A00%3A00Z&time_end='+time_end+'T12%3A00%3A00Z&timeStride=1'

urllib.request.urlretrieve(url1, path+VAR_name+'/BRAN_'+var_name+'_daily_'+time_start+'_1.nc')
 

# download leste ------------------------------------------
print('Download leste')

url2 = url_principal + 'ocean_'+variavel+'_'+inicio+'.nc?var='+variavel+'&north='+latnorte+'&west='+lonoeste2+'&east='+lonleste2+'&south='+latsul+'&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start='+time_start+'T12%3A00%3A00Z&time_end='+time_end+'T12%3A00%3A00Z&timeStride=1'

urllib.request.urlretrieve(url2, path+VAR_name+'/BRAN_'+var_name+'_daily_'+time_start+'_2.nc')
 


## Unindo os dois arquivos ------------------------------------------
print('Juntando arquivos')

os.system('cdo merge BRAN_'+var_name+'_daily_'+time_start+'_1.nc BRAN_'+var_name+'_daily_'+time_start+'_2.nc BRAN_'+var_name+'_daily_'+time_start+'.nc')

##

#https://dapds00.nci.org.au/thredds/ncss/gb6/BRAN/BRAN2020/daily/
#ocean_eta_t_1993_01.nc?north=20&west=-90&east=50&south=-80&horizStride=1&time_start=1993-01-01T12%3A00%3A00Z
#&time_end=1993-01-02T12%3A00%3A00Z&timeStride=1
#
#https://dapds00.nci.org.au/thredds/ncss/gb6/BRAN/BRAN2020/daily/
#ocean_eta_t_1993_01.nc?var=eta_t&north=20&west=-90&east=50&south=-80&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start=1993-01-01T12%3A00%3A00Z&time_end=1993-01-02T12%3A00%3A00Z&timeStride=1

## exemplo

#https://dapds00.nci.org.au/thredds/ncss/gb6/BRAN/BRAN2020/daily/ocean_eta_t_2012_01.nc?var=eta_t&north=20&west=270&east=50&south=-80&disableProjSubset=on&horizStride=1&time_start=2012-01-01T12%3A00%3A00Z&time_end=2012-01-31T12%3A00%3A00Z&timeStride=1

'''
'''






