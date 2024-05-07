from flask import Blueprint,render_template,url_for,flash,request,redirect,jsonify
from controllers import workouts, userworkouts,routines
from flask_jwt_extended import jwt_required, get_jwt_identity


workout_views=Blueprint('workout_views',__name__,template_folder='../Templates')


@workout_views.route('/workouts/<value>',methods=['GET'])
@jwt_required()
def workouts_page(value):
    value=value.lower()
    all_workouts=workouts.getWorkoutbyBody(value)
    all_routines=routines.getRoutines(get_jwt_identity())
    return render_template('workouts.html',all_workouts=all_workouts,all_routines=all_routines,value=value.capitalize())


@workout_views.route('/addWorkout',methods=['POST'])
@jwt_required()
def addWorkout():
    data=request.form
    r=data['routine_id']
    w=data['workout_id']
    day=data['day']
    id=get_jwt_identity()
    print(f'Workout {w} Added to {r} day:{day}')
    userworkouts.addUserWorkout(w,r,day,id)

    flash('Workout added successfully','success')
    return redirect(request.referrer)