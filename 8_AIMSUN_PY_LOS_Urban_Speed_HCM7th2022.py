
################### 
#Script para cr
###################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::UR_SPEED_LOS","LOS (Urbano - velocidad)", GKColumn.String)
	return attribute

def fillattribute(column):
	sectionType = model.getType ("GKSection")
	speed_col = model.getColumn("DYNAMIC::SRC_GKSection_speed_0") 
	speed_lim_col = model.getColumn("GKSection::speedAtt")

	for section in GK.GetObjectsOfType (sectionType) :
		
		speedTS = section.getDataValueTS(speed_col)
		if speedTS:
			speed = section.getDataValueTS(speed_col).getAggregatedValue() #getMin()  getMax(0)   getMean(0)
			speed_lim = section.getDataValueDouble(speed_lim_col)
			if (speed_lim == 80) and (speed > 64):
				UR_SPEED_LOS = "A" 
			elif (speed_lim == 80) and (speed > 55) and (speed <= 64):
				UR_SPEED_LOS = "B"
			elif (speed_lim == 80) and (speed > 40) and (speed <= 55):
				UR_SPEED_LOS = "C"
			elif (speed_lim == 80) and (speed > 32) and (speed <= 40):
				UR_SPEED_LOS = "D"
			elif (speed_lim == 80) and (speed > 24) and (speed <= 32):
				UR_SPEED_LOS = "E"
			elif (speed_lim == 80) and (speed <= 24) and (speed >= 0):
				UR_SPEED_LOS = "F"
			elif (speed_lim == 80) and (speed < 0):
				UR_SPEED_LOS = "A"	
			else:
			
				if (speed_lim == 70) and (speed > 56):
					UR_SPEED_LOS = "A" 
				elif (speed_lim == 70) and (speed > 47) and (speed <= 56):
					UR_SPEED_LOS = "B"
				elif (speed_lim == 70) and (speed > 36) and (speed <= 47):
					UR_SPEED_LOS = "C"
				elif (speed_lim == 70) and (speed > 28) and (speed <= 36):
					UR_SPEED_LOS = "D"
				elif (speed_lim == 70) and (speed > 22) and (speed <= 28):
					UR_SPEED_LOS = "E"
				elif (speed_lim == 70) and (speed <= 22) and (speed >= 0):
					UR_SPEED_LOS = "F"
				elif (speed_lim == 70) and (speed < 0):
					UR_SPEED_LOS = "A"	
				else:
					
					if (speed_lim == 60) and (speed > 48):
						UR_SPEED_LOS = "A" 
					elif (speed_lim == 60) and (speed > 40) and (speed <= 48):
						UR_SPEED_LOS = "B"
					elif (speed_lim == 60) and (speed > 31) and (speed <= 40):
						UR_SPEED_LOS = "C"
					elif (speed_lim == 60) and (speed > 25) and (speed <= 31):
						UR_SPEED_LOS = "D"
					elif (speed_lim == 60) and (speed > 19) and (speed <= 25):
						UR_SPEED_LOS = "E"
					elif (speed_lim == 60) and (speed <= 19) and (speed >= 0):
						UR_SPEED_LOS = "F"
					elif (speed_lim == 60) and (speed < 0):
						UR_SPEED_LOS = "A"
					else:

						if (speed_lim == 50) and (speed > 41):
							UR_SPEED_LOS = "A" 
						elif (speed_lim == 50) and (speed > 33) and (speed <= 41):
							UR_SPEED_LOS = "B"
						elif (speed_lim == 50) and (speed > 25) and (speed <= 33):
							UR_SPEED_LOS = "C"
						elif (speed_lim == 50) and (speed > 20) and (speed <= 25):
							UR_SPEED_LOS = "D"
						elif (speed_lim == 50) and (speed > 15) and (speed <= 20):
							UR_SPEED_LOS = "E"
						elif (speed_lim == 50) and (speed <= 15) and (speed >= 0):
							UR_SPEED_LOS = "F"
						elif (speed_lim == 50) and (speed < 0):
							UR_SPEED_LOS = "A"
						else:
				
							if (speed_lim == 40) and (speed > 32):
								UR_SPEED_LOS = "A" 
							elif (speed_lim == 40) and (speed > 27) and (speed <= 32):
								UR_SPEED_LOS = "B"
							elif (speed_lim == 40) and (speed > 21) and (speed <= 27):
								UR_SPEED_LOS = "C"
							elif (speed_lim == 40) and (speed > 16) and (speed <= 21):
								UR_SPEED_LOS = "D"
							elif (speed_lim == 40) and (speed > 13) and (speed <= 16):
								UR_SPEED_LOS = "E"
							elif (speed_lim == 40) and (speed <= 13) and (speed >= 0):
								UR_SPEED_LOS = "F"
							elif (speed_lim == 40) and (speed < 0):
								UR_SPEED_LOS = "A"
							else:
								UR_SPEED_LOS  = "Out of range"
						
			
			section.setDataValue(column, QVariant(UR_SPEED_LOS))
		else:
			continue
	
attribute = getCreateAttribute()
fillattribute(attribute)
print ("Urban Speed LOS calculado")
model.getCommander().addCommand(None)

