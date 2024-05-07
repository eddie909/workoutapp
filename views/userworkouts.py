from flask import Blueprint,render_template,flash,request,redirect,jsonify
from controllers.userworkouts import (viewWorkouts,deleteUserWorkout,changeSets,changeDay)
from controllers.routines import getRoutine
from flask_jwt_extended import jwt_required, get_jwt_identity

userworkout_views=Blueprint('userworkout_views',__name__,template_folder='../Templates')


@userworkout_views.route('/user_workouts/<value>',methods=['GET'])
@jwt_required()
def user_workouts_page(value):
    workouts=viewWorkouts(value,get_jwt_identity())

    routine=getRoutine(value,get_jwt_identity())
    name=routine.name
    
    
    return render_template('userworkouts.html',workouts=workouts,routineName=name,routine=routine)


@userworkout_views.route('/deleteWorkout',methods=['POST'])
@jwt_required()
def delete_Workout():
    data=request.form
    deleted=deleteUserWorkout(data['workout_id'],data['routine_id'],get_jwt_identity())
    if deleted:
        flash('Workout deleted successfully','success')
    else:
        flash('Workout not deleted','danger')
    return redirect(request.referrer)


@userworkout_views.route('/editsets',methods=['POST'])
@jwt_required()
def editSets():
    data=request.form
    sets=data['sets']
    id=data['id']
    changeSets(id,sets)
    flash('Sets changed successfully','success')
    return redirect(request.referrer)


@userworkout_views.route('/editday',methods=['POST'])
@jwt_required()
def editDay():
    data=request.form
    
    changeDay(data['workout_id'],data['routine_id'],get_jwt_identity(),data['day'])
    flash('Day changed successfully','success')
    return redirect(request.referrer)