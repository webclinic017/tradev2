from jugaad_trader import Zerodha
import os
import click
from jugaad_trader.util import CLI_NAME
import pickle

# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential
import configparser

class ZerodhaAuth:
    kite = None
    @classmethod
    def get_kite(cls):
        if cls.kite == None:
            creds = cls.get_creds()
            kite = Zerodha(
                user_id=creds['Zerodha']['usr'], 
                password=creds['Zerodha']['pwd'], 
                twofa=creds['Zerodha']['pin'])
            
            try:
                kite.set_access_token()
                profile = kite.profile()
            except:
                print(f'Logging in')
                login = kite.login()
                cookie_path = os.path.join(click.get_app_dir(CLI_NAME), ".zsession")
                with open(cookie_path, "wb") as fp:
                    pickle.dump(kite.reqsession ,fp)
                profile = kite.profile()
            print(f'Logged in as {profile["user_name"]}')
            cls.kite = kite
        return cls.kite
    
    @classmethod
    def get_creds(self):
        # keyVaultName = 'cred-rohit'
        # KVUri = f"https://{keyVaultName}.vault.azure.net"
        # secretName = "creds"

        # credential = DefaultAzureCredential()
        # azure_client = SecretClient(vault_url=KVUri, credential=credential)

        # retrieved_secret = azure_client.get_secret(secretName)
        # config = configparser.RawConfigParser()
        # config.read_string(retrieved_secret.value.replace('\\n','\n'))

        # config = {'Zerodha':{'usr':'HD8422','pwd':'#ze#rgkm#764484','pin':'764484'}}

        return config