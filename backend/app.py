from application import create_app

app = create_app(init_admin=True)
if __name__ == "__main__":
    app.run(debug=True)
    