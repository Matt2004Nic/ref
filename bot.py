from telethon import TelegramClient, client, events
from telethon.tl.functions.messages import SendMessageRequest
from bitly_api import Connection
import bitly_api
import re 


token = '2031158106:AAH3HjnbQST6cH3mLfwf8NveROwACW7Rlmg'
api_id = 15443592
api_hash = "4765a38d2895fcc169c7ce2452c7ebd9"
client = TelegramClient('session_read',api_id,api_hash)


async def mediaworld(event,message_text,BITLY_ACCESS_TOKEN):

    link_list = [
                "https://www.mediaworld.it/", 
                "https://www.eneba.com/", 
                "https://www.comet.it/", 
                "https://www.eprice.it/", 
                "https://www.unieuro.it/", 
                "https://www.mi.com/"
                ]

    ref = "https://www.awin1.com/cread.php?awinmid=18529&awinaffid=576475&ued="


    for link in link_list:
        
        if link in message_text:
            messageCambiato = message_text.replace(':','%3A')
            messageCambiato = messageCambiato.replace('/','%2F')
            refcompleto = ref + messageCambiato + '%3F'

            
            sus=event.chat.id
            messaggioId=event.message.id
            username = event.sender.username
            first_name = event.sender.first_name
            last_name = event.sender.last_name

            #print("link= " + refcompleto)
            access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
            short_url = access.shorten(refcompleto)
            #print(event.sender)
            if last_name != None and username != None:  
                commentoSussyBaka = f"Messaggio inviato da {first_name} {last_name} (@{username}) \n\n{short_url['url']}"
            elif username != None:
                commentoSussyBaka = f"Messaggio inviato da {first_name} (@{username}) \n\n{short_url['url']}"
            elif last_name != None:
                commentoSussyBaka = f"Messaggio inviato da {first_name} {last_name} \n\n{short_url['url']}"
            else: 
                commentoSussyBaka = f"Messaggio inviato da {first_name} \n\n{short_url['url']}" 
            
            #await client.send_message(sus,commentoSussyBaka) 
            #await client.delete_messages(sus,messaggioId) 
            short_url = {}

            access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
            short_url = access.shorten(refcompleto)
            #await client.send_message(sus,commentoSussyBaka) 
            #await client.delete_messages(sus,messaggioId)
            uff=short_url['url']
            return uff
            #except:
            #commento_errore = f"Cambiare token bitly con /c e il token attaccato, il token {BITLY_ACCESS_TOKEN} é scaduto/finito"
            #await client.send_message(-730744224,commento_errore)
        else:
            return None


async def ebay(event,message_text,BITLY_ACCESS_TOKEN):
    ref = "mkevt=1&mkcid=1&mkrid=724-53478-19255-0&campid=5338494094&toolid=10001&"

    if "https://www.ebay.it/" in message_text:
        messageCambiato = message_text.replace('%7C','|') #UwU
        messageCambiato = messageCambiato.replace('%3A',':') #UwU
        messageCambiato = messageCambiato.replace('%3DITM%26','&') #UwU
        messageCambiato = messageCambiato.replace('%3D','=') #UwU
        messageCambiato = messageCambiato.replace('%26','&') #UwU
        refcompleto = messageCambiato.replace('?','?'+ref) #UwU
        #paciuga con i ref
        
        sus=event.chat.id
        messaggioId=event.message.id
        username = event.sender.username
        first_name = event.sender.first_name
        last_name = event.sender.last_name

        short_url = {}

        access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        short_url = access.shorten(refcompleto)
            #await client.send_message(sus,commentoSussyBaka) 
            #await client.delete_messages(sus,messaggioId)
        uff=short_url['url']
        return uff
        #except:
            #commento_errore = f"Cambiare token bitly con /c e il token attaccato, il token {BITLY_ACCESS_TOKEN} é scaduto/finito"
            #await client.send_message(-730744224,commento_errore)
    else:
        return None



async def trippodo(event,message_text,BITLY_ACCESS_TOKEN):
    ref = "?affp=25386"

    if "https://www.trippodo.com/" in message_text:

        refcompleto = message_text + ref
        sus=event.chat.id
        messaggioId=event.message.id
        username = event.sender.username
        first_name = event.sender.first_name
        last_name = event.sender.last_name


        #await client.send_message(sus,commentoSussyBaka) 
        #await client.delete_messages(sus,messaggioId)
        short_url = {}

        access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        short_url = access.shorten(refcompleto)
            #await client.send_message(sus,commentoSussyBaka) 
            #await client.delete_messages(sus,messaggioId)
        uff=short_url['url']
        return uff
        #except:
            #commento_errore = f"Cambiare token bitly con /c e il token attaccato, il token {BITLY_ACCESS_TOKEN} é scaduto/finito"
            #await client.send_message(-730744224,commento_errore)
    else:
        return None



async def gamersOutlet(event,message_text,BITLY_ACCESS_TOKEN):
    ref = "?tracking=hwo"

    if "https://www.gamers-outlet.net/" in message_text:

        refcompleto = message_text + ref
        
        sus=event.chat.id
        messaggioId=event.message.id
        username = event.sender.username
        first_name = event.sender.first_name
        last_name = event.sender.last_name

        short_url = {}

        access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        short_url = access.shorten(refcompleto)
            #await client.send_message(sus,commentoSussyBaka) 
            #await client.delete_messages(sus,messaggioId)
        uff=short_url['url']
        return uff
        #except:
            #commento_errore = f"Cambiare token bitly con /c e il token attaccato, il token {BITLY_ACCESS_TOKEN} é scaduto/finito"
            #await client.send_message(-730744224,commento_errore)
    else:
        return None



#2031158106:AAH3HjnbQST6cH3mLfwf8NveROwACW7Rlmg 


@client.on(events.NewMessage)
async def main(event):

    BITLY_ACCESS_TOKEN = "00dfa870f9e39858e0f5f639497db01af1983b7b"
    print(BITLY_ACCESS_TOKEN)
    message = event.text
    cleaned_string = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    message_text = cleaned_string.findall(message)
    #bitly_error_finder = re.compile("/c(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    #token_changer = bitly_error_finder.findall(message)
    '''for lel in token_changer:
        if lel!=None:
            tokenlul = token_changer[0].replace('/c','')
            BITLY_ACCESS_TOKEN = tokenlul
            f = open("token.txt","w")
            f.write(tokenlul) 
            f.close()
            await client.send_message(-730744224,f"Il token é stato cambiato correttamente, token nuovo: {tokenlul}")'''


    message_return = []
    chat_id=event.chat.id
    messaggioId=event.message.id
    username = event.sender.username
    first_name = event.sender.first_name
    last_name = event.sender.last_name

    for link in message_text:
        sus=await mediaworld(event,link,BITLY_ACCESS_TOKEN)
        if sus!=None:
            message_return.append(sus)
        sus=await ebay(event,link,BITLY_ACCESS_TOKEN)
        if sus!=None:
            print(sus)
            message_return.append(sus)
        sus=await trippodo(event,link,BITLY_ACCESS_TOKEN)
        if sus!=None:
            message_return.append(sus)
        sus=await gamersOutlet(event,link,BITLY_ACCESS_TOKEN)
        if sus!=None:
            message_return.append(sus)
        #print(message_return[message_text.index(link)])
        message=message.replace(link,message_return[message_text.index(link)])
    print(message)
    if len(message_return)>0:
        if last_name != None and username != None:  
            commentoSussyBaka = f"Messaggio inviato da {first_name} {last_name} (@{username}) \n\n{message}"
        elif username != None:
            commentoSussyBaka = f"Messaggio inviato da {first_name} (@{username}) \n\n{message}"
        elif last_name != None:
            commentoSussyBaka = f"Messaggio inviato da {first_name} {last_name} \n\n{message}"
        else: 
            commentoSussyBaka = f"Messaggio inviato da {first_name} \n\n{message}" 
        
        await client.send_message(chat_id,commentoSussyBaka) 
        await client.delete_messages(chat_id,messaggioId)
        
        



client.start()
client.run_until_disconnected() 