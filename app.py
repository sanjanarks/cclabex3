from flask import Flask
app = Flask(__name__)

@app.route("/")
def sum();
num1=2
num2=3
sum=num1+num2
print(the sum is : , sum)
return 0

if __name__ == "__main__":
    app.run()
