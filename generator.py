def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1
file = open(r"O:\MCA\SE&PM\Chatbot\file.txt", "r")
s = file.read()
l = s.split('##')
file.close()
nl = []
for i in l:
    if "\n" in i:
        i = i.replace('\n', '')

    nl.append(i)
print(len(nl))
nll = []
for i in range(len(nl)):
    if i % 2 == 0:
        nll.append([nl[i], nl[i+1]])
file2 = open(r"O:\MCA\SE&PM\Chatbot\file2.txt", "w")
i = 0
str = """One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Twenty-One Twenty-two Twenty-three Twenty-four Twenty-five Twenty-six Twenty-seven Twenty-eight"""
numberl = str.split()
# f=open('generatedlist.txt','w')
# p=listToString(nll)
# f.write(p)
# f.close()
# for question, answer in nll:
#     file2.write("""<div class="accordion-item">
#     <h2 class="accordion-header" id="panelsStayOpen-heading"""+numberl[i]+"""">
#       <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse"""+numberl[i]+"""" aria-expanded="false" aria-controls="panelsStayOpen-collapse"""+numberl[i]+"""">
#         <b>"""+question+"""</b>
#       </button>
#     </h2>
#     <div id="panelsStayOpen-collapse"""+numberl[i]+"""" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading"""+numberl[i]+"""">
#       <div class="accordion-body">
#         """ + answer + """
#       </div>
#     </div>
#   </div>""")
#     i += 1
# file2.close()
j=0
import json
jsonf=open('new.json','r')
x=json.loads(jsonf.read())
jsonf.close()
print(x["intents"][0])
print(type(x))
for question, answer in nll:
  x["intents"].append({"tag": question,"patterns":question,"responses":answer,"context_set": ""})
  j+=1
# jsonf.write()
jsonf=open('new.json','w')
json.dump(x, jsonf)
jsonf.close()

