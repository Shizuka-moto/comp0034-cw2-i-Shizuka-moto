# Import the required modules
from flaskapp import create_app
from flaskapp.config import ProdConfig

# Create an instance of the application with the production configuration
app = create_app(ProdConfig)

# Check if this script is run directly and not imported
if __name__ == '__main__':
    # Run the application with debug mode enabled
    app.run(debug=True)