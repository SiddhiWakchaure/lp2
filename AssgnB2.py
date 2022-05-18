import string
import random


def notify_responses():
    global name, chatbotName, ticket, responses
    responses = {
        'quit': {
            'keyword': ['end', 'bye', 'quit'],
            'response': "Hope you are satisfied by our Customer Service Interaction\nThank you " + name
        },
        'my_name': {
            'keyword': ['my name'],
            'response': f"Hi {name}, nice to meet you"
        },
        'your_name': {
            'keyword': ['your name'],
            'response': f"My name is {chatbotName}"
        },
        'rename': {
            'keyword': ['rename', 'repair', 'status'],
            'response': f"Woah! I like my new name "
        },
        'hello': {
            'keyword': ['hi', 'hello', 'good morning', 'good evening'],
            'response': "Good morning " + name
        },
        'warranty': {
            'keyword': ['warranty', 'guarantee'],
            'response': "We understand your problem with our product\n"
            + f"We have created a ticket\nTicket number: {ticket}"
            + "\nTo avail warranty/guarantee please visit your nearest Service Center"
        },
        'ticket': {
            'keyword': ['ticket'],
            'response': '\nPlease enter your ticket number again\n>'
        },
        'valid_ticket': {
            'keyword': [],
            'response': "Your product is currently undergoing repairs.\nETA: 22nd May"
        },
        'invalid_ticket': {
            'keyword': [],
            'response': 'Sorry, we found no ticket matching to your ticket number'
        },
    }


def keyword_find(keyword):
    return any(x in query for x in responses[keyword]['keyword'])


def get_response(keyword):
    return responses[keyword]['response']


def converse(query: str):
    global name, chatbotName, ticket, responses

    if keyword_find('quit'):
        res = get_response('quit')

    elif keyword_find('my_name'):
        name = query.split(' ')[-1].capitalize()
        notify_responses()
        res = get_response('my_name')

    elif keyword_find('your_name'):
        res = get_response('your_name')

    elif keyword_find('rename'):
        chatbotName = query.split(' ')[-1].capitalize()
        notify_responses()
        res = get_response('rename')
        for ch in chatbotName:
            res += ch.upper() + ' '

    elif keyword_find('hello'):
        res = get_response('hello')

    elif keyword_find('warranty'):
        ticket = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k=5)).upper()
        notify_responses()
        res = get_response('warranty')
    elif keyword_find('ticket'):
        t2 = input(get_response('ticket')).upper()
        if ticket == t2:
            res = get_response('valid_ticket')
        else:
            res = get_response('invalid_ticket')
    else:
        res = "I am not smart enough to handle this query.\nPlease contact our customer representative"
    return res


if __name__ == "__main__":
    global name, chatbotName, ticket, responses
    name = ''
    chatbotName = 'Aero0XTP'
    ticket = ''

    notify_responses()

    query = str(
        input('Welcome to Aero Mobile Services.\nHow may we help you?\n>')).lower()
    while not keyword_find('quit'):
        print(converse(query))
        print()
        query = str(input('>')).lower()
