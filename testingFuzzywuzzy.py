from fuzzywuzzy import process

import doc2PJ
import modeleGN
from modeleGN import *
import doc2Intrigue
import lecteurGoogle
import sys

folderid = "1toM693dBuKl8OPMDmCkDix0z6xX9syjA"  # le folder des intrigues de Chalacta
folderSqueletteEmeric = "1hpo8HQ8GKjQG63Qm_QlEX7wQ58wZ9-Bw"
folderSqueletteJu = "17ii8P23nkyEk37MqFZKS3K9xohKDg0X7"
folderSqueletteCharles = "1uz_m0PEY8fxNFembqL7om3LMskE4e5Ee"


nomspersos = ["Anko Siwa", "Ashaya Asty", "Aved - 4V-3D", "Axel Brance", "Bynar Siwa", "Dall Joval D'rasnov",
              "Desnash Rhylee", "Dophine Rhue", "Driss Ranner", "Edrik Vance", "Greeta Asty", "Hart Do", "Havok",
              "Hog'Gemod Ippolruna", "Isayjja Kahl", "Jaldine Gerams", "Jay Mozel", "Jerima D'rasnov", "Jish Zyld",
              "Jory Asty", "Kael Sin", "Kalitt", "Kess Horoby", "Kianstev Nacram", "Korrgaarr Gguurd'k", "KR3-NC0",
              "Kyle Talus", "Kyrielle Viszla", "Lars Duskon", "Lexi Ipolruna", "Mano Tori", "Mina Tarkin",
              "Naka Kushir", "Naam Poorf", "Nemko Var", "Nexxar Graam", "NT 346/bredan", "Oni Lux", "Pregda Snorn",
              "Rhebanxx Kar", "Rika Sant", "Rimo Twil", "Saryth D'rasnov", "Seika Poorf", "Sirudan Bonte",
              "Slayke Jontab", "Sol Preeda - Soree", "Tarik Koma", "Teysa Cio", "Thuorn Hermon", "Timagua", "Trevek",
              "Tristan Wrenn", "Tsvan Kessig", "Val Krendel", "Valin​ Hess", "Vauber Brasell", "Wexley Ello",
              "Wor Monba", "Xabria", "Yulsa Nazdij", "Zaar Tamwi", "Zagrinn Vrask", "Zoln Ubri"]
nomsPNJs = ['Loomis Kent (éboueurs)', 'Agent tu BSI Mort à définir', 'Nosfran ?', 'Kelar Veil',
            'Un des joueurs de Sabbacc (nom à trouver)', 'Lady Santhe ??', 'Tranche Mitaines', 'Tranche Mitaines',
            'Jaarush Adan', 'L’inquisiteur', 'Clawool', 'Yerraz', 'Droïdes mercenaires',
            'Quay Tolsite, agent des Pykes', 'FX-4', 'Oskrabkosi', 'Loomis Xent', 'Katlyn Clawwool', 'Tranche mitaines',
            'Rebelle 1',
            'Boh Pragg chef de gare Kel dor Et Teezk un esclave rodien issu de la purge du cartel Rodien par Tagge',
            'Nekma', 'Katlyn Clawool', 'Benjey Doroat', 'Droïde syndiqué', 'Seerdo', 'Sid Kashan', 'Nosfran Ratspik',
            'Membres du J.A.N', 'Caleadr Schlon', 'Zuckuss (ou Boush, ou une autre star)', 'B2B', 'Haaris',
            'Le fils de Kalitt', 'Trewek', 'Revos Vannak', 'Inquisiteurice', 'Varima', 'Eliana Zorn', 'Zev Jessk',
            'Katlyn Clawool', 'Mohadarr Bodfre', 'Ex esclave', 'Inquisiteur', 'XXXX Rhylee', 'Rak Stryn  le mandalo',
            'Yerraz le go faster', 'Apprenti de l’Inquisiteur', 'Témoin X', 'XXX Geska (frère de wirt)',
            'Fraterr Millbra', 'Izzik Walo’s', 'Katlyn Clawool', 'Rosson & Yorshill', 'Rebelle 3', 'Drashk',
            'Baron Soontir Fel', 'esclave porcher, sbire de Hogg', 'Osrabkosi', '5ème frère',
            'La mère (Suwan) et la soeur (Ilanni) de Lexi', 'Darsha Viel', 'Jarus Adams (star tour)', 'Muic Wula',
            'Rebelle 2', 'Nosfran ?', 'O-MR1', 'Katleen Clawool', 'Varina Leech', 'Kalie Hess (Décédée)',
            'Boba Fett (ou un mandalorien bien badass de l’enfer)', 'OMR-1', 'Lieira Sonn', 'esclave 1',
            'Bossk (ou un trando qui le représente)', 'Soontir Fel', 'FX4', 'Trerlil Irgann',
            'Khaljab Welall, agent de l’Aube Ecarlate', 'Inquisiteur : 5ème frère', 'Shaani']





def main():
    sys.setrecursionlimit(5000) #mis en place pour prévenir pickle de planter
    # todo charger les relations depuis le tableau des relations
    # todo faire en sorte que si on force une intrigue(singletest)  elle est automatiquement traitée / updatée

    monGN = GN(folderIntriguesID=folderid,
               folderPJID=[folderSqueletteJu, folderSqueletteEmeric, folderSqueletteCharles])


    for pnj in nomsPNJs:
        monGN.dictPNJs[pnj] = Personnage(nom=nomsPNJs, pj=EST_PNJ_HORS_JEU)

    # si on veut charger un fichier
    # monGN = GN.load("archive Chalacta")
 #todo refaire une passe sur la fconction de personnages entre ceux qui sont importés et les autres : limiter les versions ne processantone
    apiDrive, apiDoc = lecteurGoogle.creerLecteursGoogleAPIs()
    # doc2Intrigue.extraireIntrigues(monGN, apiDrive=apiDrive, apiDoc=apiDoc, singletest="-01")
    doc2PJ.extrairePJs(monGN, apiDrive=apiDrive, apiDoc=apiDoc, singletest="-01")

    ajouterPersosSansFiche(monGN)
#todo : quand on cherche les joueurs, chercher aussi les "joueuses"
    monGN.rebuildLinks(verbal=False)
    monGN.save("archive Chalacta")
#todo : ajouter un wanrning quand on a moins de persos dans une scene qu'il n'y en avait au début > ca veutsurement dire que le perso n'est pas dans le tableau récap// marche aussi pour le nombre de cars est trop petit
    print("****************************")
    print("****************************")
    print("****************************")
    # #écrit toutes les scènes qui sont dans le GN, sans ordre particulier
    dumpAllScenes(monGN)

#todo comprendre pourquoi les PNJs ont un plein lot de roles qui leurs sont affectés (ex : intrigue 40)

    ## pour avoir tous les objets du jeu :
    # generecsvobjets(monGN)

    # squelettePerso(monGN, "Kyle Talus")
    # listerRolesPerso(monGN, "Kyle Talus")
    # listerPNJs(monGN)
    # genererCsvPNJs(monGN)
    # genererCsvObjets(monGN)

    # #lister les correspondaces entre les roles et les noms standards
    # mesroles = tousLesRoles(monGN)
    # fuzzyWuzzyme(mesroles, nomspersos)

    # # print(normaliserNomsPNJs(monGN))
    # #génération d'un premier tableau de noms de PNJs à partir de ce qu'on lit dans les intrigues
    # nomsPNSnormalisés = normaliserNomsPNJs(monGN)
    # print([ nomsPNSnormalisés[k][0] for k in nomsPNSnormalisés])

    # print(getAllRole(GN))

    # afficherLesPersos(monGN)
    # afficherDatesScenes(monGN)
    # genererCsvOrgaIntrigue(monGN)
    # listerLesRoles(monGN)
    # del monGN.intrigues['1gf3VUIophPUIgu6EPmubO0kPiOwAx9-3DacvVEfAgiw']
    # listerDatesIntrigues(monGN)

    ## test de la fonction d'effaçage'
    # testEffacerIntrigue(monGN)

    # print(" l'intrigue la plus ancienne est {0}, c'est {1}, maj : {2}".format(monGN.idOldestUpdate, monGN.intrigues[monGN.idOldestUpdate], monGN.oldestUpdate))

    # test de la focntion de rapprochement des PNJs
    # fuzzyWuzzyme(listerPNJs(monGN), nomsPNJs)

    # #test de la focntion de lecture des PJs
    # dumpPersosLus(monGN)
    # dumpSortedPersos(monGN)


def ajouterPersosSansFiche(monGN):
    print("début de l'ajout des personnages sans fiche")
    nomsLus = [x.nom for x in monGN.dictPJs.values()]
    #pour chaque perso de ma liste :
    # SI son nom est dans les persos > ne rien faire
    #SINON, lui créer une coquille vide
    persosSansCorrespondance=[]
    for perso in nomspersos:
        if perso in nomsLus:
            print(f"le personnage {perso} a une correspondance dans les persos lus")
        else:
            persosSansCorrespondance.append(
                [perso,
                 process.extractOne(perso, nomsLus)[0],
                 process.extractOne(perso, nomsLus)[1]])
            #todo : si processone >= 75 >> on adapte, sinon on crée
            monGN.dictPJs[perso] = Personnage(nom=perso, pj=EST_PJ) #on met son nom en clef pour se souvenir qu'il a été généré

    print(persosSansCorrespondance)
    for perso in persosSansCorrespondance:
        print(perso)
    print("fin de l'ajout des personnages sans fiche")

def testEffacerIntrigue(monGN):
    listerRolesPerso(monGN, "Kyle Talus")
    monGN.intrigues["1p5ndWGUb3uCJ1iSSkPpHrDAzwY8iBdK8Lf9CLpP9Diw"].clear()
    del monGN.intrigues["1p5ndWGUb3uCJ1iSSkPpHrDAzwY8iBdK8Lf9CLpP9Diw"]
    print("J'ai effacé l'intrigue Rox et Rouky")
    listerRolesPerso(monGN, "Kyle Talus")


def afficherLesPersos(monGN):
    for intrigue in monGN.intrigues:
        # print("propriétaire intrigue : {0} : {1}".format(intrigue.nom, intrigue.orgaReferent))
        # for clef in intrigue.roles.keys():
        #     print(clef + " a pour nom complet : " + str(intrigue.roles[clef].nom))

        for role in intrigue.roles.values():
            print("pour le rôle " + role.nom)
            print("Personnage : " + role.perso.nom)
            texteScenes = ""
            for scene in role.scenes:
                texteScenes += scene.titre + "; "
            print("scenes : " + texteScenes)


def afficherDatesScenes(monGN):
    for intrigue in monGN.intrigues:
        for scene in intrigue.scenes:
            print("scène : {0} / date : {1} > {2}".format(scene.titre, scene.date, scene.getFormattedDate()))


def genererCsvOrgaIntrigue(monGN):
    for intrigue in monGN.intrigues:
        print("{0};{1}".format(intrigue.nom, intrigue.orgaReferent))


def listerLesRoles(monGN):
    for intrigue in monGN.intrigues:
        print(f"intrigue : {intrigue.nom} - url : {intrigue.url}")
        for role in intrigue.roles.values():
            print(str(role))


def listerDatesIntrigues(monGN):
    for intrigue in monGN.intrigues.values():
        print("{0} - {1} - {2}".format(intrigue.nom, intrigue.lastChange, intrigue.url))


def listerRolesPerso(monGN, nomPerso):
    nomPerso = process.extractOne(nomPerso, nomspersos)[0]
    for role in monGN.dictPJs[nomPerso].roles:
        print("Role : {0}".format(role))


def squelettePerso(monGN, nomPerso):
    mesScenes = dict()
    nomPerso = process.extractOne(nomPerso, nomspersos)[0]
    for role in monGN.dictPJs[nomPerso].roles:
        for scene in role.scenes:
            mesScenes[str(scene.getLongdigitsDate())] = scene

    for key in sorted([str(x) for x in mesScenes.keys()], reverse=True):
        print(
            f"date : {mesScenes[key].getFormattedDate()} ({mesScenes[key].date}) : {mesScenes[key].titre} dans {mesScenes[key].intrigue.nom}")
        print(f"{mesScenes[key].description}")


def listerPNJs(monGN):
    toReturn = []
    for intrigue in monGN.intrigues.values():
        for role in intrigue.roles.values():
            if role.estUnPNJ():
                print(role)
                toReturn.append(role.nom)
    return toReturn


def genererCsvPNJs(monGN):
    print("nomRole;description;typePJ;niveau implication;details intervention;intrigue")
    for intrigue in monGN.intrigues.values():
        for role in intrigue.roles.values():
            if role.estUnPNJ():
                nompnj = role.nom.replace('\n', chr(10))
                description = role.description.replace('\n', "***")
                niveauImplication = role.niveauImplication.replace('\n', chr(10))
                perimetreIntervention = role.perimetreIntervention.replace('\n', chr(10))
                print(f"{nompnj};"
                      f"{description};"
                      f"{stringTypePJ(role.pj)};"
                      f"{niveauImplication};"
                      f"{perimetreIntervention};"
                      f"{intrigue.nom}")


def genererCsvObjets(monGN):
    print("description;Avec FX?;FX;Débute Où?;fourni par Qui?;utilisé où?")
    for intrigue in monGN.intrigues.values():
        for objet in intrigue.objets:
            description = objet.description.replace('\n', "***")
            avecfx = objet.rfid
            fx = objet.specialEffect.replace('\n', "***")
            debuteou = objet.emplacementDebut.replace('\n', "***")
            fournipar = objet.fourniParJoueur.replace('\n', "***")
            utiliseou = [x.nom for x in objet.inIntrigues]
            print(f"{description};"
                  f"{avecfx};"
                  f"{fx};"
                  f"{debuteou};"
                  f"{fournipar};"
                  f"{utiliseou}")


def tousLesRoles(monGN):
    tousLesRoles = []
    print(f"dernière modification GN : {monGN.oldestUpdate}/{monGN.intrigues[monGN.oldestUpdatedIntrigue]}")
    for intrigue in monGN.intrigues.values():
        for role in intrigue.roles.values():
            if not modeleGN.estUnPNJ(role.pj) and role.pj != EST_REROLL:
                tousLesRoles.append(role.nom)
        # print(f"date dernière MAJ {intrigue.dateModification}")
    return tousLesRoles


def fuzzyWuzzyme(input, choices):
    # input.sort()
    toReturn = []
    input = set(input)
    for element in input:
        # scores = process.extract(element, choices, limit=5)
        scores = process.extractOne(element, choices)
        toReturn.append([element, scores[0], scores[1]])
    toReturn.sort(key=lambda x: x[2])

    for element in toReturn:
        print(f"fuzzy : {element}")


def normaliserNomsPNJs(monGN):
    nomsPNJs = []
    nomsNormalises = dict()
    for intrigue in monGN.intrigues.values():
        for role in intrigue.roles.values():
            if role.estUnPNJ():
                nomsPNJs.append(role.nom)
    nomsPNJs = list(set(nomsPNJs))
    print("Nom D'origine ;Meilleur choix;Confiance")
    for i in range(len(nomsPNJs)):
        choices = process.extract(nomsPNJs[i], nomsPNJs, limit=2)
        print(f"{choices[0][0]};{choices[1][0]};{choices[1][1]}")

        # le premier choix sera toujours de 100, vu qu'il se sera trouvé lui-même
        # si le second choix est > 90 il y a de fortes chances qu'on ait le même perso
        # sinon on ne prend pas de risques et on garde le meme perso
        if choices[1][1] > 90:
            nomsNormalises[nomsPNJs[i]] = [choices[1][0], choices[1][1]]
        else:
            nomsNormalises[nomsPNJs[i]] = [choices[0][0], choices[0][1]]

    return nomsNormalises

def generecsvobjets(monGn):
    for intrigue in monGn.intrigues.values():
        for objet in intrigue.objets:
            print(f"{intrigue.nom};{intrigue.orgaReferent};{objet.description};{objet.fourniParJoueur};{objet.fourniParJoueur};{objet.rfid};{objet.specialEffect};")


def dumpPersosLus(monGN):
    for pj in monGN.dictPJs.values():
        # if pj.url != "":
            print(pj)

def dumpSortedPersos(monGN):
    tousLesPersos = [x.nom for x in monGN.dictPJs.values()]
    tousLesPersos.sort()
    print(tousLesPersos)
    print(len(tousLesPersos))
    print(len(nomspersos))


def dumpAllScenes(monGN):
    for intrigue in monGN.intrigues.values():
        print(f"{str(intrigue)}")
        print(f" a {len(intrigue.scenes)} scenes")

        mesScenes = dict()
        for scene in intrigue.scenes:
            # print(scene.titre)
            # print(scene.getFormattedDate())
            # print(scene)

            mesScenes[str(scene.getLongdigitsDate())] = scene

        for key in sorted([str(x) for x in mesScenes.keys()], reverse=True):
            print(mesScenes[key])


main()
