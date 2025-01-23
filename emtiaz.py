jam_se_emtiaz = 0
jam_yek_emtiaz = 0
c=0
for i in range(30):
    emtiaz = int(input())
    if emtiaz == 3:
        c+=1
        jam_se_emtiaz = jam_se_emtiaz + emtiaz
    elif emtiaz == 1:
        jam_yek_emtiaz = jam_yek_emtiaz + emtiaz
jame_kol = jam_yek_emtiaz + jam_se_emtiaz
print(jame_kol,c)