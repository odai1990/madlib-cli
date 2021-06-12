import re
def print_wecome_mesage():

    """
    Print wilcome and explane the game and how to play it and waht the result

    Arguments:
        No Arguments
    Returns:
        No return just printing 
    """

    print('\n\n"Welcome To The Game" \n\n In this game you will been asked for enter several adjectives,nouns,numbers and names and collect these and put them in a funny paragraph.\n\n Be Ready  ')



def read_template(file_name):

    """
    Reading file and return it to other function
    Arguments:
        n:string --- ptha file 
    Returns:
        String of all countent of ifle 
    """
    try:
        with open(file_name) as file:
            content_text=file.read()             
    except Exception:             
        raise FileNotFoundError("missing.txt")      

    return content_text



def parse_template(content_text):

    """
    Saprate text form each location will replace it inputs user
    Arguments:
        content_text:string --- test 
    Returns:
        list contane stripted text and what we stripted in tuple 
    """

    all_changes=re.findall('{(.+?)}',content_text)
    all_text_stripted=re.sub("{(.+?)}", "{}",content_text)
    return all_text_stripted,tuple(all_changes)



def read_from_user(input_user): 

    """
    Reaing inputs from user
    Arguments:
        input_user:string --- to let users knows waht he should insert
    Returns:
        string of waht user input
    """

    return input(f'> Please Enter {input_user}: ')


def merge(*args):

    """
    put every thing toguther  what user input and stripted text
    Arguments:
        args:list --- list of wat user input and stripted text
    Returns:
        return text merged with user inputs
    """

    return args[0].format(*args[1])


def save(final_content):

    """
    save the file to specifec location with final content 
    Arguments:
        path:string --- the path where you whant to add
        final_content:string --- final text 
    Returns:
      none/ just print result
    """

    with open('assets/result.txt','w') as file:
        file.write(final_content)
    print(final_content)


def start_game():

    """
    Strating the game and mangae the order of calling functions 
    Arguments:
       none
    Returns:
       none
    """

    print_wecome_mesage()    
    content_of_file=parse_template(read_template('assets/sample.txt'))   
    save(merge(content_of_file[0],map(read_from_user,content_of_file[1])))
   

def test_prompt(capsys, monkeypatch):
    monkeypatch.setattr('path.to.yourmodule.input', lambda: 'no')
    val = start_game()
    assert not val



if __name__ == '__main__':
    start_game()
