
################### 
#Script para crear una columna "LOS_Criterio" donde se establezca qué criterio aplicar para calcular el Nivel de Servicio (LOS) según el tipo de vía (por demora, por velocidad o por densidad)
###################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::LOS_criterio","LOS_Criterio", GKColumn.String)
	return attribute


				
		
attribute = getCreateAttribute()

print ("Atributo de critero LOS creado")
model.getCommander().addCommand(None)
