from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample product data 
product_data = pd.DataFrame({
    'asin': ['B000050B6Z', 'B000001OMI', 'B0000YBX0W'],
    'summary': ['Product A', 'Product B', 'Product C'],
    'reviewText': ['This is a great product.', 'Amazing product!', 'Not satisfied.'],
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form['query']

    # Product Recommendation Using Advanced_Recommender
    # For demonstration purposes, we'll return sample product data
    recommended_products = product_data.sample(3)

    return render_template('recommendation.html', query=query, recommended_products=recommended_products)

if __name__ == '__main__':
    app.run(debug=True)
