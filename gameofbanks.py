import time
import colorama
from colorama import Back
colorama.init(autoreset=True)

print( 'Üdvözöllek! Kérlek válassz az alábbiak közül : játék, történet, csapat\n')

triangles = '1045'
var = '1175'
name_input_ = 'adam cholk'
game = 'játék'
history = 'történet'
team = 'csapat'
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
nom = 'oc'
imv = 2340000001 #india_money_value
bacon = 'CODEFORMONEY'
base64 = 'KEYFORTHESUCCESS'
ww2 = '1939-1945'
door_math = '3699'
osi = 'open systems interconnection'
binary = 'BinaryEncryption'
binary2 = 'Open'
rot13 = 'SuccessfullyDecodedRot13'
saw = ('jobb, jobb, bal, jobb, bal, bal')
door1 = '4664'
door2 = '1'
door3 = 'benjamin franklin'
laser = 'Open'
rich = 'melléknév'
ftp = 'ftp'
emailpass = 'CHOCOLATECOOKIE'
adminssh = 'ssh jack@123.123.123.12'
adminpass = 'ServerSideAccessKey'
regularssh1 = 'ssh adam@333.333.3.33'
regularssh2 = 'ssh taylor@333.333.3.33'
regularssh3 = 'ssh jack@333.333.3.33'
regularssh4 = 'ssh daniel@333.333.3.33'
regularssh5 = 'ssh cholk@333.333.3.33'
regularssh6 = 'ssh damn@333.333.3.33'
regularssh7 = 'ssh tommy@333.333.3.33'
regularpass = 'Asd123asD'
anonymepass = 'SSHAnonymeAccess'
maingatepass = 'MainGateAccess'
anonymessh = 'ssh tommy@321.321.321.21'



mainuinput = input('Válassz: ')



while mainuinput.lower() == game or history or team:


	if mainuinput.lower() == game:
		print('Üdvözöllek a játékban, Adam Cholk ! Kérlek válassz az lehetőségek közül: 1, 2, 3\n')
		print(Back.GREEN +'1 Bank of America ( ~$2.16 trillion ) (expert)')
		print(Back.GREEN +'2 Bank of Budapest ( ~$44.66 billion  ) (medium)')
		print(Back.GREEN +'3 Bank of India ( ~$2.34 billion ) (easy)')
		bankuinput = input('\nVálassz: ')
		while bankuinput.lower() == three or two or one:
			if bankuinput == three:
				print('\nHol és hogyan szeretnél bemenni ?')
				print('1 Főbejárat (ügyfélként) ')
				print('2 vészkijárat')
				print('3 szemétlerakó helyiség')
				optuinput = input('\nVálassz: ') #options_user_input

				while optuinput.lower() == one or two or three:
					if optuinput.lower() == one:				
						print('\nElindultál egy ügyintéző felé, de az egyik őr kissé szokatlannak talált téged és végig téged bámúl. Mit fogsz tenni ?')
						print('1 tovább megyek ')
						print('2 meggondolom magamat és elhagyom a bank területét')
						finbuinput = input('\nVálassz: ') #first_in_bank_user_input

						while finbuinput.lower() == one or two:
							if finbuinput.lower() == one:
								print('(ügyintéző) -Szép napot, miben segíthetek ?')
								print('(te) -Üdvözlöm, pénzt szeretnék felvenni! ')
								print('(ügyintéző) -Rendben, kérem töltse ki a papiron lévő adatokat a pénzfelvételhez!\n')


								while True:
									nameinput=input('Név: ')
									if nameinput.lower() == name_input_:
										print('\n(costumer)Ellenőriztettem az adatait, megerősítették, hogy lehetséges a pénzfelvétel !\n'
											  ' Mennyit szeretne igényelni ?')
										money_value_input = int(float(input('Összeg: ')))
										while money_value_input != int(float(imv)):
											if money_value_input <= int(float(imv)): #nem lehet az érték 2340000001
												time.sleep(.5)
												print('\nRendben, kérem kövessen !\n')
												print('Mivel kétely merül fel benned az ügyintézővel kapcsolatban, ezért két gondolat is megfordul a fejedben, melyet véghez is vihetsz.\n')
												print('1 félúton leütod az ügyintézőt, elveszed a kulcsokat, majd elmész a széfhez.')
												print('2 követed és megvárod amíg megérkeztek a széfhez.\n')
												kinput = input('Válassz: ')#knock_input
												while kinput == one or two:
													if kinput == one:
														print('\nKirály, megvannak a kulcsok és a széfhez vezető utat is megtaláltad, de mi lesz a leütött személlyel ?')
														print('1 viszed magaddal túszként')
														print('2 elrejted ')
														hoinput = input('Válassz: ')#hostage_input
														while hoinput == one or two:
															if hoinput == one:
																print('\nElértetek a széfhez és kitudtad nyitni, most próbáld megfejteni a kódot a végső ajtóhoz!')
																print('A kód : AAABAABBABAAABBAABAAAABABABBABBAAAAABABBABBABABBAAAABAABABBA')
																winput = input('Megoldás: ')
																while winput != '<>#<>#':
																	if winput == bacon:
																		print(Back.GREEN +'Gratulálok, megfejtetted a kódot, most fogd és vidd pénzt :)')
																		time.sleep(10)
																		exit()

																	elif winput != bacon:
																		print("Helytelen, próbáld újra!")
																		winput=input('\nMegoldás: ')


															if hoinput == two:
																print('\nSajnos észrevette egy arra járőröző őr és értesítette a rendőrséget a tudtadon kivűl, ezáltal elkaptak és lecsuktak. ~10 év börtönt kaptál :/')
																time.sleep(10)
																exit()

															else:# hoinput != one or two:
																print("Sajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: 1, 2")
																hoinput=input('\nVálassz: ')

													if kinput == two:
														print('Elérkeztetek a széfhez, de az ügyintéző megpróbálja értesíteni az őrséget. Mit teszel?')
														print('1 kimenekülsz a bankból és meghúzod magad')
														print('2 megakadályozod ezt és túszként viszed tovább')
														ainput = input('Válassz: ')
														while ainput == one or two:
															if ainput == one:
																print('Sikeresen elmenekültél, de hónapokkal késöbb elkaptak.')
																time.sleep(10)
																exit()

															if ainput == two:
																print('Siker, elértetek széfhez és senki se tud az incidensről. Megtudod fejteni a jelkódot ?')
																print('Kód: S0VZRk9SVEhFU1VDQ0VTUw== ')
																b64inp = input('Megoldás: ')
																while b64inp != '>#&>#&':
																	if b64inp == base64:
																		print(Back.GREEN + 'Gratulálok, megfejtetted a kódot, most fogd és vidd pénzt :)')
																		exit()

																	elif b64inp != base64:
																		print("Helytelen, próbáld újra!")
																		winput=input('\nMegoldás: ')


															elif ainput != one or two:
																print('Sajnos nem értem ezt a parancsot ! Kérlek válassz az alábbiak közül: 1, 2')
																ainput = input('Válassz: ')


													elif kinput != one or two:
														print("Sajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: 1, 2")
														kinput=input('\nVálassz: ')


											elif money_value_input >= int(float(imv)):
												print('Helytelen összeget adtál meg ! Elérhető mennyiség: 2.34 Milliárd')
												money_value_input=int(float(input('Összeg: ')))

									else:
										print(Back.RED + 'Error')


							elif finbuinput.lower() == two:
								print(Back.RED + 'Vesztettél ! :(')
								time.sleep(5)
								quit()
								

							elif finbuinput != one or two:
								print("Sajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: 1, 2")
								finbuinput = input('\nVálassz: ')  # first_in_bank_user_input

					if optuinput.lower() == two:
						print('\nVigyázz ! Óvatosan bánj ezekkel az ajtókkal, bármelyik percben beriaszthatnak, az egyik ajtón van egy jelszó olvasó. Mi lehet ennek a kódja?')
						print('Kód: 253+638−62×1+346=')

						while True:
							ansinp=input('Megoldás: ')
							if ansinp == var:
								print('\nKirály, bentvagy, most szerezd meg a széfkulcsokat. A menedzsernél találod őket.')
								print('A lépcsőn lemenve elötted áll a menedzser, mit csinálsz vele? Vigyázz,mert tartja a kapcsolatot az őrökkel!\n')
								print('1 Túszként magaddal viszed és megengeded neki a kommunikációt időközönként.')
								print('2 Leütöd és elviszed a kulcsokat\n')
								maninp = input('Válassz: ')
								while maninp == one or two:
									if maninp == one:
										print('\nNem volt a legjobb ötlet, felébredt és a tudtatod kivül értesítette az őrséget,'+ Back.RED +'lebuktál.')
										time.sleep(10)
										exit()
									if maninp == two:
										print('\nMi lesz az emberrel?\n')
										print('1 elrejted')
										print('2 magaddal viszed\n')
										man2inp = input('Válassz: ')
										while man2inp == one or two:
											if man2inp == one:
												print('Hmmm, érdekes. Te tudod :)')
												print('Elértetek a széfhez de biztonsági kérdéssel védik.')
												print('A kérdés így hangzik: Mettől meddig tartott a második világháború? (beviteli forma: <év>-<év>\n')
												while True:
													ww2inp = input('Válasz: ')
													if ww2inp == ww2:
														print(Back.GREEN + 'Szép volt, most fogd és vidd a pénzt :)')
														time.sleep(10)
														exit()
													else:
														print('Helytelen a válaszod, próbáld újra!')


											if man2inp == two:
												print('Sajnos ez nagy hiba volt, nem voltál elég figyelmes és nem vetted észre amikor magához tért. Elfutott és szólt az őröknek. Börtönbe kerültél. ')
												time.sleep(10)
												exit()
												
											else:
												print('Nem értem ezt a parancsot, válassz az alábbiakból: 1, 2')
												man2inp=input('Válassz: ')


									else:
										print('Nem értem ezt a parancsot, válassz az alábbiakból: 1, 2')
										maninp=input('Válassz: ')

							else:# ansinp != var:
								print('Helytelen az értéked, próbáld újra !')




					if optuinput.lower() == three:
						print('\nNos mivel ez egy elég picike bank, nem gondoltak nagyon a biztonságra, így eléggé közel vagy a széfhez.')
						print('Elhagyva találtál egy kulcsot. Magaddal viszed és megpróbálod vele kinyitni a letétes fiókokat?')
						print('1 igen')
						print('2 nem\n')

						while True:
							yon=input('Válassz: ')
							if yon == one:
								print(Back.GREEN + 'Gratulálok a jó kulcsot hoztad el, bár ezzel nem lesz akkora nyereséged mint a széffel, de szép volt ! :)')
								time.sleep(10)
								exit()
							if yon == two:
								print('Ez esetben menj tovább és probálj bejutni a széfhez.')
								time.sleep(.5)
								print('\nEz sikerült is, de mi lehet a széf kódja ?')
								print('feladvány = Határozd meg az alábbi derékszögű háromszögek hiányzó oldalait! \na=6cm, b=8cm, c=?\na=3cm, c=5cm, b=?\nc=13cm, b=12cm, a=?\n(egybe írd a számokat! pl: 0000)\n')

								while True:
									triinpt=input('Megoldás: ')
									if triinpt == triangles:
										print(Back.GREEN + 'Gratulálok, ügyes vagy ! Itt a pénz :)')
										time.sleep(10)
										exit()
									else:
										print('Helytelen a számkód, próbáld újra!')

							elif yon != one or two:
								print('Nem értem ezt a parancsot, válassz az alábbiakból: 1, 2')



					elif optuinput.lower() != one or two or three:
						print("Sajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: 1, 2, 3")
						optuinput = input('Válassz: ')



			if bankuinput.lower() == two:
				print('\nHol és hogyan szeretnél bemenni ?')
				print('1 Éjjel a tetőn keresztűl')
				print('2 Csatornák felől')
				print('3 Irodák felől')
				optuinput=input('\nVálassz: ')  # options_user_input
				while optuinput.lower()==one or two or three:
					if optuinput.lower()==one:
						print('Nehéz dolgot lesz, ugyanis éjjel mozgásérzékelő lézerek vannak a széf közelében. A tetőn át merre mész tovább ?')
						print('1 Leereszkedsz egy kötéllel')
						print('2 Átvágod az egyik ablakot')
						print('3 Vészkijáratot keresel, mert megijedtél, majd elmész')
						onroof_inpt=input('Válassz: ')
						while onroof_inpt.lower()!=one or two or three:
							if onroof_inpt.lower()==one:
								print('\nÓvatosan, eléggé feltünő egy kötél a bank a közepén, nem gondolod ? Mit csinálsz a továbbiakban a kötéllel ?')
								print('1 Otthagyod')
								print('2 Viszed magaddal\n')
								rope_inpt=input('Válassz: ')
								while rope_inpt.lower()==one or two:
									if rope_inpt==one:
										print('\nSajnos ez nem volt a legokosabb döntés, egy arra felé járkáló őr észrevette és értesítette a rendőrséget. Börtönbe kerültél')
										time.sleep(10)
										exit()

									if rope_inpt.lower()==two:
										print('Remek ötlet. Miután lementél a lépcsőn találtál egy ajtót rajta egy számzáras lakattal, ideje kinyitni. Mi lehet a kódja?')

										while True:
											dmath_inpt=input('5432 - 2345 + 234 - (-2) + 376 = ')  # door_math(3699)
											if dmath_inpt.lower()==door_math:
												print('Szuper bejutottál a kamera szobába, nem kell többet aggódnod a kamerák miatt. \nA folyósó végén van egy lift és egy ajtó, melyiket használod ?')
												print('1 Lift')
												print('2 Ajtó')
												de_inpt=input('Válassz: ')
												while de_inpt==one or two:
													if de_inpt==one:
														print('Miért nem gondoltál arra, hogy feltűnik az őröknek ha valaki használja a liftet? Sajnos lebuktál...')

													if de_inpt==two:
														print('Fenébe biztonsági kérdés védi, megtudod oldani ?')
														print('\n Mit jelent az alábbi rövidítés: OSI\n')
														print('Formátum: <szó> <szó> <szó>')

														while True:
															osi_inpt=input('Megoldás: ')
															if osi_inpt.lower()==osi:
																print('Ügyes vagy, haladj tovább, már majdnem ott vagy a széfnél.')
																time.sleep(3)
																print('Meg is érkeztél, de még elötted egy számzáras ajtó, emlékszel még a legelső számzár kódjára ? :)')

																while True:
																	ans_inpt=input('Válasz: ')
																	if ans_inpt==door_math:
																		print('Gratulálok, már csak a széf maradt hátra. Eléggé nehéznek tűnik a kód megfejtése, de én bízok benned ! Mit jelenthet ez a számsorozat ?')
																		print('\n 01000010 01101001 01101110 01100001 01110010 01111001 01000101 01101110 01100011 01110010 01111001 01110000 01110100 01101001 01101111 01101110')

																		while True:
																			bina_inpt=input('Megoldás: ')
																			if bina_inpt==binary:
																				print('Gratulálok, sikeresn bejutottál a széfbe. Itt rengeteg pénz és arany vár arra, hogy megutaztassák őket :)')
																				time.sleep(10)
																				exit()

																			else:
																				print('Helyeteln, próbáld újra !')

																	else:
																		print('Helytelen próbáld újra !')

															else:
																print('Helytelen próbáld újra !')

											else:
												print('Helytelen az értéked, próbáld újra !')


									else:
										print('Sajnos ezt az utasítást nem értem, kérlek válassz az alábbiak közül: 1, 2')
										rope_inpt=input('\nVálassz: ')

							if onroof_inpt.lower()==two:
								print('Bejutottál a bank épületébe, de vigyázz, mert rengteg kamera van ami észrevehet téged !')
								time.sleep(3)
								print('Miután sikeresen a földszintre értél, (találtál) egy ajtót. Megprobálod megfejteni a kódját vagy tovább haladsz?')
								print('1 Megpróbálom')
								print('2 Tovább megyek')
								next_inpt=input('Válassz: ')
								while next_inpt==one or two:
									if next_inpt==one:
										time.sleep(3)
										print('Sajnálatodra ez egy amolyan "honeypot" volt, beriasztott a rendszer és lebuktál...')
										time.sleep(10)
										exit()

									if next_inpt==two:
										print('Jól válaszotottál, hisz az az ajtó egy csapda volt !')
										time.sleep(5)
										print('Kis kutakodás után meglett a széf, mi lehet a kódja ? Próbáld meg megfejteni !')
										print('FhpprffshyylQrpbqrqEbg13')
										while True:
											rot_inpt=input('Megoldás: ')
											if rot_inpt==rot13:
												print('ügyes vagy megfejtetted, nyertél ! :)')
												time.sleep(5)
												exit()

											else:
												print('Helytelen próbáld újra !')

							if onroof_inpt==three:
								print('Vége a játéknak...(béna vagy :P)')
								time.sleep(5)
								exit()

							else:
								print('Sajnos nem értem, válassz az alábbi lehetőségek közül: 1, 2, 3')

					if optuinput.lower()==two:
						print(
							'Elindultál a csatornák felé, de sajnos levannak zárva, válassz egy másik útvonalat vagy próbáld meg átvágni!')
						print('2 megpróbálom átvágni')
						canal_inpt=input('Válassz: ')
						while canal_inpt==two:
							if canal_inpt==two:
								print('Ahhoz, hogy sikeresen átvágd, írd be az alábbi mozdulatokat: jobb, jobb, bal, jobb, bal, bal')
								print('formátum =<mozdulat>, <mozdulat>')

								while True:
									move_inpt=input('Mozdulatok: ')
									if move_inpt.lower()==saw:
										time.sleep(3)
										print('Sikeresen átvágtad!')
										print('Most három ajtónyira vagy a széftől, de ezeket az ajtókat kódok illetve kérdések védik + van egy lézer a 2. ajtó után\n')
										print('1. ajtó kódja : 222*222*2/2+2-222')  # 4664

										while True:
											dr1_inpt=input(' Megoldás: ')
											if dr1_inpt==door1:
												print('Helyes !\n')
												print('2. ajtó kérdése: Van 12 szénkupacom bal oldalon meg 42 szénkupac jobboldalon ha ezeket összetolom hány kupacot kapok ?')

												while True:
													dr2_inpt=input('Megoldás: ')
													if dr2_inpt.lower()==door2:
														print('Ügyes vagy !\n')
														print('Lézer kioldásához fejtsd meg : 01101111 01110000 01100101 01101110 ')  # Open
														while True:
															bina2=input('Megoldás: ')
															if bina2==binary2:
																print('Gratulálok, már csak 1 ajtó maradt hátra !')
																print('3. ajtó és egyben az utolsó is : Melyik személy található a 100$-os bankjegyen ?')  # Benjamin Franklin
																while True:
																	bill=input('Válasz: ')
																	if bill.lower()==door3:
																		print('Gratulálok már csak a széf maradt hátra: Mi a szófaja az alábbi szónak? : gazdag')

																		while True:
																			word_inpt=input('Megoldás: ')
																			if word_inpt.lower()==rich:
																				print('Sikeresen megoldottad a feladványokat és megszerezted a pénzt, boldog életed lett :)')
																				time.sleep(10)
																				exit()

																			else:
																				print('Helytelen, próbáld újra !')


																	else:
																		print('Sajnos nem jó, próbáld újra !')

															else:
																print('Helytelen próbáld újra !')

													else:
														print('Helytelen, próbáld újra !')

											else:
												print('Helytelen, próbáld újra !')

									else:
										print(
											'Helytelen mozdulatokat végeztél vagy rossz értéket adtál meg, próbáld újra !')




							else:
								print('Sajnos nem értem, válassz az alábbi lehetőség közül: 1')

					if optuinput.lower()==three:
						print('A hátsó lépcsőn felmész beöltözve irodai alkalmazottként, bemenve egy biztonságiőr áll előtted, hogy igazold magad. Szerencsére meglátod a hónap dolgozója feliratot, így tudsz rá hivatkozni, hogy ismered.')
						print('1 hivatkozol az alkalmazottra')
						print('2 nem hivatkozol az alkalmazottra')
						office_inpt = input('Válassz: ')
						while office_inpt == one or two:
							if office_inpt == one:
								print('Itt Elfogadja az ismerettséged és továbbenged az irodák felé, ahol ahhoz az alkalmazotthoz vezet.')
								print(' Az alkalmazott megkérdezi ki vagy, emiatt pánikba esel és elgondolkodsz, hogy fegyvert rátasz-e vagy.')
								print('1 fegyvert rántasz')
								print('2 Megpróbálod magad kimagyarázni')
								inoff_inpt = input('Válassz: ')
								while inoff_inpt == one or two:
									if inoff_inpt == one:
										print('Az őrt leütöd hirtelen mozdulattal, majd a fegyverét elkobozva túszul ejted a hónap alkalmazottját,\n'
											  ' ezzel a magas prioritású emberrel sikeresen kinyitod a széfet és ellopod a pénzt.')
										time.sleep(10)
										exit()


									if inoff_inpt == two:
										print('Sajnos nem sikerül kimagyarázni igy elkapnak és 10 év börtönt kapsz hivatalos személynek való kiadás miatt.')
										time.sleep(10)
										exit()


									elif inoff_inpt != one or two:
										print('Sajnos nem értem válassz az alábbiak közül: 1, 2')

							if office_inpt == two:
								print('Kitessékel, és sajnos nem tudod folytantni a rablást. (küldetés sikertelen.)')
								time.sleep(10)
								exit()

							elif office_inpt != one or two:
								print('Sajnos nem értem, kérlek válassz az alábbiak közül: 1, 2')
								office_inpt=input('Válassz: ')

					else:
						print('Sajnos ezt az utasítást nem értem, kérlek válassz az alábbiak közül: 1, 2, 3')
						optuinput=input('\nVálassz: ')  # options_user_input

			if bankuinput == one:
				print(
					' Ez a világ egyik leggazdagabb bankja, ha ezt választottad nem lesz egyszerü dolgod.\n Ahhoz, hogy sikeresen véghezz vidd a feladatot már nem elég a fizikai behatolás, egy hacker szerepébe kell lépned. Sok sikert !')

				print('Elvállalod?')

				print('1 vállalod')
				print('2 nem vállalod')
				accept_inpt=input('Válassz: ')
				while accept_inpt==one or two:
					if accept_inpt==one:
						print(
							'Kis kutakodás után találtál egy-két érdekes dolgot. \nEgy nyitott 21-es portra bukkansz, mert nemrég volt rendszer frissítés és elfelejtették zárni, elrejteni. Milyen szolgáltatás fut ezen ?')
						while True:
							ftp_inpt=input('Válasz: ')
							if ftp_inpt==ftp:
								print(
									'Igen, jól tudod, ezen egy ftp szerver fut amin találtál néhány érdekes információt. \nMegtudtad, hogy van egy egy file amiben található egy email cím és egy titkositott jelszó páros. \nNem lenne rossz ötlet ha utánna néznél ezeknek, kitudja még miket találsz. \n(nyugodtan lépj be az email-be és mindenbe amit ott találsz!)')
								print('email: twitterforgameofbanksamerica@gmail.com')
								print('jelszó: -.-. .... --- -.-. --- .-.. .- - . -.-. --- --- -.- .. .')
								while True:
									mail=input('Mi volt a jelszó: ')
									if mail==emailpass:
										print('Remek, most keresgélj egy picit tovább :)')
										time.sleep(5)
										print(
											'Kis keresgélés után találsz egy nyitott 22-es portot, ezen egy SSH server fut, ez lehet az admin oldal. \nCsatlakozz rá és nézd meg miket találsz rajta. \n(ne külön terminálban probálkozz, mert úgy nem fog müködni :D)')

										while True:
											admin=str(input('Csatlakozás: '))
											if admin==adminssh:

												while True:
													admin_ssh_pass=str(input('Jelszó: '))

													if admin_ssh_pass==adminpass:
														print(
															'Bent is vagy, most nézzük, hogy mik vannak fent a szerveren !')
														time.sleep(3)
														print('1 utalási rendszer SSH ip címe (anonyme)')
														time.sleep(1)
														print('2 utalási rendszer SSH ip címe (regular)')
														time.sleep(1)
														print('3 alkalmazottak listája')
														time.sleep(1)
														print('4 nyitási/zárási időpontok')
														time.sleep(1)
														print('5 !!!FONTOS!!! :)')

														select_in_ssh=input('Válassz: ')
														while select_in_ssh==one or two or three or four or five:
															if select_in_ssh==one:
																print('ip: 321.321.321.21')
																print('------------------------------------------')
																while True:
																	anonyme=str(input('Csatlakozás: '))
																	if anonyme==anonymessh:

																		while True:
																			anonyme_ssh_pass=str(input('Jelszó: '))

																			if anonyme_ssh_pass==anonymepass:
																				print(
																					'Bejutottál az utalási rendszerbe, de szükség lesz a megerősítésnél a "main gate access" kódra !\n')

																				print('utalás:')
																				time.sleep(1)
																				print(
																					'-kezdeményezett neve: ------------')
																				time.sleep(1)
																				print(
																					'-kezdeményezett bankszámlaszáma: 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc')
																				time.sleep(1)
																				print('-utalás dátuma: XXXX-XX-XX')
																				time.sleep(1)
																				print('-utalandó összeg: $750.500.000')

																				while True:
																					anonyme_ssh_transacc=str(
																						input('megerősítési jelszó: '))

																					if anonyme_ssh_transacc==maingatepass:
																						time.sleep(3)
																						print('Sikeres tranzakció !\n')
																						time.sleep(5)
																						print(
																							'Gratulálok sikeresen elutaltad a pénzt és a mai napig nem tudja senkise, hogy ki tette ^^)')
																						time.sleep(10)
																						exit()

																					else:
																						print(
																							'Helytelen jelszó, probáld újra!')

																			else:
																				print('Helytelen jelszó')
																	else:
																		print(
																			'Helytelen formátumot használtál, probáld újra !')

															if select_in_ssh==two:
																print('ip: 333.333.3.33')
																print('------------------------------------------')
																while True:
																	regular=str(input('Csatlakozás: '))
																	if regular==regularssh1 or regularssh2 or regularssh3 or regularssh4 or regularssh5 or regularssh6 or regularssh7:

																		while True:
																			regular_ssh_pass=str(input('Jelszó: '))

																			if regular_ssh_pass==regularpass:
																				print(
																					'Bejutottál az utalási rendszerbe !\n')

																				print('utalás:')
																				time.sleep(1)
																				print('-kezdeményezett neve: Jack Hosh')
																				time.sleep(1)
																				print(
																					'-kezdeményezett bankszámlaszáma: 1173333333-22222221')
																				time.sleep(1)
																				print('-utalás dátuma: 2021-03-5')
																				time.sleep(1)
																				print('-utalandó összeg: $750.500.000')

																				while True:
																					regular_ssh_transacc=str(
																						input('megerősítési jelszó: '))

																					if regular_ssh_transacc==regularpass:
																						time.sleep(3)
																						print('Sikeres tranzakció !\n')
																						time.sleep(5)
																						print(
																							'Egy pár hétig nem találtak meg téged, de a végén rád bukkantak az utalás alapján, börtönbe kerültél... Vesztettél ! :/')
																						time.sleep(10)
																						exit()

																					else:
																						print(
																							'Helytelen jelszó, probáld újra!')

																			else:
																				print('Helytelen jelszó')
																	else:
																		print(
																			'Helytelen formátumot használtál, probáld újra !')

															if select_in_ssh==three:
																print(' -George Adam\n'
																	  '-Great Taylor\n'
																	  '-Viral Jack\n'
																	  '-Foiry Daniel\n'
																	  '-Adam Cholk\n'
																	  '-Big Damn\n'
																	  '-Klofer Tommy\n')

															if select_in_ssh==four:
																print(' H: 7:00-21:00\n'
																	  'K: 7:00-21:00\n'
																	  'Sz:7:00-21:00\n '
																	  'Cs:7:00-21:00\n'
																	  'P: 7:00-21:00\n'
																	  'Sz: zárva\n'
																	  'V:  zárva')

															if select_in_ssh==five:
																print(
																	'Hát ezt nem kellett volna választani, ez egy "honepot" volt mely egyből lezárta a rendszert, így sikertelenné vált az akciód :(')
																time.sleep(10)
																exit()

															elif select_in_ssh!=one or two or three or four or five:
																print(
																	'Nem értem ezt a parancsot, kérlek az alábbiak közül válassz: 1, 2, 3, 4, 5')


													else:
														print('Helytelen probáld újra !')
											else:
												print('Helytelen formátum, probáld újra !')

									else:
										print('Helytelen, probáld újra !')
							else:
								print('Helytelen, probáld újra !')

					if accept_inpt==two:
						print('Ebben az esetben sikertelen az akciód...')
						time.sleep(5)
						exit()

					elif accept_inpt!=one or two:
						print('Nem értem ezt az utasítást ! Válassz az alábbiakból : 1, 2')
						accept_inpt=input('Válassz: ')



			elif bankuinput.lower() != one or two or three:
				print("Sajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: 1, 2, 3")
				bankuinput = input('Válassz: ')

	if mainuinput.lower() == history:
		print(' Nem mindig éltem így, régen volt rendes munkám.\n Viszont egy ponton minden megváltozott.\n'
			  ' A főnököm elbocsátott, hisz felvettek a helyemre külföldi munkásokat, fele annyiért.\n'
			  ' Elkezdtem eladósodni, és a kiutat kerestem, majd találkoztam egy kedves úriemberrel, aki azt mondta, hogy van számomra egy munkája.\n'
			  ' Elmondta, mit is kéne csinálni, csak elvinni A-ból B-be egy csomagot.\n'
			  ' Könnyűnek tűnt, úgyhogy elvállaltam.\n'
			  ' Azóta is bánom, hisz akadt egy kis gond, a végét kiderült, hogy a csóka a Szerb maffiának dolgozik.\n'
			  ' Minden a lehető legrosszabb irányban sült el.\n Pénzt követeltek a szállítmányért, amit nem tudtam megadni.\n'
			  '\nElhatároztam, hogy kirablok egy bankot, hogy visszafizethessem azt amivel nem is tartozok, a családom és saját érdekemben.\n')
		print('\nKérlek válassz az alábbiak közül : játék, történet, csapat')
		mainuinput = input('Válassz: ')
	

	if mainuinput.lower() == team:
		print('\nCsapatnév: Good Game')
		print('Játéknév: Game of Banks')
		print('Csapattagok: Szilléry Szabolcs, Szász Csaba, Holecska Dániel, Petz Dávid, Pótz-Nagy Ábel')
		print('Alkalmazott technikák: Python')
		print('\nKérlek válassz az alábbiak közül : játék, történet, csapat')
		mainuinput = input('Válassz: ')

	elif mainuinput.lower() != game or history or team:
		print("\nSajnos ezt a parancsot nem értem ! Kérlek válassz az alábbi lehetőségek közül: játék, történet, csapat")
		mainuinput = input('\nVálassz: ')
