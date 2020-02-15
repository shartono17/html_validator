


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tag_list = _extract_tags(html)
    if tag_list == []:
        return False
    else: 
        s = []
        symbol = ''
        balanced = True
        for i in range(len(tag_list)):
            currtag = tag_list[i]
            if currtag[1] != '/':
                s.append(currtag)
            elif currtag[1] == '/':
                symbol = '</'
                if s == []:
                    return False
                else: 
                    top = s.pop()
                    topsym = top[0]
                    if  _matches(topsym, symbol) and (top[1:]==currtag[2:] ):
                        balanced = True
                    else: balanced = False

        if balanced and s==[]:
            return True
        else: return False

    


def _matches(left, right):
    openbrack = '<'
    closebrack = '</'
    return openbrack.index(left) == closebrack.index(right)


    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>',
    '''
    if "<" and "</" and ">" not in html:
        return []
    else: 

        parsed_tags = []
#    i = 0
#    while i < len(html):
        for i in range(len(html)):
            temp = ''
            end_tag = ">"
            currsym = html[i]
            if currsym == "<":
                while currsym != ">":
                    temp += currsym
                    i += 1
                    currsym = html[i]
                temp += ">"
                parsed_tags.append(temp)
        return parsed_tags

# def _extract_tags(html):
#     parsed_tags = []
#    if len(html) <
#    i = 0
#     while i<len(html)
