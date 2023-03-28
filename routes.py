from models import *
from forms import *

@app.route("/login", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('groups'))
            else:
                flash('User password is incorrect!!!', category='error')
        else:
            flash('User email is incorrect!!!', category='error')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logout', category='success')
    return redirect(url_for('login'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        date = datetime.fromtimestamp(math.floor(time.time()))
        checkUserName = len([i for i in Users.query.filter_by(userName=form.userName.data)])
        checkEmail = len([i for i in Users.query.filter_by(email=form.email.data)])
        
        if form.password1.data == form.password2.data and checkUserName == 0 and checkEmail == 0:
            hashpass = generate_password_hash(form.password1.data)
            addDateToDB = Users(userName=form.userName.data, email=form.email.data, password=hashpass, date=date)
            db.session.add(addDateToDB)
            db.session.commit()
            
            if addDateToDB:
                flash('User registered successfully', category='success')
                return redirect(url_for('login'))
        else:
            if checkUserName > 0:
                flash(
                    'A user with this username already exists, please choose another username.', category='error')
            elif checkEmail > 0:
                flash(
                    'A user with this email already exists, please choose another email.', category='error')
            elif form.password1.data != form.password2.data:
                flash('Password mismatch!!!', category='error')
    return render_template("register.html", form=form)

@app.route("/groups", methods=['GET', 'POST'])
@login_required
def groups():
    form = AddGroup()
    dataGroupsDB = TripGroup.query.all()
    return render_template("groups.html", form=form, dataGroupsDB=dataGroupsDB)

@app.route("/<string:title>", methods=['GET', 'POST'])
@login_required
def bills(title):
    form = Bills()
    dataBillsDB = BillsGroup.query.filter_by(groupId = title)
    if form.validate_on_submit():     
            addDateToDB = BillsGroup(amount=form.amout.data, discription=form.discription.data, groupId = form.groupid.data)
            db.session.add(addDateToDB)
            db.session.commit()
            return redirect(url_for("groups"))
    return render_template("bills.html", title=title, form=form, dataBillsDB=dataBillsDB)

# ERRORS PAGES

@app.errorhandler(500)
def pageError500(error):
    return render_template("error500.html"), 500


# ----------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)