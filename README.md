# C3-Project


**About**

This project is about creating a pizza before ordering I have used Rest Apis for better quality.so bascially it form just like normal any form except
hear the should be able pick one size and type of pizza and also they should be able to select multipile kinds of toppins on pizza like u knon extra cheese 
some thing of that sort i have reffred some of the top franchises the reference.

# Lets get started
  
  **Before u need to install git and django**
  
  **Install Git for linux**
  If you want to install the basic Git tools on Linux via a binary installer, you can generally do so through the 
  package management tool that comes with your distribution. If you’re on Fedora (or any closely-related RPM-based distribution, such as RHEL or CentOS), 
  you can use dnf insted of apt
  
    $ sudo apt install git-all
    
**Run the Project :**

  First clone the project into your local machine  and the try to install requirements.txt file all the dependinces required to run the project will 
  get install automatically
    
    git clone https://github.com/bobbyprs/C3-Project.git
    
   **installing Dependencys**
   
    pip install -r requirements.txt
    
   **This step is optional unless if you are adding a new database then this is required steap**
      
      python manage.py makemigrations
      
   **Make shure you migrate it is good check ones**
   
      python manage.py migrate
   **For running the Project**
   
   Ones u have complected all the above steps u have to activate the virtual env u can install by refering to 
   this link:https://www.javatpoint.com/django-virtual-environment-setup  or else u can use the djangoenv folder      
   **Make shure you not running project with out activating vitual env**
   
      python manage.py runserver
   
  # Into The Project
  
  There are three phases as soon as u start Click on the this url give below where u can add your type of toppings for example Veg and Non Veg 
  the reson why i did this because u can add every thing dynamiclly and it saves lot of time because now u dont have to alter the code every time
  u want to change the items and this model is for vender side s
    
       'API Root': http://127.0.0.1:8000/pizza/
        
       'types':http://127.0.0.1:8000/pizza/types/
  
  **From this url u can add toppins**
        
         "toppings": "http://127.0.0.1:8000/pizza/toppings/"
         
   **This is urls for main objective create pizza for update delete press on link given bellow id**
   
          "pizza": "http://127.0.0.1:8000/pizza/pizza/",
  **for the filter i have also done the filter button which u ca seeon top right where get button is preasent i have added two fields for filtering
  you can add more if want in the views.py**
  

