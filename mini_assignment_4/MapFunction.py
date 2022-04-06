input_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
ListContainingA = sum(map(lambda x: x[0] == 'A', input_list))
ListContaininga = sum(map(lambda x: x.lower().count("a"), input_list))-ListContainingA
print("Occurence Of A : "+str(ListContainingA))
print("Occurence Of a : "+str(ListContaininga))
