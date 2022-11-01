expression = 0

def init(sample):
    global expression
    expression = sample
    

def do_it(sample): 
    result = eval(sample)
    return result