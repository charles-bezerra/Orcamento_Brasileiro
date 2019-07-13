#Charles Bezerra
#Silvio Carlos
#Julio Tavares
#Alisson Orlando
#orçamento 2016 a 2036
class Calculos:
            __teto = 0
            __anos = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036]
            __ano = None
            __percentual = 0.05
            __populacao = 0
            __orcamento_educacao = 0.0
            __orcamento_saude = 0.0
            __orcamento_previdencia = 0.0
            __orcamento_folha_P = 0.0
            __orcamento_abono_SD = 0.0
            __orcamento_beneficios = 0.0
            __orcamento_bolsa_familia = 0.0
            __inativos = 0.0
            __outros = 0.0
            def setTeto(self, valor):
                self.__teto = valor
            def setAno(self, ano):
                self.__ano = ano
            def getTeto(self):
                return self.__teto
            def getAno(self):
                return self.__ano
            def getAnos(self):
                return self.__anos
            def setPopulacao(self, populacao):
                self.__populacao = populacao
            def setOrcamento_Educacao(self, x):
                self.__orcamento_educacao = x
            def setOrcamento_Saude(self, x):
                self.__orcamento_saude = x
            def setOrcamento_Previdencia(self, x):
                self.__orcamento_previdencia = x
            def setOrcamento_Beneficios(self, x):
                self.__orcamento_beneficios = x
            def setOrcamento_Folha_P(self, x):
                self.__orcamento_folha_P = x
            def setOrcamento_Abono(self, x):
                self.__orcamento_beneficios = x
            def setOrcamento_bolsa_familia(self, x):
                self.__orcamento_bolsa_familia = x
            def setOrcamento_inativos(self, x):
                self.__inativos = x
            def setOrcamento_Outros(self, x):
                self.__outros = x
            def getNovo_Teto(self):
                cont = 0
                novo_teto = self.__teto
                result = 0
                try:
                    while True:
                        if self.__anos[cont] == self.__ano:
                            break;
                        cont = cont+1
                    for i in range(cont):
                            novo_teto = (novo_teto * self.__percentual) + novo_teto
                    return novo_teto
                except IndexError:
                    return "Error"

            def getTeto__Todos__Anos(self):
                aux = [0] * 21
                teto = self.__teto
                for i in range(len(aux)):
                    if i > 0:
                        teto = (self.__teto * self.__percentual) + teto
                    aux[i] = teto
                return aux
            def getOrcamento_Educacao(self):
                return  self.__orcamento_educacao * self.getNovo_Teto()
            def getOrcamento_Saude(self):
                return  self.__orcamento_saude * self.getNovo_Teto()
            def getOrcamento_Previdecia(self):
                return  self.__orcamento_previdencia * self.getNovo_Teto()
            def getOrcamento_Folha(self):
                return self.__orcamento_folha_P * self.getNovo_Teto()
            def getOrcamento_Abono(self):
                return self.__orcamento_abono_SD * self.getNovo_Teto()
            def getOrcamento_Beneficios(self):
                return self.__orcamento_beneficios * self.getNovo_Teto()
            def getOrcamento_Bolsa_Familia(self):
                return self.__orcamento_bolsa_familia * self.getNovo_Teto()
            def getOrcamento_Inativos(self):
                return self.__inativos * self.getNovo_Teto()
            def getOrcamento_Outros(self):
                return self.__outros * self.getNovo_Teto()
            def getVerificador(self):
                aux = (self.__orcamento_educacao + self.__orcamento_saude + self.__orcamento_folha_P + self.__orcamento_abono_SD +self.__orcamento_previdencia +self.__orcamento_beneficios + self.__orcamento_bolsa_familia + self.__outros + self.__inativos)
                if(aux > 1):
                     return 0
                elif(aux == 1.0 or aux == 1):
                     return 1
                else:
                     return 2
            def getCusto_Pessoa_Area(self, area):
                aux = (area/ self.__populacao)
                return aux
