
################### 
#Script para crear un nuevo atributo en cada sección con el Nivel de Servicio (LOS) a partir del tiempo de demora/demora en segmento (s) de la via urbana

## Demora de cola DYNAMIC::SRC_GKSection_queueDelay_0

## Demora de parada DYNAMIC::SRC_GKSection_stoppedDelay_0
###################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute_2 = sectionType.addColumn ("GKSection::UR_CONDELAY_LOS","LOS (control_delay)", GKColumn.String)
	return attribute_2

def fillattribute(column):
	sectionType = model.getType ("GKSection")
	con_delay_col = model.getColumn("DYNAMIC::SRC_GKSection_segmentDelay_0") 
	
	for section in GK.GetObjectsOfType (sectionType) :
		
		con_delayTS = section.getDataValueTS(con_delay_col)
		if con_delayTS:

			con_delay = section.getDataValueTS(con_delay_col).getAggregatedValue()
							
			if (con_delay <= 10):
				CON_DELAY_LOS = "A" 
			elif (con_delay > 10) and (con_delay <= 15):
				CON_DELAY_LOS = "B"
			elif (con_delay  > 15) and (con_delay  <= 25):
				CON_DELAY_LOS = "C"
			elif (con_delay  > 25) and (con_delay  <= 35):
				CON_DELAY_LOS = "D"
			elif (con_delay  > 35) and (con_delay  <= 50):
				CON_DELAY_LOS = "E"
			elif (con_delay  > 50 ):
				CON_DELAY_LOS = "F"
			else:
				CON_DELAY_LOS  = "Out of range"
								
			section.setDataValue(column, QVariant(CON_DELAY_LOS))
		else:
			continue
	
attribute_2 = getCreateAttribute()
fillattribute(attribute_2)
print ("Demora de parada (control Delay) LOS calculado")
model.getCommander().addCommand(None)
