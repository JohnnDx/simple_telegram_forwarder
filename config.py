

class ConfigClass:
    api_id =   
    api_hash = ''
    
    # To Get Session String Use Telegram Bot like @SessionGeneratorBot
    session_string = ''
    # Remove emoji from forwarded message
    remove_emoji = False
    # Webhook request using python
    webhook_request = False
    # URL for Post Request with Message Data
    post_url = 'https://webhook.site/' 
    
    from_chats =[] # list ids of channels you want to forward from (use id)
    to_chat =  # id of channel you want to forward to

    
    filter_string = "" # message has to contain this phrase in order to forward it | Leave empty if you want to forward everything.
    filter_string_replace_to = "" # replaces above string with this one | If you have filter_string empty, leave this empty as well.

    passphrase = '' # passphrase for extra security on receiver webhook server | If you use webhooks, it's recommended to use it.