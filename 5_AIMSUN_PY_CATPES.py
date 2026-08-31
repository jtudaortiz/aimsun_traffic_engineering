###################
#Script para crear un nuevo atributo para cada sección con la categoría de tráfico en función de la IMDp
#Se necesita calcular previamente la IMDp de pesados mediante la Script "Categoría de Pesados - IMDp" ya que ésta crea un atributo necesario
####################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::CATPES","Cat T Pesado", GKColumn.String)
	return attribute


def fillattribute(column):
	sectionType = model.getType ("GKSection")
	for section in GK.GetObjectsOfType (sectionType):

		IMDpColumn=model.getColumn("GKSection::IMDp")
		IMDp=section.getDataValueDouble(IMDpColumn)

		if IMDp<25.0:
			CATPES= "T42"
		elif 25.0 < IMDp <49.999:
			CATPES="T41"
		elif 50.0 < IMDp <99.999:
			CATPES="T32"
		elif 100.0 < IMDp <199.999:
			CATPES="T31"
		elif 200.0 < IMDp <799.999:
			CATPES="T2"
		elif 800.0 < IMDp <1999.999:
			CATPES="T1"
		elif 2000.0 < IMDp <3999.999:
			CATPES="T0"
		else:
			CATPES="T00"

		section.setDataValue(column, QVariant(CATPES))

	
attribute = getCreateAttribute()
fillattribute(attribute)
print ("Etiqueta lista")
model.getCommander().addCommand(None)
