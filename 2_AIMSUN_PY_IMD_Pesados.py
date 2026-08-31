################### 
#Script para crear un nuevo atributo en cada sección con la IMD de Pesados a partir de la H100
#Sustituir el valor de la línea 19: (IMDPES = count/0.07175) por el correspondiente de tu estación de referencia
###################


def getCreateAttribute():
	sectionType = model.getType ('GKSection')
	attribute = sectionType.addColumn ('GKSection::IMDPES','IMD de Pesados', GKColumn.Double)
	return attribute

def fillattribute(column):
	sectionType = model.getType ('GKSection')
	countColumn=model.getColumn('DYNAMIC::SRC_GKSection_count_159')
	for section in GK.GetObjectsOfType (sectionType) :
		countTS = section.getDataValueTS( countColumn )
		if countTS:
			count = countTS.getAggregatedValue()
			IMDPES=count/0.07175
			section.setDataValue(column, QVariant(IMDPES))
		else:
			continue
	
attribute = getCreateAttribute()
fillattribute(attribute)
print ('IMD de pesados calculado')
model.getCommander().addCommand(None)
