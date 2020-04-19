<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Informe 
                <xsl:value-of select=
                "InformeFIM/InformacionGeneralFIM/DenominacionFondo"/>
                </h2>
                <td>Año Informe: <xsl:value-of select=
                "InformeFIM/InformacionGeneralFIM/DescripcionGeneral/
                AnoInforme"/>
                </td>
                <br/>
                <td>Divisa: <xsl:value-of select=
                "InformeFIM/InformacionGeneralFIM/DescripcionGeneral/
                Xcode_ISO4217.EUR"/>
                </td>
                <br/>
                <td>Calificación: <xsl:value-of select=
                "InformeFIM/InformacionGeneralFIM/RatingDepositario"/>
                </td>
                <br/>
                <td>Fecha de registro: <xsl:value-of select=
                "InformeFIM/DatosFondoCompartimentoFIM/FechaRegistroFondo"/>
                </td>
                <br/>
                <td>Perfil de riesgo: <xsl:value-of select=
                "InformeFIM/DatosFondoCompartimentoFIM/PoliticaDivisaFIM/
                CategoriaFIM/PerfilRiesgo"/>
                </td>
                <br/>
                <td>Política de inversión: <xsl:value-of select=
                "InformeFIM/DatosFondoCompartimentoFIM/PoliticaDivisaFIM/
                PoliticaInversion"/>
                </td>
                <br/>
                <td>Operativa en Derivados: <xsl:value-of select=
                "InformeFIM/DatosFondoCompartimentoFIM/PoliticaDivisaFIM/
                OperativaDerivados"/>
                </td>
                <br/>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>