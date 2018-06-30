from congress import Congress

API_KEY = 'yVbIvFN2w9CBAvRLcTHheLYA4o8mDmjJqPlpagma'

dictPerson = {}

def getChamberList(chamber):
    
    congress = Congress(API_KEY)
    all_members = congress.members.filter(chamber)
    
    # print (all_members)
    num_results = int(all_members[0]["num_results"])
    
    member_list = all_members[0]["members"]
    
        
    i = 0
    while i < num_results:
        dictPerson[i] = member_list[i]["id"]
        cdb_id = member_list[i]["id"]
        title = member_list[i]["short_title"]
        first_name = member_list[i]["first_name"]
        last_name = member_list[i]["last_name"]
        state = member_list[i]["state"]
        party = member_list[i]["party"]
        print ("%s: %s %s %s (%s) %s" % (cdb_id, title, first_name, last_name, party, state))
        i += 1

# pelosi = congress.members.get('P000197')
# print (pelosi['twitter_account'])

if __name__ == '__main__':
    getChamberList("senate")   
        