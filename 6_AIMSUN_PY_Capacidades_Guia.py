################### 
#Script para crear un nuevo atributo en cada sección con la capacidad según la Guía de Nudos Viarios de la Orden Circular 32/2012. Tablas 4.6-M
###################


def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::Capacidad_guia","Capacidad_guia", GKColumn.String)
	return attribute


def fillattribute(column):
		sectionType = model.getType ("GKSection")
		for section in GK.GetObjectsOfType (sectionType) :
			
			SpeedLimColumn=model.getColumn('GKSection::speedAtt') 
			SpeedLim= section.getDataValueDouble(SpeedLimColumn)
			
			nbFullLanesColumn=model.getColumn("GKSection::nbFullLanesAtt")
			nbFullLanes=section.getDataValueInt(nbFullLanesColumn)
		

			if nbFullLanes == 1:
				if SpeedLim < 30.0:
					Capacidad_guia = "1800"
				elif 30.0 < SpeedLim < 51.0:
					Capacidad_guia = "1900"
				elif 51.0 < SpeedLim < 66.0:
					Capacidad_guia = "2000"
				elif 66.0 < SpeedLim < 81.0:
					Capacidad_guia = "2100"
				elif SpeedLim >= 82.0:
					Capacidad_guia = "2200"
			elif nbFullLanes > 1:
				if SpeedLim < 30.0:
					Capacidad_guia = 1600 * nbFullLanes
				elif 30.0 < SpeedLim < 51.0:
					Capacidad_guia = 1750 * nbFullLanes
				elif 51.0 < SpeedLim < 66.0:
					Capacidad_guia = 1900 * nbFullLanes
				elif 66.0 < SpeedLim < 81.0:
					Capacidad_guia = 2050 * nbFullLanes
				elif SpeedLim >= 82.0:
					Capacidad_guia = 2200 * nbFullLanes

			section.setDataValue(column, QVariant(Capacidad_guia))
			
	
attribute = getCreateAttribute()
fillattribute(attribute)
print ("Etiqueta lista")
model.getCommander().addCommand(None)
