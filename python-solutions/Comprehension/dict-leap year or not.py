year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
result = {year[i]:('yes' if year[i] % 4 == 0 or year[i] % 400 == 0 and year[i] % 100 == 0 else 'no') for i in range(0, len(year))}
print(result)
