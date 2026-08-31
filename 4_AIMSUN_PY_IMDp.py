###################
#Script para crear un nuevo atributo para cada sección con la IMDp en función del número de carriles
#Se necesita calcular previamente la IMD de pesados mediante la Script "IMD de Pesados" ya que ésta crea un atributo necesario
####################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::IMDp","IMDp", GKColumn.Double)
	return attribute


def fillattribute(column):
	sectionType = model.getType ("GKSection")
	for section in GK.GetObjectsOfType (sectionType):

		nbFullLanesColumn=model.getColumn("GKSection::nbFullLanesAtt")
		nbFullLanes=section.getDataValueInt(nbFullLanesColumn)

		IMDPESColumn=model.getColumn("GKSection::IMDPES")
		IMDPES=section.getDataValueDouble(IMDPESColumn)

		if nbFullLanes<3.0:
			IMDp= IMDPES
		else: 
			IMDp=IMDPES*0.85
		section.setDataValue(column, QVariant(IMDp))


	
attribute = getCreateAttribute()
fillattribute(attribute)
print ("IMDp listo")
model.getCommander().addCommand(None)
