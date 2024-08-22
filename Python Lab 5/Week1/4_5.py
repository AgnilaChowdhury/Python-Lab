it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


try:
    it_companies.remove('Nonexistent')  
except KeyError:
    print("The item 'Nonexistent' was not found in the set using remove.")

it_companies.discard('Nonexistent')  
print("After discard, it_companies:", it_companies)
