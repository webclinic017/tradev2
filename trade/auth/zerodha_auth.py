from jugaad_trader import Zerodha
import os
import click
from jugaad_trader.util import CLI_NAME
import pickle

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import configparser

def get_kite():
    creds = get_creds()
    kite = Zerodha(
        user_id=creds['Zerodha']['usr'], 
        password=creds['Zerodha']['pwd'], 
        twofa=creds['Zerodha']['pin'])
    
    try:
        kite.set_access_token()
        profile = kite.profile()
    except:
        login = kite.login()
        cookie_path = os.path.join(click.get_app_dir(CLI_NAME), ".zsession")
        with open(cookie_path, "wb") as fp:
            pickle.dump(kite.reqsession ,fp)
        profile = kite.profile()
    print(f'Logged in as {profile["user_name"]}')

    return kite

def get_creds():
    keyVaultName = 'cred-rohit'
    KVUri = f"https://{keyVaultName}.vault.azure.net"
    secretName = "creds"

    credential = DefaultAzureCredential()
    azure_client = SecretClient(vault_url=KVUri, credential=credential)

    retrieved_secret = azure_client.get_secret(secretName)
    config = configparser.RawConfigParser()
    config.read_string(retrieved_secret.value.replace('\\n','\n'))

    return config