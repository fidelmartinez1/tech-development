from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, UsernamePasswordCredential, VisualStudioCodeCredential
from azure.keyvault.keys import KeyClient

##################################################################################################################
# Requirements/Purpose
# The purpose of this code base is to migrate the key value pairs from one key vault to another, with both key vaults existing in different subscriptions
# For authentication using the AzureDefaultCredential constructor, the source config should use the Azure CLI while the destination config should use Visual Studio to sign in
# Prior to running, first register the key vault in Azure Active Directory with the Redirect URI set to the key vault url below then get the client ID from the registered app
# Next, retrieve the tenant ID for the destination key vault and enable Admin Access on your computer
# In VS Code, hit F1 and select "Azure: Sign in to Azure Cloud", select "Azure" then follow the on screen prompts in the browser to authenticate
# Run the code base and if prompted for a password by Keychain, enter your computer password
##################################################################################################################

# Designate variables that do not change, specifically the portions of the vault url
protocol = "https://"
az_domain = ".vault.azure.net/"

# Designate the variables that may change, specifically the vault names, the client ID for the destination vault and the username/password to use for the destination vault
src_vault = "enter name of source key vault"
des_vault = "enter name of destination key vault"
des_tenant = "enter tenant ID of the destination key vault"

src_vault_url = protocol + src_vault + az_domain
des_vault_url = protocol + des_vault + az_domain

# Sets the credentials for the source and destination to be used by the respective client
src_credential = DefaultAzureCredential(exclude_cli_credential = False, exclude_managed_identity_credential = True, exclude_shared_token_cache_credential = True, exclude_visual_studio_code_credential = True)
des_credential = DefaultAzureCredential(exclude_cli_credential = True, exclude_managed_identity_credential = True, exclude_shared_token_cache_credential = True, exclude_visual_studio_code_credential = False)

# Sets the client for the source and destination using the respective vault url and credential
src_secret_client = SecretClient(vault_url = src_vault_url, credential = src_credential)
des_secret_client = SecretClient(vault_url = des_vault_url, credential = des_credential)

# Creates the secrets with all the properties to be used in a later loop
src_secrets = src_secret_client.list_properties_of_secrets()

# Create an empty dictionary to store the key value pairs
src_creds = {}

# Loops through all the secrets while creating the key then pulling the secret and inserting into the dictionary above
for secret in src_secrets:
    key = secret.name
    src_creds[key] = src_secret_client.get_secret(key).value

# Loops through the dictionary and inserts the key value pair into the destination key vault
for key, value in src_creds.items():
    print(f"Inserting secret '{value}' for secret '{key}' into '{des_vault}'")
    secret = des_secret_client.set_secret(key, value)
