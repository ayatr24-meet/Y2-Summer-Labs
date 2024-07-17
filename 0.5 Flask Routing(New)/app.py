from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''
        <h1>Intrest Things</h1> 
        <p> Welcome to the photo gallery containing three types of photos:food,pets,also outer space </p>
        <a href="/food1">Go to the first food photo </a>
        <a href="/pet1">Go to pet1</a>
        <a href="/space1">Go to space</a>

'''
 
@app.route('/food1')  
def food1():
    return '''
        <h1>food1</h1>
        <img src="https://img.taste.com.au/9isesBer/taste/2016/11/caramello-cake-105070-1.jpeg" style="width:400px">
        <a href='/home'>home</a>
        <a href='/food2'>food2</>
''' 
    

@app.route('/food2')
def food2():
    return '''
        <h1>food2</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAq4ziaXhoJg89d9OB-SpZio58jpGYqgnPcg&s" style="width:400px">
        <a href='/home'>home</a>
        <a href='/food3'>food3</a>
        <a href='/food2'>food2</a>
'''



@app.route('/food3')
def food3():
    return '''
        <h1>food3</h1>
        <img src="https://www.allrecipes.com/thmb/0xH8n2D4cC97t7mcC7eT2SDZ0aE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6776_Pizza-Dough_ddmfs_2x1_1725-fdaa76496da045b3bdaadcec6d4c5398.jpg" style="width:400px">
        <br>
        <a href='/home'>home</a>
    '''  

@app.route('/pet1')    
def pet1():
    return '''
        <h1>its pet1</h1>
        <img src="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_3x4.jpg" style="width:400px">
        <a href='/home'>home</a>
        <a href='/pet2'>pet2</a>

'''

@app.route('/pet2')    
def pet2():
    return '''

        <h1>Pet2</h1>
        <img src="https://www.princeton.edu/sites/default/files/styles/1x_full_2x_half_crop/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=Bg2K7j7J" >
        <a href='/home'>home</a>
        <a href='/pet3'>pet3</a>

'''
@app.route('/pet3')
def pet3():  # Fixed indentation here
    return '''
        <h1>pet3</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo_bksr9rjtoSpWpkK7RJcBGFI6Avz9YByNA&s" style="width:400px">
        <br>
        <a href='/home'>home</a>
        <br>
        <a href='/pet2'>pet2</a>
        '''

@app.route('/space1')
def space1():
    return '''
        <h1>space1</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSva80qn921XF6JDyEMAvAcAibZTDL4nIuOdA&s" style="width:400px">
        <a href='/home'>home</a>
        <a href='/space2'>Go to space2</a>

'''

@app.route('/space2')
def space2():
    return '''
        <h1>space2</h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/1200px-Webb%27s_First_Deep_Field.jpg" style="width:400px">
        <br>
        <a href='/home'>home</a>
        <br>
        <a href='/space3'>go to space3</a>
        '''

@app.route('/space3')
def space3():
    return '''
        <h1>Space3</h1>
        <img src="https://starwalk.space/gallery/images/biggest-water-sourse-in-space/1920x1080.jpg" style="width:400px">
        <br>
        <a href='/home'>Go to home</a>
        <br>
        <a href='/space2'>Go to space2</a>
        <br>
        <a href='/space1'>Go to space1</a>
    '''

  

if __name__ == '__main__':
    app.run(debug=True)

