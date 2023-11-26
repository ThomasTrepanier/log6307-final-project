data= [['SiteUrl','Url','Title'],['SiteUrl','Url','Title']]
def recursive_apply(x, f=lambda v: v.lower()):
    if type(x) is list: 
        return [recursive_apply(el) for el in x]
    return f(x)
recursive_apply(data)   
