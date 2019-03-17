# All currency amounts are in US Dollars.

import random

# Imported data from iplt20.com by copying and pasting.
firstName = ["Brendon", "Chris", "Lasith", "Colin", "Shaun", "Corey", "Sam", "Angelo", "Darcy", "Eoin", "Alex", "Jonny", "Jaydev", "Morne", "Dale", "Rilee", "Luke", "James", "Alex", "Liam", "Martin", "Moises", "Chris", "Axar ", "Yuvraj", "Wriddhiman ", "Mohammad", "Adam", "Hashim", "Usman", "Lockie", "Kane", "Joe", "Dan", "JP", "Ben", "James", "Mark", "Steven", "Carlos", "Naman ", "Nicholas", "Ishant", "Jason", "James", "Kusal", "Luke", "Darren", "Lendl", "Tymal", "Hardus", "Sikandar", "David", "Harry", "Matt", "Marchant", "Dwayne", "Shimron", "Cheteshwar ", "Manoj ", "Hanuma", "Gurkeerat", "Ben", "Varun", "Mohit", "Fawad", "Khary", "Rahul", "Reeza", "Saurabh", "Hazratullah", "Rishi", "Parvez", "Heinrich", "Glenn", "Mushfiqur", "Mithun", " R Vinay ", "Barinder", "Anton", "Faiz", "Aiden", "Irfan", "Thisara", "Rovman", "Johnson", "Andre", "Shafiqullah", "Mohammad", "Brendan", "Manpreet", "Gulbadin", "Oshane", "Fabian", "Doug", "Mohammed", "Paul", "Ashton", "Sean", "Junior", "Ashoke", "Obed", "Seth", "Robbie", "Liam", "Jeevan", "Keemo", "Vernon", "Dasun", "Isuru", "Sheldon", "Dane", "Sayed", "Sudeep", "Neil", "Ryan", "Samit", "Jon-Jon", "Jack", "Rassie", "Zahir Khan", "Sherfane", "Ali", "Lewis", "Patrick", "Laurie", "Jamie", " Riley", "Ben", "Anureet Singh", "Ishwar ", "Chris", "Aniruda", "Pradeep", "Cameron", "K", "Sachin", "Ankeet", "Armaan", "Devdutt", "Anmolpreet", "Manan", "Ayush", "Varun", "Shivam", "Sarfaraz", "Akshdeep ", "Jalaj", "Ankush", "Arun Karthick", "K.S", "Baba", "Sheldon", "Anuj", "Aniket", "Tushar", "Rajneesh", "Chama", "Ishan", "Nathu", "Murugan", "K C", "Yuvraj", "Ravi ", "Jagadeesha", "Ruturaj", "Priyam ", "Amandeep", "K Rohit", "R ", "Tajinder", "Pravin", "Shubham", "Atit", "Ronit", "Anrich", "Qais", "Zeeshan", "Satyajeet", "Bhargav", "Rajesh", "Stephan", "Unmukt ", "Abhimanyu", "Chirag", "Kattingeri Ashwin", "Himanshu", "Sarthak", "Akshath ", "Himmat", "Baba", "Sandeep", "Akash", "Subodh", "Hiten", "Karim", "Saurabh", "Diwesh", "Bipul", "Atharwa", "Mohammed", "Harvik ", "Kedar", "Nikhil", "Mahesh ", "Ryan", "Jitesh", "Vishnu", "Manjeetkumar", "Yash ", "Royston", "Umar Nazir", "Chetan", "Kuldeep", "Kanishk", "Rahul", "Arshdeep", "Jaskaran", "Aaron", "Sandeep", "Siddharth", "Rajat", "Pappu", "Pradeep", "Karanveer", "Gurvinder", "Kushaal", "Tanmay", "Harpreet", "Ishank", "Sharad ", "Tanmay", "Virat ", "Treyaksh ", "Ajit", "Pankaj", "Roosh", "Milind", "Shamss", "Darshan", "Sairaj", "Jack", "Swapnil", "Shashank", "Lalit", "Samarpit", "Aryan", "Sumanth", "Anmol", "Urvil", "Sharath", "Ajay", "Prabhsimran", "Upendra Singh", "Badrey", "Bandaru", "Stephen", "Rasikh", "Mohit", "Suraj", "Mohsin", "Ravi Kiran", "Nidheesh", "Safvan", "Kushang", "Tanveer", "Lalith ", "Prithvi Raj", "Rajesh", "Swapnil", "Priyank", "Rajat", "Dwaraka", "Prayas Ray ", "Ashok", "Riyan", "Akash", "Jason", "Pratyush", "Shamar", "Milind", "R", "R.Sanjay", "Ravi ", "Ashish", "Lukman Hussain", "Babasafi", "Pankaj ", "Anupam", "Lutho", "Pawan", "Blair", "Kartik", "Ajay", "Kuldip", "Johannes", "Shubham Singh", "Ganesh", "Naushad", "Pite", "Jake", "Iqbal", "Shubham", "Agnivesh", "Jay", "Harpreet ", "Vinod ", "Akshay ", "Arun", "Shiva", "Ankit", "Jason", "Shadley", "Manzoor", "Puneet", "Pavan", "Aakarshit", "Mehdi", "Akhil", "Venkatesh", "Dharmendrasinh", "Anirudha", "Akshay", "Aman", "Shrikant", "Shreekant", "Karanveer", "Chirag", "Tanush", "Vishal ", "Dhrumil", "Akul", "Suyash", "Suryakant", "T", "Dhruva Kumar", "Sumit", "Aaron", "Jatin", "Ekant", "Kshitiz", "Mrinank", "Mukesh Kumar", "Vivek", "Sanvir ", "Shiva", "Gurinder ", "Utkarsh", "Mayank", "Pranav", "Harsh"]
surname = ["McCullum", "Woakes", "Malinga", "Ingram", "Marsh", "Anderson", "Curran", "Mathews", "Short", "Morgan", "Hales ", "Bairstow", "Unadkat", "Morkel", "Steyn", "Rossouw", "Wright", "Faulkner", "Carey", "Dawson", "Guptill", "Henriques", "Jordan", "Patel", "Singh", "Saha", "Shami", "Zampa", "Amla", "Khawaja", "Ferguson", "Richardson", "Denly", "Christian", "Duminy", "Laughlin", "Pattinson", "Wood", "Finn", "Brathwaite", "Ojha", "Pooran", "Sharma", "Holder", "Neesham", "Perera", "Ronchi", "Bravo", "Simmons", "Mills", "Viljoen", "Raza", "Wiese", "Gurney", "Henry", "De Lange", "Smith", "Hetmyer", "Pujara", "Tiwary", "Vihari", "Singh", "McDermott", "Aaron", "Sharma", "Ahmed", "Pierre", "Sharma", "Hendricks", "Tiwary", "Zazai", "Dhawan", "Rasool", "Klaasen", "Phillips", "Rahim", "Abhimanyu", "Kumar", "Sran", "Devcich", "Fazal", "Markram", "Pathan", "Perera", "Powell", "Charles", "Fletcher", "Shafiq", "Shahzad", "Taylor", "Grewal", "Naib", "Thomas", "Allen", "Bracewell", "Mahmudullah", "Stirling", "Turner", "Abbott", "Dala", "Dinda", "Mccoy", "Rance", "Frylinck", "Livingstone", "Mendis", "Paul", "Philander", "Shanaka", "Udana", "Cottrell", "Paterson", "Shirzad", "Tyagi", "Wagner", "Mclaren", "Patel", "Smuts", "Wildermuth", "Van Der Dussen", "Pakteen", "Rutherford", "Khan", "Gregory", "Brown", "Evans", "Overton", " Meredith", "Dwarshuis", "Kathuria", "Pandey", "Green", "Srikkanth", "Sangwan", "Delport", "Vignesh", "Baby", "Bawane", "Jaffer", "Padikkal", "Singh", "Vohra", "Badoni", "Chakaravarthy", "Dube", "Khan", "Nath", "Saxena", "Bains", "Basker", "Bharat", "Indrajith", "Jackson", "Rawat", "Choudhary", "Deshpande", "Gurbani", "Milind", "Porel", "Singh", "Ashwin", "Cariappa", "Chudasama", "Sai Kishore", "Suchith", "Gaikwad", "Garg", "Khare", "Rayudu", "Samarth", "Dhillon", "Dubey", "Ranjane", "Sheth", "More", "Nortje", "Ahmad", "Ansari", "Bachhav", "Bhatt", "Bishnoi", "Myburgh", "Chand", "Easwaran", "Gandhi", "Hebbar", "Rana", "Ranjan", "Reddy", "Singh", "Aparajith", "Bavanaka", "Bhandari", "Bhati", "Dalal", "Janat", "Kumar", "Pathania", "Sharma", "Taide", "Azharudeen", "Desai", "Devdhar", "Naik", "Rawat", "Rickelton", "Sharma", "Vinod", "Chaudhary", "Dayal", "Dias", "Mir", "Sakariya", "Sen", "Seth", "Shukla", "Singh", "Singh", "Summers", "Warrier", "Desai", "Goel", "Roy", "Sahu", "Singh", "Singh", "Wadhwani", "Agarwal", "Bhatia", "Jaggi", "Lumba", "Mishra", "Singh", "Bali", "Chahal", "Jaswal", "Kalaria", "Kumar", "Mulani", "Nalkande", "Patil", "Prestwidge", "Singh", "Singh", "Yadav", "Joshi", "Juyal", "Kolla", "Malhotra", "Patel", "Ravi", "Rohera", "Singh", "Yadav", "Alam", "Ayyappa", "Chipurupalli", "Dar", "Jangra", "Kamath", "Khan", "Majeti", "MD", "Patel", "Patel", "Ul Haq", "Yadav", "Yarra", "Bishnoi Sr ", "Gugale", "Panchal", "Patidar", "Ravi Teja", "Barman", "Menaria", "Parag", "Parkar", "Sangha", "Singh", "Springer", "Tandon", "Vivek", "Yadav", "Balhara", "Hooda", "Meriwala", "Pathan", "Rao", "Sanklecha", "Sipamla", "Suyal", "Tickner", "Tyagi", "Yadav", "Yadav", "Malan", "Rohilla", "Satish", "Shaikh", "Van Biljon", "Weatherald", "Abdullah", "Agrawal", "Ayachi", "Bista", "Brar", "C V", "Chandran", "Chaprana", "Chauhan", "Sharma", "Smith", "Van Schalkwyk", "Dar", "Datey", "Deshpande", "Gomel", "Hasan", "Herwadkar", "Iyer", "Jadeja", "Joshi", "Karnewar", "Khan", "Mundhe", "Wagh", "Kaushal", "Khurana", "Kotian", "Kushwah", "Matkar", "Pandove", "Prabhudessai", "Pradhan", "Ravi Teja", "Reddy", "Ruikar", "Hardie", "Saxena", "Sen", "Sharma", "Singh", "Singh", "Singh", "Singh", "Singh", "Singh", "Singh", "Dagar", "Gupta", "Tyagi"]
basePrice = [280000, 280000, 280000, 280000, 280000, 280000, 280000, 280000, 280000, 280000, 210000, 210000, 210000, 210000, 210000, 210000, 210000, 210000, 210000, 210000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 56000, 56000, 56000, 56000, 56000, 56000, 56000, 56000, 42000, 42000, 42000, 42000, 42000, 42000, 42000, 42000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000, 28000]
country = ["New Zealand", "England", "Sri Lanka", "South Africa", "Australia", "New Zealand", "England", "Sri Lanka", "Australia", "England", "England", "England", "India", "South Africa", "South Africa", "South Africa", "England", "Australia", "Australia", "England", "New Zealand", "Australia", "England", "India", "India", "India", "India", "Australia", "South Africa", "Australia", "New Zealand", "Australia", "England", "Australia", "South Africa", "Australia", "Australia", "England", "England", "West Indies", "India", "West Indies", "India", "West Indies", "New Zealand", "Sri Lanka", "New Zealand", "West Indies", "West Indies", "England", "South Africa", "Zimbabwe", "South Africa", "England", "New Zealand", "South Africa", "West Indies", "West Indies", "India", "India", "India", "India", "Australia", "India", "India", "Australia", "West Indies", "India", "South Africa", "India", "Afghanistan", "India", "India", "South Africa", "New Zealand", "Bangladesh", "India", "India", "India", "New Zealand", "India", "South Africa", "India", "Sri Lanka", "West Indies", "West Indies", "West Indies", "Afghanistan", "Afghanistan", "Zimbabwe", "India", "Afghanistan", "West Indies", "West Indies", "New Zealand", "Bangladesh", "Ireland", "Australia", "Australia", "South Africa", "India", "West Indies", "New Zealand", "South Africa", "England", "Sri Lanka", "West Indies", "South Africa", "Sri Lanka", "Sri Lanka", "West Indies", "South Africa", "Afghanistan", "India", "New Zealand", "South Africa", "England", "South Africa", "Australia", "South Africa", "Afghanistan", "West Indies", "United States of America", "England", "England", "England", "England", " Australia", "Australia", "India", "India", "Australia", "India", "India", "South Africa", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "South Africa", "Afghanistan", "India", "India", "India", "India", "Netherlands", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "Afghanistan", "India", "India", "India", "India", "India", "India", "India", "India", "India", "South Africa", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "Australia", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "Australia", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "Australia", "India", "West Indies", "India", "India", "India", "India", "India", "India", "India", "India", "India", "South Africa", "India", "New Zealand", "India", "India", "India", "South Africa", "India", "India", "India", "South Africa", "Australia", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "South Africa", "South Africa", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "Australia", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India", "India"]
typeOfPlayer = ["BATSMAN", "ALL-ROUNDER", "BOWLER", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BATSMAN", "BATSMAN", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "WICKETKEEPER", "ALL-ROUNDER", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BOWLER", "BOWLER", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "BATSMAN", "BATSMAN", "BOWLER", "BOWLER", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BATSMAN", "BOWLER", "ALL-ROUNDER", "BOWLER", "ALL-ROUNDER", "BOWLER", "BATSMAN", "ALL-ROUNDER", " Bowler", "BOWLER", "BOWLER", "BOWLER", "ALL-ROUNDER", "WICKETKEEPER", "BOWLER", "ALL-ROUNDER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "WICKETKEEPER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BOWLER", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "BATSMAN", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "ALL-ROUNDER", "BATSMAN", "ALL-ROUNDER"]

# List of team names.
teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Rajasthan Royals", "Delhi Capitals", "Kings XI Punjab", "Sunrisers Hyderabad"]

# Budgets available for each team using real numbers.
MIBudget = 1561000
CSKBudget = 1176000
RCBBudget = 2541000
KKRBudget = 2128000
RRBudget = 2933000
DCBudget = 3570000
KXIPBudget = 5068000
SRHBudget = 1358000
# 2D list to be able to loop through later.
budgets = [MIBudget, CSKBudget, RCBBudget, KKRBudget, RRBudget, DCBudget, KXIPBudget, SRHBudget]

# Store the names of all retained players from previous season in the relevant list. The first number in each list represents the number of overseas players.
# Imported data from iplt20.com by copying and pasting.
MI = [7,"Mumbai Indians", "Adam Milne", "Aditya Tare", "Anukul Roy", "Ben Cutting", "Evin Lewis", "Hardik Pandya", "Ishan Kishan", "Jason Behrendorff", "Jasprit Bumrah", "Kieron Pollard", "Krunal Pandya", "Mayank Markande", "Mitchell McCleneghan", "Quinton de Kock", "Rahul Chahar", "Rohit Sharma", "Siddhesh Lad", "Surya Kumar Yadav"]
CSK = [8,"Chennai Super Kings", "Ambati Rayudu", "Asif K M", "Chaitanya Bishnoi", "David Willey", "Deepak Chahar", "Dhruv Shorey", "Dwayne Bravo", "Faf du Plessis", "Harbhajan Singh", "Imran Tahir", "Jagadeesan Narayan", "Karn Sharma", "Kedar Jadhav", "Lungisani Ngidi", "Mitchell Santner", "Monu Singh", "MS Dhoni", "Murali Vijay", "Ravindra Jadeja", "Sam Billings", "Shane Watson", "Shardul Thakur", "Suresh Raina"]
RCB = [6,"Royal Challengers Bangalore", "AB de Villiers", "Colin de Grandhomme", "Kulwant Khejroliya", "Marcus Stoinis", "Moeen Ali", "Mohammed Siraj", "Nathan Coulter-Nile", "Navdeep Saini", "Parthiv Patel", "Pawan Negi", "Tim Southee", "Umesh Yadav", "Virat Kohli", "Washington Sundar", "Yuzvendra Chahal"]
KKR = [3,"Kolkata Knight Riders", "Andre Russell", "Chris Lynn", "Dinesh Karthik", "Kamlesh Nagarkoti", "Kuldeep Yadav", "Nitish Rana", "Piyush Chawla", "Prasidh Krishna", "Rinku Singh", "Robin Uthappa", "Shivam Mavi", "Shubman Gill", "Sunil Narine"]
RR = [5,"Rajasthan Royals", "Ajinkya Rahane", "Aryaman Vikram Birla", "Benjamin Stokes", "Dhawal Kulkarni", "Gowtham Krishnappa", "Ish Sodhi", "Jofra Archer", "Jos Buttler", "Mahipal Lomror", "Prashant Chopra", "Rahul Tripathi", "Sanju Samson", "Shreyas Gopal", "Steve Smith", "Stuart Binny", "Sudhesan Midhun"]
DC = [4,"Delhi Capitals", "Amit Mishra", "Avesh Khan", "Chris Morris", "Colin Munro", "Harshal Patel", "Jayant Yadav", "Kagiso Rabada", "Manjot Kalra", "Prithvi Shaw", "Rahul Tewatia", "Rishab Pant", "Sandeep Lamichhane", "Shikhar Dhawan", "Shreyas Iyer", "Trent Boult"]
KXIP = [4,"Kings XI Punjab", "Andrew Tye", "Ankit Singh Rajpoot", "Chris Gayle", "David Miller", "Karun Nair", "KL Rahul", "Mandeep Singh", "Mayank Agarwal", "Mujeeb Zadran", "Ravichandran Ashwin"]
SRH = [4,"Sunrisers Hyderabad", "Abhishek Sharma", "Basil Thampi", "Bhuvneshwar Kumar", "Billy Stanlake", "David Warner", "Deepak Hooda", "Kane Williamson", "Manish Pandey", "Mohammad Nabi", "Rashid Khan", "Ricky Bhui", "Sandeep Sharma", "Shahbaz Nadeem", "Shakib Al Hasan", "Shreevats Goswami", "Siddarth Kaul", "Syed Khaleel Ahmed", "T Natarajan", "Vijay Shankar", "Yusuf Pathan"]
# 2D list to be able to loop through later.
teamList = [MI,CSK,RCB,KKR,RR,DC,KXIP,SRH]

# Create an "index" for each team, which will allow me to prevent teams who are ineligible to bid from bidding.
MIIndex = 0
CSKIndex = 0
RCBIndex = 0
KKRIndex = 0
RRIndex = 0
DCIndex = 0
KXIPIndex = 0
SRHIndex = 0
# 2D list to be able to loop through later.
teamIndexes = [MIIndex, CSKIndex, RCBIndex, KKRIndex, RRIndex, DCIndex, KXIPIndex, SRHIndex]

print("Please choose a team from the following list:")
# Loop through all teams and ask the user to enter a certain number for a specific team.
for i in range(len(teams)):
    print("Please enter {} for {}.".format(i+1, teams[i]))
# Validate the user entry using a type check and a range check.
while True:
    try:
        team = int(input())
        break
    except ValueError:
        print("Please enter using numbers only.")
while team > 8 or team < 1:
    print("Please enter a number between 1 and 8.")
    team = int(input())

# Store the chosen team's position in the list and the chosen team's name.
chosenTeamPosition = team - 1
chosenTeam = teamList[chosenTeamPosition][1]

# Set out the rules of the auction.
print("Auction rules:")
print("Maximum of 8 overseas players.\n"
    "Minimum of 18 players \n"
        "Maximum of 25 players")
# Set out instructions for bidding.
print("If you wish to bid for a player at any time, enter 1, followed by the amount you wish to bid.")
print("If you wish to fast-forward bidding for a single player at any time, enter 2.")

# Set some initial values for variables to be used later.
bid = 0
teamPosition = 10
playerFirstBid = False
unsold = False
counter = 0
unsoldAdjuster = random.randint(4,6)

# Offer the user the option to simulate the entire bidding process.
print("Do you wish to simulate the whole bidding process? If so, enter 1. Otherwise, enter any other number.")
# Validate the user input using a type check.
while True:
    try:
        simulateRequest = int(input())
        break
    except ValueError:
        print("Please input using numbers only.")

if simulateRequest != 1:
# Loop through all the players who are being auctioned.
    for i in range(len(firstName)):
# Reset the values of indexSum and limit for each new player.
        indexSum = 0
        limit = random.uniform(1.1,1.5)
# Loop through the indexes for all the teams.
        for m in range(len(teamIndexes)):
# Set the default value of the index to be 1, unless...
            teamIndexes[m] = 1
# ...the size of the team is already too big, or...
            if len(teamList[m]) >= 27:
                teamIndexes[m] = 0
# ...the player currently being auctioned is an overseas player, and all the overseas slots are filled.
            if teamList[m][0] >= 8:
                if country[i] != "India":
                    teamIndexes[m] = 0
# Work out the sum of all the indexes.
        for k in range(len(teamIndexes)):
            indexSum += teamIndexes[k]
# If no teams are able to bid for this player, skip the player.
        if indexSum == 0:
            continue
# If only one team is able to bid for this player, make sure they only pay the base price and not higher.
        if indexSum == 1:
            limit = 1
# Output the name of the player currently being auctioned.
        print("Bid for {}, {}".format(surname[i],firstName[i]))
# Output the details of the player currently being auctioned.
        print("Base price: ${}, Country: {}, Type: {}".format(basePrice[i],country[i],typeOfPlayer[i]))
# If the player is eligible to bid for the player currently being auctioned, allow bidding.
        if teamIndexes[chosenTeamPosition] == 1:
            print("To bid, enter 1. To fast-forward bidding on this player, enter 2. To wait, enter 0.")
# Validate the user input using a type check and a range check.
            while True:
                try:
                    request = int(input())
                    break
                except ValueError:
                    print("Please input using numbers only.")
            while request > 2:
                print("Please only enter the numbers 0, 1 or 2.")
                request = int(input())
# If the player is not eligible to bid for the player, skip the player.
        if teamIndexes[chosenTeamPosition] != 1:
            print("You are unable to bid for this player.")
            request = 2
# Only one in every 4-6 players should be sold (as this is realistic), unless the player bids for one of the players who would otherwise be unsold.
        if counter == unsoldAdjuster:
            unsold = True
        counter += 1
        if unsold == True:
            counter = 0
            unsoldAdjuster = random.randint(4,6)
        else:
            if request != 1:
                print("Player unsold.")
                continue
        unsold = False
# Create a more random nature to the teams that bid each time.
        rand1 = random.randint(0,len(teamList)-1)
        rand2 = random.randint(0,len(teamList)-1)
        rand3 = random.randint(0,len(teamList)-1)
# While the player has not been sold yet, keep allowing the bid to be raised.
        while True:
            for j in range(len(teamList)):
                if request != 2:
# If the player wishes to bid first, ask the user to enter a bid.
# This section of code will only run if the user is the first to bid.
                    if request == 1:
                        if playerFirstBid == False:
                            print("How much do you want to bid? Please enter in whole numbers only.")
# Validate the user input using a type check and a range check.
                            while True:
                                try:
                                    price = int(input())
                                    break
                                except ValueError:
                                    print("Please input using numbers only.")
                            while price < basePrice[i]:
                                print("Please enter a valid bid.")
                                price = int(input())
                            playerFirstBid = True
# If the bid entered is valid, update the current bid value and output the bid to the player.
                            if price >= basePrice[i]:
                                if price <= budgets[j]:
                                    bid = price
                                    print("Current bid from {}: ${}".format(chosenTeam,bid))
# Update the information about who bid last.
                                    winningTeam = chosenTeam
                                    teamPosition = chosenTeamPosition
# Make sure the computer doesn't bid on behalf of the player.
                    if j == chosenTeamPosition:
                        continue
# Create a more random nature to the teams that bid each time.
                if teamIndexes[rand1] == 1 and teamIndexes[rand2] == 1 and teamIndexes[rand3] == 1:
                    if j != rand1 and j != rand2 and j != rand3 and j != chosenTeamPosition:
                        continue
# If the bid isn't already unrealistically high, if a team can afford to raise the bid, and if the team is eligible to bid, let them raise.
                if bid <= (limit * basePrice[i]):
                    if (bid + 5000) <= budgets[j]:
                        if teamIndexes[j] == 1:
                            bid += 5000
# Update the information about who bid last.
                            teamPosition = j
# Set the bid to be the base price if the user chooses not to bid first or if the user chooses to skip this player.
                        if request == 0:
                            if playerFirstBid == False:
                                bid = basePrice[i]
                                playerFirstBid = True
                        if request == 2:
                            if playerFirstBid == False:
                                bid = basePrice[i]
                                playerFirstBid = True
# Set the bid to be the base price if only one team is bidding.
                        if limit == 1:
                            bid = basePrice[i]
                        print("Current bid from {}: ${}".format(teamList[j][1],bid))
                        winningTeam = teamList[j][1]
                        if request != 2:
                            if teamIndexes[chosenTeamPosition] != 1:
                                print("You are unable to bid for this player.")
                                request = 2
# Offer the user another opportunity to bid.
                            if teamIndexes[chosenTeamPosition] == 1:
                                print("Do you wish to bid now? If so, enter 1. Otherwise, enter 0.")
# Validate the user input using a type check and a range check.
                                while True:
                                    try:
                                        request = int(input())
                                        break
                                    except ValueError:
                                        print("Please input using numbers only.")
                                while request > 2:
                                    print("Please only enter the numbers 0, 1 or 2.")
                                    request = int(input())
                                if request == 1:
                                    print("How much do you want to bid? Please enter in whole numbers only.")
                                    while True:
                                        try:
                                            price = int(input())
                                            break
                                        except ValueError:
                                            print("Please input using numbers only.")
                                    while price < basePrice[i]:
                                        print("Please enter a valid bid.")
                                        price = int(input())
                                    if price > bid:
                                        if price <= budgets[j]:
                                            bid = price
                                            print("Current bid from {}: ${}".format(chosenTeam,bid))
                                            winningTeam = chosenTeam
                                            teamPosition = chosenTeamPosition
# Once the bid has become reasonably high, end the bidding.
            if bid >= (limit * basePrice[i]):
                break
# Output the name of the player sold, the winning team and the amount.
        print("{}, {} sold to {} for ${}".format(surname[i],firstName[i],winningTeam,bid))
# Update the list of the winning team with the name of the new player, and adjust the budget to reflect the purchase.
        name = "{} {}".format(firstName[i], surname[i])
        teamList[teamPosition].append(name)
        budgets[teamPosition] -= bid
# If the player is overseas, adjust the overseas counter.
        if country[i] != "India":
            teamList[teamPosition][0] += 1
# Reset the values of bid and playerFirstBid for the next player.
        bid = 0
        playerFirstBid = False

if simulateRequest == 1:
    for i in range(len(firstName)):
        indexSum = 0
        limit = random.uniform(1.1,1.5)
        if counter == unsoldAdjuster:
            unsold = True
        counter += 1
        if unsold == True:
            counter = 0
            unsoldAdjuster = random.randint(4,6)
            unsold = False
        else:
            continue
# Set a starting value for the bid.
        bid = basePrice[i]
        for j in range(len(teamList)):
            teamIndexes[j] = 1
            if len(teamList[j]) >= 27:
                teamIndexes[j] = 0
            if teamList[j][0] >= 8:
                if country[i] != "India":
                    teamIndexes[j] = 0
        for j in range(len(teamIndexes)):
            indexSum += teamIndexes[j]
        if indexSum == 0:
            continue
        if indexSum == 1:
            limit = 1
        while True:
            for j in range(len(teamList)):
                if bid <= (limit * basePrice[i]):
                    if (bid + 5000) <= budgets[j]:
                        if teamIndexes[j] == 1:
                            bid += 5000
                            teamPosition = j
                            if limit == 1:
                                bid = basePrice[i]
                        winningTeam = teamList[j][1]
            if bid >= (limit * basePrice[i]):
                break
        name = "{} {}".format(firstName[i], surname[i])
        teamList[teamPosition].append(name)
        budgets[teamPosition] -= bid
        if country[i] != "India":
            teamList[teamPosition][0] += 1
        bid = 0

# Loop through each team and output the players in the team (including both retained and newly bought players).
for i in range(len(teamList)):
    print("This is a list of all the players for {}:".format(teamList[i][1]))
    for j in range(len(teamList[i])):
        if j <= 1:
            continue
        print(teamList[i][j])