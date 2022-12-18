import pandas as pd
import os
import json
import requests
from flask import Flask, request, Response

# constants
TOKEN = '5434794068:AAGiAOX_nn3eZsRKVYk1AAP2RBJmgbEAPss'

# # Info about the bot
# https://api.telegram.org/bot5434794068:AAGiAOX_nn3eZsRKVYk1AAP2RBJmgbEAPss/getMe

# # Get updates
# https://api.telegram.org/bot5434794068:AAGiAOX_nn3eZsRKVYk1AAP2RBJmgbEAPss/getUpdates

# # Webhook
# https://api.telegram.org/bot5434794068:AAGiAOX_nn3eZsRKVYk1AAP2RBJmgbEAPss/setWebhook?url=https://01b15a4273e0b2.lhrtunnel.link

# # Send message
# https://api.telegram.org/bot5434794068:AAGiAOX_nn3eZsRKVYk1AAP2RBJmgbEAPss/sendMessage?chat_id=1370535702&text=Hi Jefferson




def send_message( chat_id, text ):
    url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
    url = url + 'sendMessage?chat_id={}'.format( chat_id )
    r = requests.post( url, json={'text': text} )
    print( 'Status Code {}'.format( r.status_code ) )

    return None


def load_dataset( store_id ):
    # Loading test dataset
    df10 = pd.read_csv( 'bot_render_deploy/test.csv' )
    df_store_raw = pd.read_csv( 'bot_render_deploy/store.csv' )

    # Merge test dataset + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

    # Coose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:
        # Remove closed days, NA's and ID column
        df_test = df_test[df_test['Open'] == 1]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop( 'Id', axis=1 )

        # Convert dataframe to json
        data = json.dumps( df_test.to_dict( orient='records' ) )
    else:
        data = 'error'

    return data

def predict( data ):
    # API Call
    url = 'https://rossmann-predict-app.onrender.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post( url, data=data , headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

def parse_message( message ):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace( '/', '' )

    try:
        store_id = int( store_id )

    except ValueError:
        
        store_id = 'error'

    return chat_id, store_id

# API initialize
app = Flask( __name__ )

@app.route( '/', methods=['GET', 'POST'] )
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message( message )

        if store_id != 'error':
            # Loading data
            data = load_dataset( store_id )

            if data != 'error':
                # Prediction
                d1 = predict( data )

                # Calculation
                d2 = d1[['store', 'predictions']].groupby( 'store' ).sum().reset_index()

                
                # Send message
                msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
                        d2['store'].values[0],
                        d2['predictions'].values[0])

                send_message( chat_id, msg )
                return Response( 'Ok', status=200 )

            else:
                send_message( chat_id, 'Store Not Available' )
                return Response( 'Ok', status=200 )
        else:
            send_message( chat_id, 'Store ID is Wrong' )
            return Response( 'Ok', status=200 )

    

    else:
        return '<h1> Rossmann Telegram Bot</h1>'

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=port )