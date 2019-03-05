import os
from views import app
#app.run(debug=True)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
