from flask import Flask, render_template
app = Flask(__name__)
# start page
@app.route("/")
def home():
    #return "Hi Sam!"
    return render_template("other/START.html")
    
# (MAIN ROOM STUFF)
# main room
@app.route('/mxbcjqm7')
def _2():
    return render_template("main_room/room_main.html")
# locked front door
@app.route('/jg8mg9jq')
def _3():
    return render_template("main_room/inspect_end-door(locked).html")
# unlocked front door
@app.route('/33')
def _4():
    return render_template("main_room/inspect_end-door(unlocked).html")
# go insane
@app.route('/tqiwpjs0')
def _5():
    return render_template("main_room/death_insanity.html")
# glass door
@app.route('/hu8miaw3')
def _6():
    return render_template("main_room/inspect_glass-door.html")
# balcony
@app.route('/325vqvgp')
def _7():
    return render_template("main_room/room_balcony.html")
# inspect duck
@app.route('/ayzdx0ah')
def _8():
    return render_template("main_room/inspect_duck.html")
# fall
@app.route('/p024ygql')
def _9():
    return render_template("main_room/death_falling.html")
# inspect painting
@app.route('/urjxrku1')
def _10():
    return render_template("main_room/inspect_painting.html")
# bedroom door
@app.route('/w5wn5lk4')
def _11():
    return render_template("main_room/inspect_bedroom.html")
# (BEDROOM STUFF)
# bedroom
@app.route('/jimmy')
def _12():
    return render_template("bedroom/room_bedroom.html")
# closet
@app.route('/edhx16r0')
def _13():
    return render_template("bedroom/room_closet.html")
# inspect skeleton
@app.route('/0begar2w')
def _14():
    return render_template("bedroom/inspect_skeleton.html")
# crack in the wall
@app.route('/j6kotm8e')
def _15():
    return render_template("bedroom/inspect_crack.html")
# punch/skeleton attack
@app.route('/y8nel1yi')
def _16():
    return render_template("bedroom/action_punch.html")
# death by starvation
@app.route('/caq5mhem')
def _17():
    return render_template("bedroom/death_starvation.html")
# tickle funny bone :)
@app.route('/a7zd70ah')
def _18():
    return render_template("bedroom/action_tickle.html")
# resist
@app.route('/96yd6z9g')
def _19():
    return render_template("bedroom/action_resist.html")
# dont resist
@app.route('/a7ze71ah')
def _20():
    return render_template("bedroom/action_dont-resist.html")
# bed and dresser
@app.route('/7gyyhnvf')
def _21():
    return render_template("bedroom/bed-dresser.html")
# inspect bed
@app.route('/l9bp9clj')
def _22():
    return render_template("bedroom/inspect_bed.html")
# sleep
@app.route('/ocsgospx')
def _23():
    return render_template("bedroom/action_sleep.html")
# inspect dresser
@app.route('/tev7p7fb')
def _24():
    return render_template("bedroom/inspect_dresser.html")
# read note
@app.route('/9jpqwd9t')
def _25():
    return render_template("bedroom/inspect_note.html")
# (OTHER STUFF)
# outside
@app.route('/zwo2vpz6')
def _26():
    return render_template("other/outside.html")

if __name__ == '__main__':
   app.run(debug=True, port=8080)
