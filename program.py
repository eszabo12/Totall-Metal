# A program to hopefully change the names of the Store Procedures
# By Elle Szabo

from datetime import datetime


class StoreProcedure():
	#name attribute should contain the .txt extension
	def __init__(countList = [], name = None, self):
		#The number of Store Procedures contained in the store procedure that lead to another ifle
		self.countList = countList
		self.name = name
	def __str__():
		return self.name
	def writeToFile(self):
		# number of times an item in countList occurs
		countSP = 0
		countList = []
		# opens the original store procedure file with "read"
		origFile = open(self.name, "r")
		for line in origFile:
			# the line that contains the first reliable instance of its name
			if "CREATE PROCEDURE" in line or "ALTER PROCEDURE" in line:
				# splits the line in order to isolate name
				lineList = line.split(".[")
				#gets rid of bracket at end of name
				newString = lineList[1].replace("]","")
				# removes whitespace
				newString = newString.strip()
				fileName = newString
				# changes name to new, Java name
				newName = self.changeName(fileName)
				# uncomment to error check
				# print(fileName)
				# print(newName)
		origFile.close()
		# this is the file the store procedure will be converted to
		newFile = open(newName + ".txt", "w")
		# opens the original file again because it can only be looped through once
		origFile = open(self.name, "r")
		for line in origFile:
			# takes the number of times SP_ occurs and subtracts the number of times the filename (which starts with _SP) occurs
			countSP += line.count("SP_") - str.count(fileName)
			if countSP > 0:
				# splits by whitespace
				lineList = line.split()
				for item in lineList:
					# if the specific chunk of the line is the non-name store procedure, add it to the list
					if "SP_" in item and not fileName in item:
						countList.append(item)
			# indicates which line to change  the author
			if "Author" in line or "Created by" in line or "Creator" in line:
				lineList = line.split(":")
				# puts my name into the file
				lineList[1] = "  Elle"
				newLine = ":".join(lineList)
				# for this line, replaces old name with new  name
				newLine = newLine.replace(fileName, newName)
			# indicates which linehad the  date
			elif "Created" in line or "Create date" in line or "Created date" in line:
				lineList = line.split(":")
				# inserts the current date
				lineList[1] = str(datetime.now().strftime("%x"))
				newLine = ":".join(lineList)
				newLine = newLine.replace(fileName, newName)
			else:
				newLine = line.replace(fileName, newName)
			# using the changed newLine variables, writes the current line to the new file
			newFile.write(newLine)
		origFile.close()
		newFile.close()
		return countList
	# changes the SQL name to Java name guided by conventions my mentor told me
	def changeName(self):
		newName = ""
		# indicates universally used SP
		if "_Com_" in fileName:
			fileType = "Com"
		# A specific form
		elif "_Frm_" in fileName:
			fileType = "Pgm"
		# a report
		elif "_Rpt_" in fileName:
			fileType = "Rpt"
		fileList = fileName.split("_")
		# SP -> JSP
		fileList[0] = "JSP"
		fileList[1] = fileType
		# Adds Jpgm to main name
		newString = "Jpgm" + fileList[2]
		fileList[2] = newString
		# removes redundancy of Form
		if "Frm" in fileList[2]:
			fileList[3].replace("Frm", "")
		# if the name is not Com or Form, it will have only 3 items
		if len(fileList) >= 4:
			# adds control to longer namex
			if "Ctrl" not in fileName:
				fileList.insert(4, "Ctrl")
		# loops through the name list by item
		for index in range(len(fileList)-1):
			# deletes slt-- no longer using that word
			if "Slt" in fileList[index]:
				del fileList[index]
		# patches the name back together again
		newName = "_".join(fileList)
		return newName

def main():
	origFile = StoreProcedure("SP_Frm_Freight_Outgoing_Slt_WriteOff.txt")

main()