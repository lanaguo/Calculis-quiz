from website import create_app  # imported from __init__

app = create_app()

if __name__ == '__main__': # run webserver only if main file is run
    app.run(debug=True) # runs flask application
# debug = true for development only so server reruns every time change is made
