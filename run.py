from API import create_app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True,port=1250,host='0.0.0.0')