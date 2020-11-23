import pandas as pd

inputtxt = "C:/Users/maxem/Desktop/e_20111031.txt"
outputtxt = "C:/Users/maxem/Desktop/pesée.txt"

#input file
#"inputtxt = open("data.txt", "rt")
#output 
#outputtxt = open("out.txt", "wt")
#for each line in the input file
#for line in fin:
	#read replace the string and write to output file
	#fout.write(line.replace('pyton', 'python'))
#close input and output files
#fin.close()
#fout.close()

file_name = "C:/Users/maxem/Desktop/bdtest.xlsx"
sheet =  "Feuil1"# sheet name or sheet number or list of sheet numbers and names

df = pd.read_excel(io=file_name, sheet_name=sheet)
a = [(df.head(5))]
print(a)  # print first 5 rows of the dataframe