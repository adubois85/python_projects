import pprint as pp

def etaoin(text: str) -> dict:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    count_dict = {}
    for i in range(len(letters)):
        count_dict[letters[i]] = ''
    for i in range(len(text)):
        if text[i] in letters:
            # the Unicode endpoint for the full block character
            count_dict[text[i]] += "\u2588"
    return count_dict

sentence = input('Enter a sentence and get back a janky bar graph!\n')

pp.pprint(etaoin(sentence))
