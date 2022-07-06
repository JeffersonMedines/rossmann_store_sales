import pandas as pd
import json
import requests

def load_dataset( store_id ):
    # Loading test dataset
    df10 = pd.read_csv( '/home/jeffsmedines/repos/ds_producao/data/test.csv' )
    df_store_raw = pd.read_csv( '/home/jeffsmedines/repos/ds_producao/data/store.csv' )

    # Merge test dataset + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

    # Coose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    # Remove closed days, NA's and ID column
    df_test = df_test[df_test['Open'] == 1]
    df_test = df_test[~df_test['Open'].isnull()]
    df_test = df_test.drop( 'Id', axis=1 )

    # Convert dataframe to json
    data = json.dumps( df_test.to_dict( orient='records' ) )

    return data

def predict( data ):
    # API Call
    url = 'https://rossmann-predict-model.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post( url, data=data , headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

# d2 = d1[['store', 'predictions']].groupby( 'store' ).sum().reset_index()
# for i in range( len( d2 ) ):
#     print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
#             d2.loc[i, 'store'],
#             d2.loc[i, 'predictions']) )