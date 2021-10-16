import shutil

path = input ("insert Path ") 

try :

	shutil.rmtree(path)
	print(f"{path} is in havean ;) ")

except :
	
	print("same error in process , try again ")

