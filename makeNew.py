import datetime
import hashlib
import base64
import os
import random
import base64
import gzip


def heroNameGen():
    heroNames = ["Dr G", "Matt Byers"]
    return random.choice(heroNames)


def goalNameGen():
    goalNames = ["Canvas account", "Lionpath account", "Angel account"]
    return random.choice(goalNames)


def giveRanLetter():
    letterArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                   "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return random.choice(letterArray)


def makeRanString(len):
    count = 0
    name = ''
    while (count < len):
        name += giveRanLetter()
        count += 1
    return name


def makePassword(len):
    count = 0
    passwordToreturn = ''
    while count < len:
        x = random.randint(0, 10)
        if (x <= 5):
            passwordToreturn += giveRanLetter()
        else:
            passwordToreturn += str(random.randint(0, 10))
        count += 1
    return passwordToreturn


def makeMe(desiredName):
    dirName = os.path.dirname(desiredName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

def makeOpener(levelName,stringToWrite):
    opener = stringToWrite
    makeMe("/home/" + levelName + "/README.txt")
    f = open("/home/" + levelName + "/README.txt", "w")
    f.write(opener)
    f.close()


def level0(paswardone,levelName):
    makeOpener(levelName, heroNameGen() + "'s password for their " + goalNameGen() + " is in inhere.txt\n")
    os.system("echo \"cat ~/README.txt\" >> /home/"+levelName+"/.bashrc")
    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w")
    g.write(paswardone)
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")


def level1(passwardTwo,levelName):
    opener = (
                heroNameGen() + "'s password for their " + goalNameGen() + " account is in inhere.txt but something is off, its hidden.\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    makeMe("/home/"+levelName+"/.inhere.txt")
    g = open("/home/"+levelName+"/.inhere.txt", "w")
    g.write(passwardTwo)
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/.inhere.txt;")


def level2(passwardThree,levelName):
    opener = (heroNameGen() + "'s password for their " + goalNameGen() + " is in the file that is only 9 bytes long\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    password_spot = random.randint(1, 9)
    count = 0
    while (count < 10):
        ran_fileName = makeRanString(8)
        makeMe("/home/"+levelName+"/" + ran_fileName)
        if count == password_spot:
            f = open("/home/"+levelName+"/" + ran_fileName, "w")
            f.write(passwardThree)
            f.close()
            os.system("chown "+levelName+":"+levelName+" \"/home/"+levelName+"/\"" + ran_fileName)
            count += 1
        else:
            string_len = random.randint(1, 50) + 25
            count2 = 0
            file_string = ""
            while count2 < string_len:
                file_string += giveRanLetter()
                count2 += 1

            makeMe("/home/"+levelName+"/" + ran_fileName)
            f = open("/home/"+levelName+"/" + ran_fileName, "w")
            f.write(file_string)
            f.close()
            os.system("chown "+levelName+":"+levelName+" \"/home/"+levelName+"/\"" + ran_fileName)
            count += 1


def level3(passwardFour,levelName):
    password_spot = random.randint(1, 256)
    count = 0
    while (count < 256):
        if count == password_spot:
            char1 = giveRanLetter()
            char2 = giveRanLetter()
            char3 = giveRanLetter()
            char4 = giveRanLetter()
            char5 = giveRanLetter()
            char6 = giveRanLetter()
            char7 = giveRanLetter()
            char8 = giveRanLetter()
            rand_pass = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + "      " + passwardFour
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(rand_pass)
            f.close()
            hint = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
            count += 1
        else:
            char1 = giveRanLetter()
            char2 = giveRanLetter()
            char3 = giveRanLetter()
            char4 = giveRanLetter()
            char5 = giveRanLetter()
            char6 = giveRanLetter()
            char7 = giveRanLetter()
            char8 = giveRanLetter()
            char9 = giveRanLetter()
            char10 = giveRanLetter()
            char11 = giveRanLetter()
            char12 = giveRanLetter()
            char13 = giveRanLetter()
            char14 = giveRanLetter()
            char15 = giveRanLetter()
            char16 = giveRanLetter()
            rand_pass = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + "      " + char9 + char10 + char11 + char12 + char13 + char14 + char15 + char16 + "\n"
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(rand_pass)
            count += 1
    opener = ("The password you seek is next to the line.... " + hint + "\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")


def level4(passwardFour,levelName):
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(
        heroNameGen() + "'s password for their " + goalNameGen() + " is next to the word you would find last when sorted alphabetically.\n")
    f.close()

    makeMe("/home/"+levelName+"/inhere.txt")
    f = open("/home/"+levelName+"/inhere.txt", "w")
    f.write("")
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")
    wordsSet = (
        " inside, jazz , moth , lamp , light , glass , mattress , pillow , television , whale , spoon , overt , grab , pull , delicate , obstruct , tendency , sore , cloth , redundant , staking , meek , implant , homely , plan , screw , motivate , stereo , typed , protective , lacking , verify , camp , wire , umbrella , eager , weight , competition , shed , irate , seat , scab , square , undo , bat , like , pot , land , watch , patch , ripe , eyes , rabid , brother , nondescript , use , retire , heal , infect , assert , calculating , versed , teeny , father , ashamed , occupy , boundless , reaction , mom , forbidden , dangle , concerned , fantastic , efficient , convict , sentence , glamorous , creator , cow , taking , glib , cruel , tedious , gain , say , wide-eyed , stranger , elbow , wax , beam , burly , order , behold , baseball , library , pollute , sassy , bread , war , slip , silent , fat , soft , unable , ducks , mellow , sophisticated , gag , shock , wealth , summer , stir , tire , replace , bring , vie , refuse , print , sit , nail , snack , sneeze , assorted , cracker , converge , psychedelic , co-operate , disturb , pray , hope , substance , nonchalant , capture , signal , fretful , consult , ubiquitous , output , thirsty , crayon , many , healthy , quit , expand , rail , wrench , under , stand , hold , late , pump , admit , vein , football , flowery , valuable , outrageous , fang , grind , secretary , rhetorical , love , observant , enlighten , lock , extend , reset , stitch , run , tremble , anxious , tourist , expensive , consort , stone , special , magic , justify , redo , exclaim , boiling , beggar , weapon , translate , dogs , fragile , cook , impossible , selection , insidious , cattle , envy , bright , teeth , scarf , polish , rich , clean , indulge , glow , nation , sponge , aloof , plod , tree , locket , match , tidy , stingy , rid , little , smelly , male , salute , cause , yawn , scan , question , hinder , pushy , hit , idolize , deserted , gun , husky , vacuous , tank , unequaled , sacrifice , remarkable , call , participate , talk , wrist , observe , zonked , weave , slink , cakes , tart , stick , recollect , crush , number , material , detach , hall , ultra , spoil , aboard , bray , curtain , lie , mold , enchanting , structure")
    words = wordsSet.split(",")
    random.shuffle(words)
    count = 0
    while (count < len(words)):
        char1 = giveRanLetter()
        char2 = giveRanLetter()
        char3 = giveRanLetter()
        char4 = giveRanLetter()
        char5 = giveRanLetter()
        char6 = giveRanLetter()
        char7 = giveRanLetter()
        char8 = giveRanLetter()

        if words[count] == " zonked ":
            ans = passwardFour
            f = open("/home/" + levelName + "/inhere.txt", "a")
            f.write(words[count] + "      " + ans)
            f.close()

        else:
            ans = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
            f = open("/home/"+levelName+"/inhere.txt", "a")
            f.write(words[count] + "      " + ans + '\n')
            f.close()

        count += 1
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")


def level5(passwardSix,levelName):
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(
        heroNameGen() + "'s password for their " + goalNameGen() + " is inside the file named inhere.txt\n")
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    password_spot1 = random.randint(1, 10)
    password_spot2 = random.randint(1, 10)
    password_spot3 = random.randint(1, 10)
    count = 0
    while (count < 10):
        char1 = giveRanLetter()
        char2 = giveRanLetter()
        char3 = giveRanLetter()
        char4 = giveRanLetter()
        char5 = giveRanLetter()
        char6 = giveRanLetter()
        char7 = giveRanLetter()
        char8 = giveRanLetter()

        rand_dir1 = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
        makeMe("/home/"+levelName+"/" + rand_dir1)
        count2 = 0
        while (count2 < 10):
            charr1 = giveRanLetter()
            charr2 = giveRanLetter()
            charr3 = giveRanLetter()
            charr4 = giveRanLetter()
            charr5 = giveRanLetter()
            charr6 = giveRanLetter()
            charr7 = giveRanLetter()
            charr8 = giveRanLetter()

            rand_dir2 = charr1 + charr2 + charr3 + charr4 + charr5 + charr6 + charr7 + charr8
            makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2)
            count3 = 0
            while (count3 < 10):
                if count == password_spot1 and count2 == password_spot2 and count3 == password_spot3:
                    makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/inhere.txt')
                    g = open("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/inhere.txt', "w")
                    g.write(passwardSix)
                    g.close()
                    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + "/inhere.txt;")
                else:
                    rand_file = makeRanString(8)

                    makeMe("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file)

                    g = open("/home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file, "w")
                    g.write(passwardSix)
                    g.close()
                    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/" + rand_dir1 + '/' + rand_dir2 + '/' + rand_file + ';')
                count3 += 1
            count2 += 1
        count += 1


def level6(passwardSeven,levelName):
    opener = (
                heroNameGen() + "'s password for their " + goalNameGen() + " is in the inhere.txt file, how ever they seem to have accidentally gzipped it. Can you help them?\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    makeMe("/home/"+levelName+"/inhere.txt")
    g = gzip.open("/home/"+levelName+"/inhere.txt.gz", "wb")
    g.write(passwardSeven.encode())
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt.gz;")


def level7(passwardEight,levelName):
    opener = (
                heroNameGen() + "'s password for their " + goalNameGen() + " is in the inhere.txt file, how ever they seem to have lost permission to read it\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w")
    g.write(passwardEight)
    g.close()
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere.txt;")
    os.system("chmod 333 /home/"+levelName+"/inhere.txt;")


def level8(passwordNine,levelName):
    passwordCount = random.randint(1, 255)
    opener = (
            heroNameGen() + "'s password for their " + goalNameGen() + " is in an unknown file. But they do believe the file had " + str(
        passwordCount) + " words. \n the password should be the last word in the file.\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    passwordSpot = random.randint(1, 10)
    i = 0
    while i <= 10:
        filName = makeRanString(8) + ".txt"
        makeMe("/home/"+levelName+"/" + filName)
        if i == passwordSpot:
            # now to generate the words-1
            x = 0
            toPut = ""
            while x < passwordCount - 1:
                toPut += makeRanString(8) + '\n'
                x += 1
            toPut += passwordNine
            f = open("/home/"+levelName+"/" + filName, "+w")
            f.write(toPut)
            f.close

        else:
            # now to generate the words-1
            x = 0
            toPut = ""
            numTOBe = random.randint(1, 255)
            if numTOBe == passwordCount:
                numTOBe += 1
            while x < numTOBe:
                toPut += makeRanString(8) + '\n'
                x += 1
            f = open("/home/"+levelName+"/" + filName, "+w")
            f.write(toPut)
            f.close
        i += 1


def level9(passwardTen,levelName):
    opener = (
            heroNameGen() + "'s password for their " + goalNameGen() + " account is in inhere.txt but something is off, its hidden.\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")
    g = open("/home/"+levelName+"/.in here.txt", "w+")
    g.write(passwardTen)
    g.close()


def level10(final,levelName):
    opener = (heroNameGen() + "'s password for their " + goalNameGen() + " is the only different word\n")
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")
    makeMe("/home/"+levelName+"/inhere1.txt")
    f = open("/home/"+levelName+"/inhere1.txt", "w")
    f.write('')
    f.close()
    makeMe("/home/"+levelName+"/inhere2.txt")
    f = open("/home/"+levelName+"/inhere2.txt", "w")
    f.write('')
    f.close()

    password_spot = random.randint(0, 256)
    count = 0
    while (count < 256):
        rand_pass = makeRanString(8) + '\n'
        f = open("/home/"+levelName+"/inhere1.txt", "a")
        if count == password_spot:
            f.write(final)
        else:
            f.write(rand_pass)
        f.close()
        f = open("/home/" +levelName+ "/inhere2.txt", "a")
        f.write(rand_pass)
        f.close()
        count += 1
    os.system("chown " +levelName+ ":" +levelName+ " /home/" +levelName+"/inhere1.txt;")
    os.system("chown "+levelName+":"+levelName+" /home/"+levelName+"/inhere2.txt;")


def level11(password,levelName):
    opener = heroNameGen() + " accidentally encoded their " + goalNameGen() + " password in base 64! They cant read whatever is in inhere.txt but maybe you can?\n"
    makeMe("/home/"+levelName+"/README.txt")
    f = open("/home/"+levelName+"/README.txt", "w+")
    f.write(opener)
    f.close()
    os.system("echo \"cat ~/README.txt\" >> /home/" + levelName + "/.bashrc")

    makeMe("/home/"+levelName+"/inhere.txt")
    g = open("/home/"+levelName+"/inhere.txt", "w+")
    g.write(str(base64.b64encode(password.encode("utf-8")), "utf-8") + '\n')
    g.close()

def level12(password,levelName):
    partOnePass = password[0:3]
    partTwoPass = password[4:7]
    levelhero = heroNameGen()
    makeMe("/home/"+levelName+"/Desktop/")
    makeMe("/home/"+levelName+"/Desktop/"+levelhero+"FamilyVacation")
    makeMe("/home/"+levelName+"/Documents")
    makeMe("/home/"+levelName+"/Downloads")
    makeMe("/home/"+levelName+"/Music")
    makeMe("/home/"+levelName+"/Pictures")
    makeMe("/home/"+levelName+"/Videos")

# now = datetime.datetime.now()
# print ("Current date and time as a unit")
# print (str(now))


# name = input("Please enter your PSU ID (abc1234):	")

print ("Setting up the levels now, please stand by...")

# “+levelName+”_5 = name + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
# print(“+levelName+”_5)
# hashed1_5 = hashlib.md5(“+levelName+”_5.encode('utf-8'))
# print (hashed1_5.digest)
# based1_5 = base64.b64encode(hashed1_5.digest())
# print (based1_5)
# passwordToFind = str(based1_5)
# paswardOne = passwordToFind[0:9]


key = makeRanString(8)+'\n'

delCounter = 0
while (delCounter <= 101):
    os.system("userdel level" + str(delCounter) + " --force --remove &> /dev/null")
    #"userdel level“+delCounter+” --force --remove"
    delCounter+=1



def makeLevelHome(levelPassword,levelName):
    os.system(
        "useradd "+ levelName +" --create-home --password \"$(openssl passwd -1 " + levelPassword + ")\" --shell /bin/bash --user-group")

def genRanLevel(nextLevelPassword,levelName):
    bigRan = random.randint(1,11)
    if bigRan == 1:
        level1(nextLevelPassword,levelName)
    if bigRan == 2:
        level2(nextLevelPassword,levelName)
    if bigRan == 3:
        level3(nextLevelPassword,levelName)
    if bigRan == 4:
        level4(nextLevelPassword,levelName)
    if bigRan == 5:
        level5(nextLevelPassword, levelName)
    if bigRan == 6:
        level6(nextLevelPassword, levelName)
    if bigRan == 7:
        level7(nextLevelPassword, levelName)
    if bigRan ==8:
        level8(nextLevelPassword,levelName)
    if bigRan ==9:
        level9(nextLevelPassword,levelName)
    if bigRan == 10:
        level10(nextLevelPassword,levelName)
    if bigRan == 11:
        level11(nextLevelPassword,levelName)


print("Making your levels now, please hold")

passwordToBe = makeRanString(8)+'\n'
makeLevelHome("level0","level0")
level0(passwordToBe,"level0")
makeLevelHome(passwordToBe,"level1")

passwordToBe = makeRanString(8)+'\n'
level1(passwordToBe,"level1")
makeLevelHome(passwordToBe,"level2")

passwordToBe = makeRanString(8)+'\n'
level2(passwordToBe,"level2")
makeLevelHome(passwordToBe,"level3")

passwordToBe = makeRanString(8)+'\n'
level3(passwordToBe,"level3")
makeLevelHome(passwordToBe,"level4")

passwordToBe = makeRanString(8)+'\n'
level4(passwordToBe,"level4")
makeLevelHome(passwordToBe,"level5")

passwordToBe = makeRanString(8)+'\n'
level5(passwordToBe,"level5")
makeLevelHome(passwordToBe,"level6")

passwordToBe = makeRanString(8)+'\n'
level6(passwordToBe,"level6")
makeLevelHome(passwordToBe,"level7")

passwordToBe = makeRanString(8)+'\n'
level7(passwordToBe,"level7")
makeLevelHome(passwordToBe,"level8")

passwordToBe = makeRanString(8)+'\n'
level8(passwordToBe,"level8")
makeLevelHome(passwordToBe,"level9")

passwordToBe = makeRanString(8)+'\n'
level9(passwordToBe,"level9")
makeLevelHome(passwordToBe,"level10")

passwordToBe = makeRanString(8)+'\n'
level10(passwordToBe,"level10")
makeLevelHome(passwordToBe,"level11")

passwordToBe = makeRanString(8)+'\n'
level11(passwordToBe,"level11")
makeLevelHome(passwordToBe,"level12")





levelCount = 12
while levelCount < 100:
    passwordToBe = makeRanString(8)+'\n'
    genRanLevel(passwordToBe,"level"+str(levelCount))
    levelCount += 1
    makeLevelHome(passwordToBe,"level"+str(levelCount))


print("The password to level 0 localhost is “level 0”")













