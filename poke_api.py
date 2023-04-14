import requests

Poke_api_link = 'https://pokeapi.co/api/v2/pokemon/'

def get_poke_info(pokemon):
    """ Gets info about a specific Pokemon from the PokeAPi.
    
    Args:
         pokemon (str): Pokemon name (or Pokedex number )
         
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
#converting to string object and all lower case
    pokemon = str(pokemon).strip().lower() 
    
#checking if the name is an empty string 
    if pokemon == '':
        print('Error : Pokemon name not found')
        return 

#sending GET request 
    print(f'Getting information for {pokemon}... ', end='')
    url = Poke_api_link +pokemon
    
    response_message = requests.get(url)
    
# check if the request was successful 
    if response_message.status_code == requests.codes.ok:
        print('successful')
    
#Return dictionary of Pokemon 
        return response_message.json()
    else:
        print('failure')
        print(f' Response code: {response_message.status_code}({response_message.reason})')

        return
    
    if __name__ == '__main__':
        main()