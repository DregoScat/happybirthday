from flask import Flask, render_template, send_from_directory, request
import os
import subprocess

app = Flask(__name__)
small = "qwertyuiopasdfghjklzxcvbnm"
big="QWERTYUIOPASDFGHJKLZXCVBNM"
check = True
numbers = ["1","2","3","4","5","6","7","8", "9", "0"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","+","=", "/", "\\", "|", "_", "~"]
drinks = ["soda", "limonade", "juice", "water"]
roman = ["I", "V", "X", "C", "M"]
vnuk = ["VLAD", "VLADYSLAV"]
translation = {
    "I":"1",
    "V":"5",
    "X":"10",
    "C":"100",
    "M":"1000",

}
number = 0


@app.route('/styles/<path:filename>')
def styles(filename):
    font_dir = os.path.join(os.getcwd(), 'styles')  # Шлях до теки з шрифтами
    return send_from_directory(font_dir, filename)


@app.route('/images/<path:filename>')
def images(filename):
    font_dir = os.path.join(os.getcwd(), 'images')  # Шлях до теки з шрифтами
    return send_from_directory(font_dir, filename)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    global check
    global number
    if request.method == "GET":
        return render_template("reg.html", password="write your password here")
    else:
        pass1 = request.form['password']
        pass2 = request.form['rpassword']
        if pass1 != pass2:
            return render_template("reg.html", pdm=1, password=pass1)

        else:
            pass1 = str(pass1)
            if len(pass1) > 15: #15
                for i in numbers:
                    if i in pass1:
                        break
                    else:
                        continue
                else:
                    check = False
                    print("1")
                    return render_template("reg.html", password=pass1, err=1)
                if check == True:
                    for i in symbols:
                        if i in pass1:
                            break
                        else:
                            continue
                    else:
                        check = False
                        print("2")
                        return render_template("reg.html", password=pass1, err=1)
                    if check == True:
                        for i in small:
                            if i in pass1:
                                break
                            else:
                                continue
                        else:
                            check = False
                            print("3")
                            return render_template("reg.html", password=pass1, err=1)
                        if check == True:
                            for i in big:
                                if i in pass1:
                                    break
                                else:
                                    continue
                            else:
                                check = False
                                print("4")
                                return render_template("reg.html", password=pass1, err=1)
                            if check == True:
                                for i in drinks:
                                    if i in pass1:
                                        break
                                    else:
                                        continue
                                else:
                                    check = False
                                    print("5")
                                    return render_template("reg.html", password=pass1, err=1)
                                if check == True:
                                    for i in roman:
                                        if i in pass1:
                                            break
                                        else:
                                            continue
                                    else:
                                        check = False
                                        print("6")
                                        return render_template("reg.html", password=pass1, err=1)
                                    if check == True:
                                        for i in vnuk:
                                            if i in pass1:
                                                break
                                            else:
                                                continue
                                        else:
                                            check = False
                                            print("7")
                                            return render_template("reg.html", password=pass1, err=1)
                                        if check == True:
                                            pass3 = pass1
                                            for i in pass3:
                                                try:
                                                    print(pass3)
                                                    number += int(i)
                                                    pass3=pass3.replace(i, "",1)
                                                    print("tried, ",number)
                                                except:
                                                    try:
                                                        number += int(translation[i])
                                                        pass3=pass3.replace(i, "", 1)
                                                        print("excepted, ", number)
                                                    except:
                                                        continue
                                            if number == 25:
                                                print("GOOD")
                                                return render_template("reg.html", go=1)
                                            else:
                                                return render_template("reg.html", password=pass1, err=1)

                                        else:
                                            return render_template("reg.html", password=pass1, err=1)

                                    else:
                                        return render_template("reg.html", password=pass1, err=1)
                                else:
                                    return render_template("reg.html", password=pass1, err=1)
                            else:
                                return render_template("reg.html", password=pass1, err=1)
                        else:
                            return render_template("reg.html", password=pass1, err=1)
                    else:
                        return render_template("reg.html", password=pass1, err=1)
                else:
                    return render_template("reg.html", password=pass1, err=1)
            else:
                return render_template("reg.html", password=pass1, err=1)


@app.route("/gift")
def gift():
    return render_template("gift.html")


#return render_template("reg.html", go=1)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")