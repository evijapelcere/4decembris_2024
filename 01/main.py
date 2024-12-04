""" Insert Name """
name = input("Whats your name: ")  # Lietotājam tiek prasīts, lai viņs ievada savu vārdu ar funkciju "input"

""" Insert age. Also convert age into an Integer value """
age = int(input("How old are you: "))  #Lietotājam ar funkciju "input" tiek prasīts, lai viņš ievada savu vecumu, bet pirms tam ar "integer" tiek noteikts, ka ievadītā informācija ir skaitlis.

""" Do the math """
year = str((2018 - age)+100)  #Tiek aprēķināts vecums, kuru lietotājs būs sasniedzis 2102. gadā, tiek noteikts, ka aprēķins tiks veikts ar "string" datiem, sākumā no 2018. gada tiek atņemts lietotāja vecums, lai gan šobrīd ir jau 2024. gads, kas nozīmē, ka informāciju vajadzētu atjaunot, pēc tam pie iegūtā rezultāta tiek pieskaitīti vēl 100 gadi.
""" Print the result """
print(name + " will be 100 years old in the year " + year) # Tiek izprintēts lietotāja vārds un teksts, kura beigās ir pateikts, cik vecs viņš būs 2102. gadā.
