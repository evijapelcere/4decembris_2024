""" Method 1 """

num = int(input("Give me a number to check: ")) # Lietotājam ar funkciju input, jautā, lai viņš ievada skaitli "num", bet pirms tam ar "integer" tiek noteikts, ka ievadītā informācija ir skaitlis.
check = int(input("Give me a number to divide by: ")) #Lietotājam ar funkciju input, jautā, lai viņš ievada skaitli ar ko dalīt "num", kā arī pirms funkcijas "input" tiek noteikts, ka ievadītā informācija būs skaitlis.

if num % 4 == 0:
    print(num, "is a multiple of 4")  #Tiek pārbaudīts vai lietotāja ievadītais skaitlis dalās ar 4, ja dalās tiek izvadīts teksts, ka viņa ievadītais skaitlis "num" ir skaitļa 4 reizinājums.
elif num % 2 == 0:
    print(num, "is an even number") #Tiek pārbaudīts vai lietotāja ievadītais skaitlis "num" ir pāra skaitlis, liekot programmai to mēģināt dalīt ar 2, ja ir pāra skaitlis, tad tiek izvadīts teksts, ka skaitlis "num" ir pāra skaitlis.
else:
    print(num, "is an odd number") #Ja skaitlis "num" nav pāra skaitlis, tiek izvadīts teksts, ka lietotāja skaitlis "num" ir nepāra skaitlis.

if num % check == 0:
    print(num, "divides evenly by", check) # Tiek pārbaudīts vai lietotāja ievadītais skaitlis "num", dalās ar viņa ievadīto skaitli "Check", ja dalās, tad tiek izvadīts teksts, ka lietotāja skaitlis "num" dalās ar skaitli "check".
else:
    print(num, "doesn't divide evenly by", check) #Ja skaitlis "num" nedalās ar skaitli "check", tad tiek izvadīts teksts, ka skaitlis "num" nedalās ar skaitli "check".

""" Method 2 """
num = int(input("Enter a number: ")) #Lietotājam tiek prasīts, lai viņš ievada citu skaitli "num", bet pirms tam ar "integer" tiek noteikts, ka ievadītā informācija būs skaitlis.
mod = num % 2 #Tiek pārbaudīts, vai lietotāja ievadītais skaitlis "num" ir pāra skaitlis.
if mod > 0:
    print("You picked an odd number.") #Ja ievadītais skaitlis "num" ir pāra skaitlis, tad tiek izvadīts teksts, ka ievadītais skaitlis "num" ir pāra skaitlis.
else:
    print("You picked an even number.") #ja ievadītais skaitlis "num" nav pāra skaitlis, tad teik izvadīts teksts, ka ievadītais skaitlis "num" ir nepāra skaitlis.
