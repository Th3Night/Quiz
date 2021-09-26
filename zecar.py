a = "encrypted_string"

alph = "а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я, а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я"
alph = alph.split(", ")

print(alph)

for i in range(30):
    copy = []
    for l in range(len(a)):
        copy.append("")

    for j in range(len(copy)):
            copy[j] = alph[alph.index(a[j]) + i]

    print("".join(copy))
