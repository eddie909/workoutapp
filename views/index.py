from flask import Blueprint,render_template,url_for,flash,request,redirect,jsonify
from controllers import workouts
from flask_jwt_extended import jwt_required,current_user


index_views=Blueprint('index_views',__name__,template_folder='../Templates')

"""
Home page of the application
Displays all the workouts
"""
@index_views.route('/home',methods=['GET']) 
@jwt_required()
def home():
    bodyparts={
        "Muscles":{
            "Back":"https://barbend.com/wp-content/uploads/2019/04/Back-Muscles.jpg",
            "Cardio":"https://th.bing.com/th/id/OIP.9Rt_g5GeYJHYxkqAG85cygHaGe?rs=1&pid=ImgDetMain",
            "Chest":"https://th.bing.com/th/id/R.0c90b0441cc12ddf6ae38104eb8e3499?rik=C60VmMRY78KgpQ&pid=ImgRaw&r=0",
            "Lower Arms":"https://doctorlib.info/anatomy/classic-human-anatomy-motion/classic-human-anatomy-motion.files/image272.jpg",
            "Lower Legs":"https://knowledge.carolina.com/wp-content/uploads/2021/11/shutterstock_674183425.jpg",
            "Neck":"https://darebee.com/images/workouts/neck-workout.jpg",
            "Shoulders":"https://cdn.shopify.com/s/files/1/1214/5580/files/Muscle_Group_Shoulders.jpg?v=1601051035",
            "Upper Arms":"https://doctorlib.info/anatomy/classic-human-anatomy-motion/classic-human-anatomy-motion.files/image266.jpg",
            "Upper Legs":"https://th.bing.com/th/id/OIP.Q-_g3kwsGKjqpCiwI7tcbwHaH6?rs=1&pid=ImgDetMain",
            "Waist":"https://th.bing.com/th/id/OIP.uyY1YbtyMHh8Fk3IIVgWuwHaHf?rs=1&pid=ImgDetMain"
               }
    }
    
    return render_template('home.html',bodyparts=bodyparts)


