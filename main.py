from calculos import Calculos
def procedimento():
	try:
		teto = int(input("Digite o teto de 2016: "))
		ano = int(input("Digite o ano de reajuste: "))
		habitantes = int(input("Digite o numero de abitantes do Brasil: "))
		print("""
			========================
				Resultado
			========================
			""")
		a = Calculos()
		a.setTeto(teto)
		a.setAno(ano)
		a.setPopulacao(habitantes)
		print("Teto atual >>> ", a.getNovo_Teto())
		print("Custo pessoa para o pais >>> ", a.getCusto_Pessoa_Area(a.getNovo_Teto()))
		print("____________________________________________________")
		x = a.getAnos()
		y = a.getTeto__Todos__Anos()
		for i in range(21):
			print("Ano: ", x[i], "Teto correspondente: ", y[i])
		print("""
			     ==========================================
				Digite as porcentagens de cada area
					do forma to: 0.05
			     ==========================================
		      """)
		educacao = float(input("Educação: "))
		saude = float(input("Saúde: "))
		previdencia = float(input("Previdência: "))
		folha = float(input("Folha de Pagamento: "))
		abono = float(input("Abono: "))
		beneficios = float(input("Beneficius: "))
		bolsa_familia = float(input("Bolsa Familia: "))
		inativos = float(input("Inativos: "))
		outros = float(input("Outros: "))
		a.setOrcamento_Educacao(educacao)
		a.setOrcamento_Saude(saude)
		a.setOrcamento_Previdencia(previdencia)
		a.setOrcamento_Folha_P(folha)
		a.setOrcamento_Abono(abono)
		a.setOrcamento_Beneficios(beneficios)
		a.setOrcamento_bolsa_familia(bolsa_familia)
		a.setOrcamento_inativos(inativos)
		a.setOrcamento_Outros(outros)
		if a.getVerificador() == 1 or a.getVerificador() == 2:
			print("_______________________________________________")
			print("Destinado a Educação: ", a.getOrcamento_Educacao() )
			print("Destinado a Saúde: ", a.getOrcamento_Saude() )
			print("Destinado a Previdencia: ", a.getOrcamento_Previdecia())
			print("Destinado a Folha: ", a.getOrcamento_Folha())
			print("Destinado a Abono: ", a.getOrcamento_Abono() )
			print("Destinado a Beneficios: ", a.getOrcamento_Beneficios())
			print("Destinado ao Bolsa Familia: ", a.getOrcamento_Bolsa_Familia())
			print("Destinado a Inativos: ", a.getOrcamento_Inativos())
			print("Destinado a Outros: ", a.getOrcamento_Inativos())
			resp = input("Você deseja saber quanto você custa para cada area do pais? [S/n]")
			if resp == "S" or resp == "s" or resp == "sim" or resp == "SIM" or resp == "sim":
				print("__________________________________________________")
				print("Seu custo para Educação: ", a.getCusto_Pessoa_Area(a.getOrcamento_Educacao()))
				print("Seu custo para Saúde: ", a.getCusto_Pessoa_Area(a.getOrcamento_Saude()) )
				print("Seu custo para Previdencia: ", a.getCusto_Pessoa_Area(a.getOrcamento_Previdecia()))
				print("Seu custo para Folha: ", a.getCusto_Pessoa_Area(a.getOrcamento_Folha()))
				print("Seu custo para Abono: ", a.getCusto_Pessoa_Area(a.getOrcamento_Abono()) )
				print("Seu custo para Beneficios: ", a.getCusto_Pessoa_Area(a.getOrcamento_Beneficios()))
				print("Seu custo para Bolsa Familia: ", a.getCusto_Pessoa_Area(a.getOrcamento_Bolsa_Familia()))
				print("Seu custo para Inativos: ", a.getCusto_Pessoa_Area(a.getOrcamento_Inativos()))
				print("Seu custo para Outros: ", a.getCusto_Pessoa_Area(a.getOrcamento_Inativos()))
		else:
			print("Voçê digitou porcentagens que correspondem mais do que 100%")
			print("""
				Reiniciando
			      """)
			procedimento()
	except ValueError:
		print("!!!Por favor somente digitar numeros e nao outros caracteres!!!")
		print("""
			Reiniciando
		      """)
		procedimento()
	except IndexError:
		print("!!!Por favor so informa anos entre 2016 a 2036!!!")
		print("""
			Reiniciando
			      """)
		procedimento()
	except TypeError:
		print("!!!Por favor somente digitar numeros e nao outros caracteres e anos entre 2016 a 2036 !!!")
		print("""
			Reiniciando
			      """)
		procedimento()
	except ZeroDivisionError:
		print("!!!Você digitou zero como divisor, isso acasiona um valor fora dos numeros reais!!!")
		print("""
			Reiniciando
			      """)
		procedimento()
	except:
		print("Error desconhecido")
		print("""
			Reiniciando
			      """)
		procedimento()
procedimento()
