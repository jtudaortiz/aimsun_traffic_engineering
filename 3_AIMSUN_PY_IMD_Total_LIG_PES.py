################### 
#Script para crear un nuevo atributo en cada sección con la IMD total como SUMA de la IMD de Ligeros + la IMD de pesados
#en lugar de calcularla directamente con los vehículos totales para evitar diferencias con el excel, que saca la IMD como suma. 
#Requiere calcular previamente los scripts "IMD de ligeros" e "IMD de pesados"
###################

def getCreateAttribute():
	sectionType = model.getType ("GKSection")
	attribute = sectionType.addColumn ("GKSection::IMDTOT","IMD Total", GKColumn.Double)
	return attribute


def fillattribute(column):
	sectionType = model.getType ('GKSection')
	countColumn_Lig=model.getColumn('DYNAMIC::SRC_GKSection_count_154')   #CAMBIAR "_154" POR EL TIPO DE VEH. Lig DEL MODELO
	countColumn_Pes=model.getColumn('DYNAMIC::SRC_GKSection_count_159')  #CAMBIAR "_159" POR EL TIPO DE VEH. Pes DEL MODELO

	for section in GK.GetObjectsOfType (sectionType) :
		countTS_Lig = section.getDataValueTS( countColumn_Lig )
		countTS_Pes = section.getDataValueTS( countColumn_Pes )
		if countTS_Lig and countTS_Pes:
			count_Lig = countTS_Lig.getAggregatedValue()
			IMDLIG=count_Lig/0.0806427		#CAMBIAR VALOR POR EL COEF. DE PASO DE IH100 de ligeros
			count_Pes = countTS_Pes.getAggregatedValue()
			IMDPES=count_Pes/0.07612377      #CAMBIAR VALOR POR EL COEF. DE PASO DE IH100 de Pesados
			
			IMDTOT=IMDLIG+IMDPES

			section.setDataValue(column, QVariant(IMDTOT))
		else:
			continue


attribute = getCreateAttribute()
fillattribute(attribute)
print ("IMD Total = Ligeros + Pesados Calculado")
model.getCommander().addCommand(None)
