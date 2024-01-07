text = input()
def counter (txt):
    words = txt.split() 
    count = {}
    
    for word in words:
        count[word] = len(word)
        
    return count
        
print(counter(text))
