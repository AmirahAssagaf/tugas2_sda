#tipe data dictionary
nama={"mira":16,"adel":26,"suci":45}
itms=nama.items()
for i,j in itms:
    print(i,":",j)
#mengupdate
nama={"mira":16,"adel":26,"suci":45}
nama["mira"]=2
print(nama)

#menghapus
nama={"mira":16,"adel":26,"suci":45}
del nama ["mira"]
print(nama)
#menambah
nama={"mira":16,"adel":26,"suci":45}
nama["mamnun"]=66
print(nama)
    
