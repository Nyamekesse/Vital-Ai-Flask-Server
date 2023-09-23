from main import create_app


app = create_app()

if __name__ == "__main__":
    app = create_app()
    print(f"VITAL AI SERVER RUNNING ON PORT 5001")
    app.run(debug=True, port=8005)
