from website import create_app
import sys

# Check if at least one command-line argument is provided
if len(sys.argv) < 2:
    print("No Port Number found -- Usage: python main.py <port_number>")
    sys.exit(1)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True , port=sys.argv[1] , host="0.0.0.0")
