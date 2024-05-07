from flask import Blueprint,render_template,url_for,flash,request,redirect,jsonify,session
from controllers.routines import *
from controllers.userworkouts import *
from flask_jwt_extended import jwt_required, get_jwt_identity

routine_views=Blueprint('routine_views',__name__,template_folder='../Templates')


@routine_views.route('/routines',methods=['GET'])
@jwt_required()
def routines_page():
    all_routines=getRoutines(get_jwt_identity())
    return render_template('routines.html',all_routines=all_routines)


@routine_views.route('/create',methods=['POST'])
@jwt_required()
def makeRoutine():
    data=request.form
    name=data['name']
    id=get_jwt_identity()
    createRoutine(name,id)
    flash('Routine created successfully','success')
 

    return redirect(request.referrer)


@routine_views.route('/deleteRoutine/<id>',methods=['POST'])
@jwt_required()
def delete_Routine(id):
    data=request.form
    print(id)
    deleted=deleteRoutine(id)

    if deleted:
        flash('Routine deleted successfully','success')
    else:
        flash('Routine not deleted','danger')

    return redirect(request.referrer)

  

@routine_views.route('/editname',methods=['POST'])
@jwt_required()
def editRoutineName():
    data=request.form
    name=data['name']
    new_name=data['new_name']
    renameRoutine(name,new_name)
    flash('Routine name updated successfully','success')
    return redirect(request.referrer)