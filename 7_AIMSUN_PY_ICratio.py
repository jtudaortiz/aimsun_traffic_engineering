################### 
#Script para crear un nuevo atributo con el ratio I/C teniendo en cuenta la capacidad de la Guía de Nudos Viarios
###################

def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::ICratio","ICratio", GKColumn.Double)
	return attribute

def fillattribute(column):
	sectionType = model.getType ("GKSection")
	for section in GK.GetObjectsOfType (sectionType):
		
		countColumn=model.getColumn('DYNAMIC::SRC_GKSection_count_0')
		countTS = section.getDataValueTS( countColumn )

		CapGuiaColumn=model.getColumn("GKSection::Capacidad_guia")
		CapGuia=section.getDataValueDouble(CapGuiaColumn)
		
		if countTS:
			count=countTS.getAggregatedValue()
		
			ICratio = count / CapGuia
			section.setDataValue(column, QVariant(ICratio))

attribute = getCreateAttribute()
fillattribute(attribute)
print ("ICratio listo")
model.getCommander().addCommand(None)
